from __future__ import annotations

import json
import statistics
from datetime import date
from pathlib import Path
from typing import Any

from playwright.sync_api import sync_playwright


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "data" / "performance"
SHOTS = OUT / "screenshots"
AUDIT_DATE = date(2026, 8, 28)
BASE = "https://cashahnawaz.com"
URLS = {
    "home": f"{BASE}/",
    "accounting": f"{BASE}/accounting-services/",
    "gst-registration": f"{BASE}/gst-registration-online/",
    "gst-return": f"{BASE}/gst-return-filing/",
    "itr-mumbai": f"{BASE}/income-tax-return-filing-in-mumbai/",
    "nri-guide": f"{BASE}/itr-filing-for-nri-guide-for-non-resident-taxation/",
    "audit": f"{BASE}/audit-services/",
    "company-registration": f"{BASE}/private-limited-company-registration/",
    "contact": f"{BASE}/contact-us/",
}


VITALS_INIT = r"""
window.__auditVitals = {lcp: 0, lcpElement: '', cls: 0, longTaskMs: 0, longTaskCount: 0};
try {
  new PerformanceObserver(list => {
    const entries = list.getEntries();
    const last = entries[entries.length - 1];
    if (last) {
      window.__auditVitals.lcp = last.startTime;
      window.__auditVitals.lcpElement = last.element ? (last.element.tagName + '#' + (last.element.id || '') + '.' + (last.element.className || '')).slice(0,250) : '';
    }
  }).observe({type: 'largest-contentful-paint', buffered: true});
} catch(e) {}
try {
  new PerformanceObserver(list => {
    for (const entry of list.getEntries()) if (!entry.hadRecentInput) window.__auditVitals.cls += entry.value;
  }).observe({type: 'layout-shift', buffered: true});
} catch(e) {}
try {
  new PerformanceObserver(list => {
    for (const entry of list.getEntries()) {
      window.__auditVitals.longTaskMs += entry.duration;
      window.__auditVitals.longTaskCount += 1;
    }
  }).observe({type: 'longtask', buffered: true});
} catch(e) {}
"""


def median(values: list[float]) -> float:
    return round(statistics.median(values), 2) if values else 0


