# WordPress system profile — 28 August 2026

**Access mode:** Public fingerprint only. WordPress Admin was not logged into during this audit, so installed versions and admin-only settings remain unconfirmed.

| Component | Observed value | Confidence / source |
|---|---|---|
| CMS | WordPress | Confirmed by public asset and endpoint fingerprints |
| SEO plugin | Rank Math | High-confidence public fingerprint across 152 HTML pages; version not exposed/confirmed |
| Page builder | Elementor / Elementor forms | Confirmed by rendered classes, assets and form field naming |
| Caching/CDN | Hostinger hCDN + LiteSpeed caching fingerprints | Confirmed in public response headers and page source; admin configuration not inspected |
| Form system | Elementor forms with hCaptcha on sampled money pages | Confirmed in rendered form markup |
| Analytics deployment | GTM-N2LHGRCX; GA4 G-1SFXZJSYYY | Confirmed in public markup and published GTM container |
| Behaviour analytics | Contentsquare/Hotjar-style script deployed through the tag named “Hotjar” | Confirmed in published GTM version 5 |
| Redirect management | Unknown | Requires WordPress Admin/hosting inspection |
| Permalink structure | Clean post-name style for public content | Confirmed from live URLs; admin setting not inspected |
| Staging / rollback | Unknown | Requires WordPress Admin/hosting inspection |
| Admin role available | Not verified in this session | Login details were not supplied in the workspace |

Implementation paths in the audit are therefore written as likely WordPress/Rank Math/Elementor locations and must be confirmed against the installed versions before changing production.

