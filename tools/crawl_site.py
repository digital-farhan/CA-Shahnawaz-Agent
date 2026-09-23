from __future__ import annotations

import csv
import hashlib
import json
import re
import time
from collections import Counter, defaultdict, deque
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import date
from pathlib import Path
from typing import Any
from urllib.parse import parse_qsl, urldefrag, urljoin, urlsplit, urlunsplit

import requests
from bs4 import BeautifulSoup


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "data" / "crawl"
AUDIT_DATE = date(2026, 8, 28)
HOME = "https://cashahnawaz.com/"
HOST = "cashahnawaz.com"
HEADERS = {"User-Agent": "Mozilla/5.0 (compatible; CashahnawazSEOAudit/1.0; +https://cashahnawaz.com/)"}


def write_csv(path: Path, headers: list[str], rows: list[list[Any]]) -> None:
    with path.open("w", newline="", encoding="utf-8-sig") as handle:
        writer = csv.writer(handle)
        writer.writerow(headers)
        writer.writerows(rows)


def normalize(url: str, keep_query: bool = True) -> str:
    url = urldefrag(url)[0]
    parts = urlsplit(url)
    scheme = "https" if parts.scheme in ("http", "https") else parts.scheme
    host = parts.netloc.lower().replace("www.", "")
    path = re.sub(r"/{2,}", "/", parts.path or "/")
    query = parts.query if keep_query else ""
    return urlunsplit((scheme, host, path, query, ""))


def internal(url: str) -> bool:
    return urlsplit(url).netloc.lower().replace("www.", "") == HOST


def get_xml(url: str) -> tuple[str, requests.Response]:
    response = requests.get(url, headers=HEADERS, timeout=30)
    response.raise_for_status()
    return response.text, response


def sitemap_urls() -> tuple[list[tuple[str, str]], dict[str, Any]]:
    robots_response = requests.get(HOME + "robots.txt", headers=HEADERS, timeout=30)
    robots_text = robots_response.text
    (OUT / f"robots-live-{AUDIT_DATE}.txt").write_text(robots_text, encoding="utf-8")
    maps = re.findall(r"(?im)^sitemap:\s*(\S+)", robots_text)
    if not maps:
        maps = [HOME + "sitemap_index.xml"]
    queue = deque(maps)
    seen_maps: set[str] = set()
    found: list[tuple[str, str]] = []
    map_status: list[dict[str, Any]] = []
    while queue:
        sm = queue.popleft()
        if sm in seen_maps:
            continue
        seen_maps.add(sm)
        try:
            text, response = get_xml(sm)
            soup = BeautifulSoup(text, "xml")
            children = [loc.get_text(strip=True) for loc in soup.find_all("loc")]
            is_index = soup.find("sitemapindex") is not None
            map_status.append({"url": sm, "status": response.status_code, "type": "index" if is_index else "urlset", "entries": len(children)})
            if is_index:
                queue.extend(children)
            else:
                for node in soup.find_all("url"):
                    loc = node.find("loc")
                    if not loc:
                        continue
                    lastmod = node.find("lastmod")
                    found.append((normalize(loc.get_text(strip=True)), lastmod.get_text(strip=True) if lastmod else ""))
        except Exception as exc:
            map_status.append({"url": sm, "status": "error", "error": str(exc)})
    return found, {"robots_status": robots_response.status_code, "sitemaps": map_status}


def jsonld_types(value: Any) -> list[str]:
    types: list[str] = []
    if isinstance(value, dict):
        raw_type = value.get("@type")
        if isinstance(raw_type, str):
            types.append(raw_type)
        elif isinstance(raw_type, list):
            types.extend(str(x) for x in raw_type)
        for child in value.values():
            types.extend(jsonld_types(child))
    elif isinstance(value, list):
        for child in value:
            types.extend(jsonld_types(child))
    return types


def link_location(node: Any) -> str:
    for parent in [node] + list(node.parents):
        name = getattr(parent, "name", None)
        if name in ("header", "nav", "footer", "main", "article", "aside"):
            return name
        classes = " ".join(getattr(parent, "get", lambda *_: [])("class", []) or []).lower()
        ident = str(getattr(parent, "get", lambda *_: "")("id", "")).lower()
        fingerprint = classes + " " + ident
        if "footer" in fingerprint:
            return "footer"
        if "header" in fingerprint or "menu" in fingerprint or "nav" in fingerprint:
            return "nav"
    return "body"