def audit_once(browser: Any, slug: str, url: str, device: str, run: int, screenshot: bool) -> dict[str, Any]:
    if device == "mobile":
        context = browser.new_context(
            viewport={"width": 390, "height": 844},
            device_scale_factor=2,
            is_mobile=True,
            has_touch=True,
            user_agent="Mozilla/5.0 (Linux; Android 13; Pixel 7) AppleWebKit/537.36 Chrome/151 Mobile Safari/537.36",
        )
    else:
        context = browser.new_context(viewport={"width": 1440, "height": 900}, device_scale_factor=1)
    page = context.new_page()
    page.set_default_timeout(60_000)
    page.add_init_script(VITALS_INIT)
    client = context.new_cdp_session(page)
    client.send("Network.enable")
    client.send("Emulation.setCPUThrottlingRate", {"rate": 4 if device == "mobile" else 1})
    if device == "mobile":
        client.send("Network.emulateNetworkConditions", {
            "offline": False,
            "latency": 150,
            "downloadThroughput": 1_600_000 / 8,
            "uploadThroughput": 750_000 / 8,
            "connectionType": "cellular4g",
        })
    requests: list[dict[str, Any]] = []

    def on_response(response: Any) -> None:
        try:
            headers = response.headers
            requests.append({
                "url": response.url,
                "status": response.status,
                "type": response.request.resource_type,
                "content_length": int(headers.get("content-length", "0") or 0),
                "cache_control": headers.get("cache-control", ""),
            })
        except Exception:
            pass

    page.on("response", on_response)
    error = ""
    response_status: int | None = None
    try:
        response = page.goto(url, wait_until="domcontentloaded", timeout=90_000)
        response_status = response.status if response else None
        page.wait_for_timeout(7_000 if device == "mobile" else 5_000)
    except Exception as exc:
        error = str(exc)
    screenshot_error = ""
    if screenshot and not error:
        try:
            shot_path = SHOTS / f"{slug}-{device}-{AUDIT_DATE}.png"
            if not shot_path.exists():
                page.screenshot(path=str(shot_path), full_page=False, timeout=10_000)
        except Exception as exc:
            screenshot_error = str(exc)
    metrics_script = r"""
() => {
  const nav = performance.getEntriesByType('navigation')[0] || {};
  const resources = performance.getEntriesByType('resource') || [];
  const anchors = [...document.querySelectorAll('a')];
  const buttons = [...document.querySelectorAll('button, input[type=submit], input[type=button]')];
  const forms = [...document.querySelectorAll('form')];
  const visible = el => { const r = el.getBoundingClientRect(); return r.width > 0 && r.height > 0 && getComputedStyle(el).visibility !== 'hidden'; };
  const aboveFold = el => { const r = el.getBoundingClientRect(); return visible(el) && r.top < innerHeight && r.bottom > 0; };
  const fieldDetails = forms.map((form, i) => ({
    index: i,
    action: form.action || '',
    method: form.method || '',
    fields: [...form.querySelectorAll('input,select,textarea')].map(x => ({name:x.name||'',type:x.type||x.tagName.toLowerCase(),required:!!x.required,placeholder:x.placeholder||''})),
    submits: [...form.querySelectorAll('button,input[type=submit]')].map(x => (x.innerText || x.value || '').trim()).filter(Boolean),
  }));
  return {
    vitals: window.__auditVitals || {},
    navigation: {
      ttfb: (nav.responseStart || 0) - (nav.requestStart || 0),
      domContentLoaded: nav.domContentLoadedEventEnd || 0,
      load: nav.loadEventEnd || 0,
      transferSize: nav.transferSize || 0,
      encodedBodySize: nav.encodedBodySize || 0,
      decodedBodySize: nav.decodedBodySize || 0,
    },
    resourceCount: resources.length,
    resourceTransferSize: resources.reduce((n, x) => n + (x.transferSize || 0), 0),
    resourceEncodedSize: resources.reduce((n, x) => n + (x.encodedBodySize || 0), 0),
    jsTransferSize: resources.filter(x => x.initiatorType === 'script').reduce((n, x) => n + (x.transferSize || 0), 0),
    cssTransferSize: resources.filter(x => x.initiatorType === 'css' || /\.css(?:\?|$)/.test(x.name)).reduce((n, x) => n + (x.transferSize || 0), 0),
    imageTransferSize: resources.filter(x => x.initiatorType === 'img').reduce((n, x) => n + (x.transferSize || 0), 0),
    domNodes: document.querySelectorAll('*').length,
    headings: [...document.querySelectorAll('h1,h2')].map(x => ({tag:x.tagName,text:(x.innerText||'').trim().slice(0,200)})),
    forms: fieldDetails,
    telLinks: anchors.filter(x => (x.href||'').startsWith('tel:')).map(x => ({href:x.href,text:(x.innerText||'').trim(),aboveFold:aboveFold(x)})),
    whatsappLinks: anchors.filter(x => /wa\.me|whatsapp/i.test(x.href||'')).map(x => ({href:x.href,text:(x.innerText||'').trim(),aboveFold:aboveFold(x)})),
    ctasAboveFold: [...anchors, ...buttons].filter(aboveFold).map(x => ({tag:x.tagName,text:(x.innerText||x.value||'').trim().slice(0,100),href:x.href||''})).filter(x => x.text || x.href).slice(0,50),
    allButtons: buttons.map(x => (x.innerText || x.value || '').trim()).filter(Boolean),
    bodyTextSample: (document.body.innerText || '').replace(/\s+/g,' ').slice(0,2500),
  };
}
"""
    metrics = {}
    if not error:
        for _ in range(3):
            try:
                page.wait_for_load_state("domcontentloaded", timeout=30_000)
                page.wait_for_timeout(1_000)
                metrics = page.evaluate(metrics_script)
                break
            except Exception as exc:
                screenshot_error = (screenshot_error + "; " if screenshot_error else "") + f"Metrics retry: {exc}"
    result = {
        "slug": slug,
        "url": url,
        "device": device,
        "run": run,
        "status": response_status,
        "error": error,
        "screenshotError": screenshot_error,
        "metrics": metrics,
        "responseInventory": requests,
    }
    context.close()
    return result


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    SHOTS.mkdir(parents=True, exist_ok=True)
    raw: list[dict[str, Any]] = []
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        for slug, url in URLS.items():
            for run in (1, 2):
                raw.append(audit_once(browser, slug, url, "mobile", run, screenshot=run == 1))
                (OUT / f"browser-audit-partial-{AUDIT_DATE}.json").write_text(json.dumps(raw, indent=2, ensure_ascii=False), encoding="utf-8")
        for slug in ("home", "accounting", "gst-return", "itr-mumbai", "contact"):
            raw.append(audit_once(browser, slug, URLS[slug], "desktop", 1, screenshot=True))
            (OUT / f"browser-audit-partial-{AUDIT_DATE}.json").write_text(json.dumps(raw, indent=2, ensure_ascii=False), encoding="utf-8")
        browser.close()
    (OUT / f"browser-audit-raw-{AUDIT_DATE}.json").write_text(json.dumps(raw, indent=2, ensure_ascii=False), encoding="utf-8")

    summary: list[dict[str, Any]] = []
    groups: dict[tuple[str, str], list[dict[str, Any]]] = {}
    for row in raw:
        groups.setdefault((row["slug"], row["device"]), []).append(row)
    for (slug, device), rows in groups.items():
        successful = [x for x in rows if not x["error"]]
        def vals(path: tuple[str, ...]) -> list[float]:
            output = []
            for row in successful:
                value: Any = row["metrics"]
                for key in path:
                    value = value.get(key, {}) if isinstance(value, dict) else {}
                if isinstance(value, (int, float)):
                    output.append(float(value))
            return output
        example = successful[0]["metrics"] if successful else {}
        summary.append({
            "slug": slug,
            "url": URLS[slug],
            "device": device,
            "runs": len(successful),
            "lcp_ms_median": median(vals(("vitals", "lcp"))),
            "cls_median": median(vals(("vitals", "cls"))),
            "ttfb_ms_median": median(vals(("navigation", "ttfb"))),
            "dcl_ms_median": median(vals(("navigation", "domContentLoaded"))),
            "load_ms_median": median(vals(("navigation", "load"))),
            "long_task_ms_median": median(vals(("vitals", "longTaskMs"))),
            "resource_count_median": median(vals(("resourceCount",))),
            "resource_transfer_kb_median": round(median(vals(("resourceTransferSize",))) / 1024, 1),
            "js_transfer_kb_median": round(median(vals(("jsTransferSize",))) / 1024, 1),
            "image_transfer_kb_median": round(median(vals(("imageTransferSize",))) / 1024, 1),
            "dom_nodes_median": median(vals(("domNodes",))),
            "form_count": len(example.get("forms", [])),
            "tel_link_count": len(example.get("telLinks", [])),
            "whatsapp_link_count": len(example.get("whatsappLinks", [])),
            "lcp_element": example.get("vitals", {}).get("lcpElement", ""),
            "notes": "LAB: Chromium; mobile uses 4x CPU slowdown and approximately 1.6 Mbps/150 ms network. INP requires real-user field data and is not inferred.",
        })
    (OUT / f"browser-audit-summary-{AUDIT_DATE}.json").write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
