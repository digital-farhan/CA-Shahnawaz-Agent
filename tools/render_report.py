from __future__ import annotations

import re
from pathlib import Path

import markdown


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "reports" / "Cashahnawaz-Comprehensive-SEO-Audit-2026-08-28.md"
TARGET = ROOT / "reports" / "Cashahnawaz-Comprehensive-SEO-Audit-2026-08-28.html"


def main() -> None:
    source = SOURCE.read_text(encoding="utf-8")
    md = markdown.Markdown(
        extensions=["extra", "toc", "sane_lists"],
        extension_configs={"toc": {"permalink": False}},
    )
    body = md.convert(source)
    toc = md.toc
    html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="Comprehensive SEO, analytics, technical, content, local and conversion audit for cashahnawaz.com - 28 August 2026.">
<title>Comprehensive SEO Audit - Shahnawaz and Associates</title>
<style>
:root {{
  --navy:#0a2740; --teal:#0b8f98; --gold:#f4b942; --ink:#172536;
  --muted:#5b6a79; --line:#dce5eb; --paper:#fff; --wash:#f3f7f9;
  --critical:#bd2c37; --high:#d9642b; --medium:#b5810a;
}}
* {{ box-sizing:border-box; }}
html {{ scroll-behavior:smooth; }}
body {{ margin:0; color:var(--ink); background:var(--wash); font:15px/1.65 Inter,Segoe UI,Arial,sans-serif; }}
a {{ color:#087985; text-decoration-thickness:1px; text-underline-offset:2px; }}
.cover {{ position:relative; overflow:hidden; color:white; background:linear-gradient(135deg,var(--navy) 0%,#0a4358 55%,var(--teal) 100%); padding:70px max(6vw,40px) 56px; }}
.cover:before,.cover:after {{ content:""; position:absolute; border-radius:999px; opacity:.14; border:1px solid white; }}
.cover:before {{ width:430px;height:430px;right:-120px;top:-190px; }}
.cover:after {{ width:230px;height:230px;right:150px;bottom:-160px; }}
.kicker {{ color:#b8f2ed; font-weight:800; letter-spacing:.16em; text-transform:uppercase; font-size:12px; }}
.cover h1 {{ max-width:860px; margin:14px 0 8px; color:white; font-size:clamp(34px,5vw,64px); line-height:1.03; letter-spacing:-.04em; }}
.cover .client {{ font-size:20px; color:#d7f5f2; margin-bottom:26px; }}
.cover .lede {{ max-width:850px; font-size:18px; color:#eefafa; }}
.meta-row {{ display:flex; flex-wrap:wrap; gap:10px; margin:28px 0 0; }}
.pill {{ border:1px solid rgba(255,255,255,.35); background:rgba(255,255,255,.09); border-radius:999px; padding:7px 13px; font-size:13px; }}
.metrics {{ display:grid; grid-template-columns:repeat(4,minmax(140px,1fr)); gap:12px; max-width:1000px; margin-top:34px; }}
.metric {{ padding:17px 18px; background:rgba(255,255,255,.10); border:1px solid rgba(255,255,255,.18); border-radius:14px; backdrop-filter:blur(6px); }}
.metric strong {{ display:block; font-size:25px; line-height:1.1; color:white; }}
.metric span {{ display:block; margin-top:6px; color:#ccebea; font-size:12px; text-transform:uppercase; letter-spacing:.08em; }}
.layout {{ display:grid; grid-template-columns:280px minmax(0,980px); gap:34px; max-width:1340px; margin:0 auto; padding:34px 24px 70px; align-items:start; }}
.sidebar {{ position:sticky; top:18px; max-height:calc(100vh - 36px); overflow:auto; background:white; border:1px solid var(--line); border-radius:15px; padding:20px; box-shadow:0 12px 35px rgba(10,39,64,.08); }}
.sidebar .label {{ color:var(--teal); font-weight:800; text-transform:uppercase; letter-spacing:.12em; font-size:11px; margin-bottom:10px; }}
.sidebar ul {{ list-style:none; margin:0; padding:0; }}
.sidebar li {{ margin:4px 0; }}
.sidebar li li {{ padding-left:12px; }}
.sidebar li li li {{ display:none; }}
.sidebar a {{ display:block; color:#435467; text-decoration:none; padding:5px 7px; border-radius:7px; font-size:12.5px; line-height:1.25; }}
.sidebar a:hover {{ background:#edf7f7; color:#066a73; }}
.content {{ min-width:0; background:var(--paper); border:1px solid var(--line); border-radius:16px; padding:42px 50px 64px; box-shadow:0 12px 35px rgba(10,39,64,.07); }}
.content > h1:first-child,.content > h1:first-child + h2 {{ position:absolute; width:1px; height:1px; overflow:hidden; clip:rect(0 0 0 0); white-space:nowrap; }}
h1,h2,h3,h4 {{ color:var(--navy); line-height:1.22; letter-spacing:-.015em; scroll-margin-top:24px; }}
h2 {{ margin:52px 0 18px; padding-top:8px; font-size:29px; border-top:1px solid var(--line); }}
h2:first-of-type {{ margin-top:12px; border-top:0; }}
h3 {{ margin:32px 0 12px; font-size:21px; }}
h4 {{ margin:22px 0 8px; }}
p {{ margin:10px 0 15px; }}
ul,ol {{ padding-left:23px; }}
li {{ margin:5px 0; }}
blockquote {{ margin:20px 0; padding:16px 20px; border-left:4px solid var(--teal); background:#eef8f8; color:#344b58; }}
hr {{ border:0; height:1px; background:var(--line); margin:34px 0; }}
code {{ background:#eef3f5; color:#9f2340; padding:2px 5px; border-radius:5px; font-size:.9em; overflow-wrap:anywhere; }}
table {{ width:100%; border-collapse:separate; border-spacing:0; margin:18px 0 27px; font-size:13px; border:1px solid var(--line); border-radius:11px; overflow:hidden; }}
thead th {{ background:var(--navy); color:white; font-weight:700; text-align:left; padding:11px 12px; vertical-align:top; }}
tbody td {{ padding:10px 12px; vertical-align:top; border-top:1px solid var(--line); }}
tbody tr:nth-child(even) td {{ background:#f7fafb; }}
tbody tr:hover td {{ background:#eef8f8; }}
.severity {{ display:inline-block; color:white; font-weight:800; font-size:11px; letter-spacing:.08em; border-radius:999px; padding:4px 9px; margin-left:7px; vertical-align:middle; }}
.critical {{ background:var(--critical); }} .high {{ background:var(--high); }} .medium {{ background:var(--medium); }}
.footer {{ text-align:center; padding:26px; color:#71808c; font-size:12px; }}
@media (max-width:980px) {{
  .metrics {{ grid-template-columns:repeat(2,1fr); }}
  .layout {{ display:block; padding:18px 10px 40px; }}
  .sidebar {{ position:relative; top:auto; max-height:none; margin:0 0 14px; }}
  .sidebar .toc > ul {{ columns:2; }}
  .content {{ padding:28px 20px 45px; }}
}}
@media (max-width:600px) {{
  .cover {{ padding:45px 22px 38px; }}
  .metrics {{ grid-template-columns:1fr 1fr; }}
  .metric strong {{ font-size:21px; }}
  .sidebar .toc > ul {{ columns:1; }}
  .content {{ border-radius:12px; }}
  h2 {{ font-size:25px; }}
  table {{ display:block; overflow-x:auto; white-space:normal; }}
}}
@media print {{
  @page {{ size:A4; margin:16mm 13mm; }}
  body {{ background:white; font-size:10.2pt; }}
  .cover {{ min-height:245mm; padding:35mm 18mm; break-after:page; print-color-adjust:exact; -webkit-print-color-adjust:exact; }}
  .metrics {{ grid-template-columns:1fr 1fr; }}
  .layout {{ display:block; max-width:none; padding:0; }}
  .sidebar {{ display:none; }}
  .content {{ border:0; box-shadow:none; padding:0; }}
  h2 {{ break-before:page; margin-top:0; }}
  h2:first-of-type {{ break-before:auto; }}
  h3 {{ break-after:avoid; }}
  table,blockquote {{ break-inside:avoid; }}
  a {{ color:inherit; text-decoration:none; }}
}}
</style>
</head>
<body>
<header class="cover">
  <div class="kicker">Confidential growth audit | 28 August 2026</div>
  <h1>Comprehensive SEO, Analytics &amp; Growth Audit</h1>
  <div class="client">Shahnawaz and Associates | cashahnawaz.com</div>
  <p class="lede">A verified, implementation-ready review of organic visibility, audience quality, technical SEO, content, conversion tracking, mobile experience, local presence and competitive positioning.</p>
  <div class="meta-row"><span class="pill">GSC connected</span><span class="pill">GA4 connected</span><span class="pill">Published GTM inspected</span><span class="pill">175 URLs crawled</span><span class="pill">No live changes made</span></div>
  <div class="metrics">
    <div class="metric"><strong>402,561</strong><span>90-day impressions</span></div>
    <div class="metric"><strong>3,744</strong><span>90-day clicks</span></div>
    <div class="metric"><strong>+83%</strong><span>Last vs first 30-day clicks</span></div>
    <div class="metric"><strong>81.7%</strong><span>Organic share of GA4 sessions</span></div>
  </div>
</header>
<main class="layout">
  <aside class="sidebar"><div class="label">Report contents</div><div class="toc">{toc}</div></aside>
  <article class="content">{body}</article>
</main>
<div class="footer">Prepared from live first-party data and public-site evidence | Audit date 28 August 2026</div>
<script>
document.querySelectorAll('h3').forEach(h => {{
  const t=h.textContent;
  if (/^F-\\d+/.test(t)) {{
    const next=h.nextElementSibling;
    if(next && next.textContent.includes('CRITICAL')) h.insertAdjacentHTML('beforeend','<span class="severity critical">CRITICAL</span>');
    else if(next && next.textContent.includes('HIGH')) h.insertAdjacentHTML('beforeend','<span class="severity high">HIGH</span>');
    else if(next && next.textContent.includes('MEDIUM')) h.insertAdjacentHTML('beforeend','<span class="severity medium">MEDIUM</span>');
  }}
}});
</script>
</body>
</html>"""
    TARGET.write_text(html, encoding="utf-8")
    print(f"Rendered {TARGET} ({TARGET.stat().st_size:,} bytes)")


if __name__ == "__main__":
    main()