def classify(url: str, sitemap_source: str = "") -> str:
    path = urlsplit(url).path.lower()
    if path == "/":
        return "home"
    if "/category/" in path:
        return "category"
    if "/tag/" in path:
        return "tag"
    if any(x in path for x in ("contact", "about", "privacy", "terms")):
        return "business"
    if any(x in path for x in ("services", "registration", "compliance", "filing", "audit", "accounting", "bookkeeping", "taxation", "consultancy")):
        return "service"
    if "post-sitemap" in sitemap_source:
        return "article"
    return "page"


def fetch_page(url: str, in_sitemap: bool, lastmod: str) -> dict[str, Any]:
    started = time.perf_counter()
    try:
        response = requests.get(url, headers=HEADERS, timeout=45, allow_redirects=True)
        elapsed = round((time.perf_counter() - started) * 1000)
        final_url = normalize(response.url)
        content_type = response.headers.get("content-type", "")
        result: dict[str, Any] = {
            "url": url,
            "final_url": final_url,
            "status": response.status_code,
            "redirect_chain": " -> ".join(f"{h.status_code}:{normalize(h.url)}" for h in response.history),
            "redirect_hops": len(response.history),
            "response_ms": elapsed,
            "bytes": len(response.content),
            "content_type": content_type,
            "cache_control": response.headers.get("cache-control", ""),
            "x_robots_tag": response.headers.get("x-robots-tag", ""),
            "hsts": response.headers.get("strict-transport-security", ""),
            "server": response.headers.get("server", ""),
            "in_sitemap": in_sitemap,
            "lastmod": lastmod,
            "html": response.text if "html" in content_type else "",
            "links": [],
        }
        if not result["html"]:
            return result
        soup = BeautifulSoup(result["html"], "lxml")
        title = soup.title.get_text(" ", strip=True) if soup.title else ""
        desc = soup.find("meta", attrs={"name": re.compile(r"^description$", re.I)})
        robots = soup.find("meta", attrs={"name": re.compile(r"^robots$", re.I)})
        canonicals = [normalize(x.get("href", "")) for x in soup.find_all("link", attrs={"rel": lambda v: v and "canonical" in [str(z).lower() for z in (v if isinstance(v, list) else [v])]}) if x.get("href")]
        h1s = [x.get_text(" ", strip=True) for x in soup.find_all("h1")]
        h2s = [x.get_text(" ", strip=True) for x in soup.find_all("h2")]
        imgs = soup.find_all("img")
        forms = soup.find_all("form")
        json_scripts = soup.find_all("script", attrs={"type": re.compile(r"application/ld\+json", re.I)})
        schema_types: list[str] = []
        schema_errors = 0
        schema_faq_questions = 0
        for script in json_scripts:
            try:
                data = json.loads(script.string or script.get_text())
                schema_types.extend(jsonld_types(data))
                schema_faq_questions += json.dumps(data).count('"@type": "Question"') + json.dumps(data).count('"@type":"Question"')
            except Exception:
                schema_errors += 1
        for node in soup(["script", "style", "noscript", "svg", "template"]):
            node.decompose()
        body_text = soup.get_text(" ", strip=True)
        words = re.findall(r"\b[\w'-]+\b", body_text)
        links: list[dict[str, str]] = []
        tel_links: list[str] = []
        wa_links: list[str] = []
        for a in soup.find_all("a", href=True):
            href = a.get("href", "").strip()
            if href.startswith("tel:"):
                tel_links.append(href)
            if "wa.me" in href or "whatsapp" in href.lower():
                wa_links.append(href)
            absolute = urljoin(final_url, href)
            if absolute.startswith(("http://", "https://")) and internal(absolute):
                links.append({"target": normalize(absolute), "anchor": a.get_text(" ", strip=True)[:300], "location": link_location(a), "rel": " ".join(a.get("rel", []))})
        phone_text = sorted(set(re.findall(r"(?:\+?91[\s-]?)?[6-9]\d{9}", re.sub(r"[()\s-]", "", body_text))))
        html_lower = result["html"].lower()
        generators = [x.get("content", "") for x in BeautifulSoup(result["html"], "lxml").find_all("meta", attrs={"name": re.compile(r"generator", re.I)})]
        result.update({
            "title": title,
            "title_length": len(title),
            "meta_description": desc.get("content", "").strip() if desc else "",
            "meta_length": len(desc.get("content", "").strip()) if desc else 0,
            "meta_robots": robots.get("content", "").strip() if robots else "",
            "canonicals": canonicals,
            "canonical": canonicals[0] if canonicals else "",
            "h1s": h1s,
            "h1_count": len(h1s),
            "h2_count": len(h2s),
            "word_count": len(words),
            "content_hash": hashlib.sha256(" ".join(words).lower().encode("utf-8")).hexdigest(),
            "image_count": len(imgs),
            "images_missing_alt": sum(1 for x in imgs if not x.has_attr("alt")),
            "images_empty_alt": sum(1 for x in imgs if x.get("alt") == ""),
            "form_count": len(forms),
            "form_fields": sum(len(x.find_all(["input", "select", "textarea"])) for x in forms),
            "tel_links": sorted(set(tel_links)),
            "whatsapp_links": sorted(set(wa_links)),
            "phone_text": phone_text,
            "schema_blocks": len(json_scripts),
            "schema_types": sorted(set(schema_types)),
            "schema_errors": schema_errors,
            "schema_faq_questions": schema_faq_questions,
            "gtm_ids": sorted(set(re.findall(r"GTM-[A-Z0-9]+", result["html"]))),
            "ga_ids": sorted(set(re.findall(r"G-[A-Z0-9]+", result["html"]))),
            "generators": generators,
            "has_elementor": "elementor" in html_lower,
            "has_rankmath": "rank-math" in html_lower or "rankmath" in html_lower,
            "has_yoast": "yoast" in html_lower,
            "has_aioseo": "aioseo" in html_lower or "all in one seo" in html_lower,
            "has_litespeed": "litespeed" in html_lower,
            "has_cf7": "wpcf7" in html_lower or "contact-form-7" in html_lower,
            "has_wpforms": "wpforms" in html_lower,
            "links": links,
        })
        return result
    except Exception as exc:
        return {"url": url, "final_url": "", "status": "error", "error": str(exc), "in_sitemap": in_sitemap, "lastmod": lastmod, "links": []}


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    sm_urls, sm_meta = sitemap_urls()
    sitemap_map = {url: lastmod for url, lastmod in sm_urls}
    seeds = set(sitemap_map)
    seeds.add(HOME)
    seeds.add(HOME + "?jkit-ajax-request=jkit_elements")
    seeds.add(HOME + "gst-registration-services-india-a-guide-to-gst/")
    seeds.add(HOME + "privacy-policy/")
    results: list[dict[str, Any]] = []
    with ThreadPoolExecutor(max_workers=8) as pool:
        futures = {pool.submit(fetch_page, url, url in sitemap_map, sitemap_map.get(url, "")): url for url in sorted(seeds)}
        for future in as_completed(futures):
            results.append(future.result())

    discovered: set[str] = set()
    for result in results:
        for link in result.get("links", []):
            target = link["target"]
            if not any(key.startswith("utm_") for key, _ in parse_qsl(urlsplit(target).query)):
                discovered.add(target)
    new_urls = sorted(x for x in discovered if x not in seeds and len(parse_qsl(urlsplit(x).query)) <= 2)
    if new_urls:
        with ThreadPoolExecutor(max_workers=8) as pool:
            futures = {pool.submit(fetch_page, url, False, ""): url for url in new_urls[:500]}
            for future in as_completed(futures):
                results.append(future.result())

    by_url = {x["url"]: x for x in results}
    edges: list[list[Any]] = []
    inbound: Counter[str] = Counter()
    contextual_inbound: Counter[str] = Counter()
    adjacency: dict[str, set[str]] = defaultdict(set)
    for result in results:
        source = normalize(result["url"])
        for link in result.get("links", []):
            target = link["target"]
            edges.append([source, target, link["anchor"], link["location"], link["rel"]])
            inbound[target] += 1
            if link["location"] not in ("nav", "header", "footer"):
                contextual_inbound[target] += 1
            adjacency[source].add(target)
    depth: dict[str, int] = {HOME: 0}
    queue = deque([HOME])
    while queue:
        source = queue.popleft()
        for target in adjacency.get(source, set()):
            if target not in depth:
                depth[target] = depth[source] + 1
                queue.append(target)

    headers = [
        "url", "final_url", "status", "redirect_hops", "redirect_chain", "response_ms", "bytes", "content_type",
        "cache_control", "x_robots_tag", "hsts", "in_sitemap", "lastmod", "indexable", "canonical", "canonical_issue",
        "meta_robots", "title", "title_length", "meta_description", "meta_length", "h1_count", "h1s", "h2_count", "word_count",
        "image_count", "images_missing_alt", "images_empty_alt", "form_count", "form_fields", "tel_links", "whatsapp_links",
        "schema_blocks", "schema_types", "schema_errors", "gtm_ids", "ga_ids", "inbound_links", "contextual_inbound_links", "click_depth", "page_type",
    ]
    inventory_rows: list[list[Any]] = []
    for result in sorted(results, key=lambda x: x["url"]):
        url = normalize(result["url"])
        robots = (result.get("meta_robots", "") + "," + result.get("x_robots_tag", "")).lower()
        status = result.get("status")
        canonical = result.get("canonical", "")
        indexable = status == 200 and "noindex" not in robots
        canonical_issue = ""
        if indexable and not canonical:
            canonical_issue = "missing"
        elif canonical and canonical != normalize(result.get("final_url") or url):
            canonical_issue = "non-self"
        row_values = {
            **result,
            "indexable": indexable,
            "canonical_issue": canonical_issue,
            "inbound_links": inbound[url],
            "contextual_inbound_links": contextual_inbound[url],
            "click_depth": depth.get(url, "orphan"),
            "page_type": classify(url),
        }
        inventory_rows.append([
            "; ".join(row_values.get(h, [])) if isinstance(row_values.get(h), list) else row_values.get(h, "") for h in headers
        ])
    write_csv(OUT / f"url-inventory-{AUDIT_DATE}.csv", headers, inventory_rows)
    write_csv(OUT / f"internal-links-{AUDIT_DATE}.csv", ["source", "target", "anchor", "location", "rel"], edges)
    write_csv(OUT / f"sitemap-urls-{AUDIT_DATE}.csv", ["url", "lastmod"], [[u, lm] for u, lm in sorted(sm_urls)])

    schema_rows = []
    for result in sorted(results, key=lambda x: x["url"]):
        schema_rows.append([result["url"], result.get("schema_blocks", 0), "; ".join(result.get("schema_types", [])), result.get("schema_errors", 0), result.get("schema_faq_questions", 0)])
    write_csv(OUT / f"schema-inventory-{AUDIT_DATE}.csv", ["url", "jsonld_blocks", "schema_types", "parse_errors", "faq_questions"], schema_rows)

    indexable_results = [x for x in results if x.get("status") == 200 and "noindex" not in (x.get("meta_robots", "") + x.get("x_robots_tag", "")).lower()]
    title_counts = Counter(x.get("title", "") for x in indexable_results if x.get("title"))
    desc_counts = Counter(x.get("meta_description", "") for x in indexable_results if x.get("meta_description"))
    summary = {
        "audit_date": str(AUDIT_DATE),
        "sitemap": sm_meta,
        "sitemap_url_count": len(sm_urls),
        "crawled_url_count": len(results),
        "status_counts": dict(Counter(str(x.get("status")) for x in results)),
        "indexable_count": len(indexable_results),
        "missing_canonical": [x["url"] for x in indexable_results if not x.get("canonical")],
        "nonself_canonical": [{"url": x["url"], "canonical": x.get("canonical")} for x in indexable_results if x.get("canonical") and x.get("canonical") != normalize(x.get("final_url") or x["url"])],
        "missing_title": [x["url"] for x in indexable_results if not x.get("title")],
        "missing_meta": [x["url"] for x in indexable_results if not x.get("meta_description")],
        "missing_h1": [x["url"] for x in indexable_results if not x.get("h1s")],
        "multiple_h1": [x["url"] for x in indexable_results if len(x.get("h1s", [])) > 1],
        "duplicate_titles": {k: v for k, v in title_counts.items() if v > 1},
        "duplicate_descriptions": {k: v for k, v in desc_counts.items() if v > 1},
        "sitemap_not_200": [x["url"] for x in results if x.get("in_sitemap") and x.get("status") != 200],
        "sitemap_noindex": [x["url"] for x in results if x.get("in_sitemap") and "noindex" in (x.get("meta_robots", "") + x.get("x_robots_tag", "")).lower()],
        "orphan_sitemap_urls": [x["url"] for x in results if x.get("in_sitemap") and inbound[normalize(x["url"])] == 0 and normalize(x["url"]) != HOME],
        "plugin_fingerprints": {
            "elementor_pages": sum(bool(x.get("has_elementor")) for x in results),
            "rankmath_pages": sum(bool(x.get("has_rankmath")) for x in results),
            "yoast_pages": sum(bool(x.get("has_yoast")) for x in results),
            "aioseo_pages": sum(bool(x.get("has_aioseo")) for x in results),
            "litespeed_pages": sum(bool(x.get("has_litespeed")) for x in results),
            "contact_form_7_pages": sum(bool(x.get("has_cf7")) for x in results),
            "wpforms_pages": sum(bool(x.get("has_wpforms")) for x in results),
        },
    }
    (OUT / f"crawl-summary-{AUDIT_DATE}.json").write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps({k: summary[k] for k in ("sitemap_url_count", "crawled_url_count", "status_counts", "indexable_count", "plugin_fingerprints")}, indent=2))


if __name__ == "__main__":
    main()
