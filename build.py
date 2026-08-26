# -*- coding: utf-8 -*-
"""Static site generator: David Wainwright Jr — RE/MAX Select (Netlify build)."""
import os, html

ROOT = os.path.join(os.path.dirname(__file__), "site")

IMG = {
 "logo": "/assets/img/d67b83e87866.webp",
 "hero_video": "/assets/img/5e63795c1a0d.mp4",
 "valuation_bg": "https://cdn.chime.me/image/fs/sitebuild/site-cms/site-cms/md-cta-single-column/row/bg-jpeg.webp",
 "work_bg": "/assets/img/1136f6805861.jpg",
 "gsmls": "/assets/img/e007eb4d99e4.webp",
 "b_somerset": "/assets/img/3d6712ed8bcb.webp",
 "b_bergen": "/assets/img/94218a5799f7.webp",
 "b_union": "/assets/img/e4464c6fb9de.webp",
 "b_morris": "/assets/img/73fafb1d39ea.webp",
 "b_passaic": "/assets/img/cab88798f894.webp",
 "b_sussex": "/assets/img/4326737f69fc.webp",
 # Footer credential row. All four are transparent WebP with light artwork, sized
 # to sit directly on the black footer -- no white chip behind them.
 #
 # Deliberately renamed off the old hashed filenames (ef4b897f55ce.webp etc).
 # Those hashes are inherited from the Lofty export and say nothing about what
 # the file is, which made it far too easy to upload a stale copy over a new one.
 # The old files are left in place, unreferenced, rather than deleted.
 "badge1": "/assets/img/badge-remax-select.webp",   # RE/MAX SELECT | Morris Agent Team
 "badge2": "/assets/img/badge-wainwright.webp",     # Wainwright Realty NJ | NY
 "badge3": "/assets/img/badge-nrba-master.webp",    # NRBA NJ Master Broker
 "badge4": "/assets/img/badge-csse.webp",           # Certified Short Sale Expert (CSSE)
}

AGENT = {
 "name": "David Wainwright Jr",
 "brand": "RE/MAX SELECT",
 "phone": "+1 (973) 818-7100",
 "phone_href": "+19738187100",
 "email": "dave@dwainwrightrealty.com",
 "license": "8744778",
 "mls_id": "234919",
 "address": "20 W Main St, Rockaway, NJ 07866, USA",
}

# Where the footer "Get My App" QR points. Swap this one string to repoint the
# QR; regenerate the image with tools/make_qr.py after changing it.
APP_URL = "https://dwainwrightrealty.com/"

HOUSE_SVG = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4">'
 '<path d="M3 11l9-7 9 7"/><path d="M5 10v10h14V10"/><path d="M9 20v-6h6v6"/></svg>')

def nav_link(href, label, active, key, akey):
    cls = ' class="active"' if akey == key else ''
    return '<a href="%s"%s>%s</a>' % (href, cls, label)

def header(akey=""):
    return """<header class="site-header">
  <div class="container header-inner">
    <a class="logo" href="/"><img src="%(logo)s" alt="Wainwright Realty"></a>
    <nav class="main-nav">
      %(home)s
      <span class="has-drop">%(buy)s
        <span class="drop">
          <a href="/listing">Listings</a>
          <a href="/featured-listing">Featured Listings</a>
          <a href="/sold-listing">Sold Listings</a>
          <a href="/calculate-mortgage">Mortgage Calculator</a>
          <a href="/calculate-affordability">Affordability Calculator</a>
        </span>
      </span>
      <span class="has-drop">%(sell)s
        <span class="drop">
          <a href="/sell">Sell My Home</a>
          <a href="/sell">Home Valuation</a>
          <a href="/home-sale-calculator">Home Sale Calculator</a>
        </span>
      </span>
      <span class="has-drop">%(reo)s
        <span class="drop">
          <a href="/reo-services">REO Process &amp; Services</a>
          <a href="/reo-services/bpo-services">BPO Services</a>
          <a href="/reo-services/initial-assignment">Initial Assignment</a>
          <a href="/reo-services/occupied-properties">Occupied Properties</a>
          <a href="/reo-services/property-preservation-services">Property Preservation</a>
          <a href="/reo-services/preparing-assets-for-listing">Preparing Assets for Listing</a>
          <a href="/reo-services/marketing-your-assets">Marketing Your Assets</a>
          <a href="/reo-services/usda-and-rural">USDA &amp; Rural</a>
        </span>
      </span>
      %(commercial)s
      %(blog)s
    </nav>
    <div class="header-cta">
      <a class="reg" href="/contact">Register</a>
      <a href="/contact">Sign In</a>
    </div>
    <button class="nav-toggle" aria-label="Menu">&#9776;</button>
  </div>
</header>""" % {
      "logo": IMG["logo"],
      "home": nav_link("/", "Real Estate Services in NJ &amp; NY", akey, "home", akey),
      "buy": nav_link("/listing", "Buy", akey, "buy", akey),
      "sell": nav_link("/sell", "Sell", akey, "sell", akey),
      "reo": nav_link("/reo-services", "REO Services", akey, "reo", akey),
      "commercial": nav_link("/commercial", "Commercial", akey, "commercial", akey),
      "blog": nav_link("/blog", "Market Insights", akey, "blog", akey),
    }

def footer():
    return """<footer class="site-footer">
  <div class="container">
    <div class="footer-top">
      <div class="f-agent">
        <div class="brand">%(brand)s</div>
        <h3>%(name)s</h3>
        <p><a href="tel:%(phone_href)s">%(phone)s</a></p>
        <p><a href="mailto:%(email)s">%(email)s</a></p>
        <p>License ID: %(license)s &nbsp;&middot;&nbsp; MLS ID: %(mls_id)s</p>
        <p>%(address)s</p>
        <div class="f-badges">
          <img src="%(badge1)s" alt="RE/MAX Select — Morris Agent Team" loading="lazy">
          <img src="%(badge2)s" alt="Wainwright Realty — New Jersey and New York" loading="lazy">
          <img src="%(badge3)s" alt="NRBA National REO Brokers Association — NJ Master Broker" loading="lazy">
          <img src="%(badge4)s" alt="Certified Short Sale Expert (CSSE)" loading="lazy">
        </div>
        <div class="f-qr">
          <div class="f-qr-label">Get My App</div>
          <a class="qr" href="%(app_url)s" title="Open the app">%(qr_svg)s</a>
          <div class="f-qr-hint">Scan with your phone</div>
        </div>
      </div>
      <div class="f-nav">
        <a href="/">Real Estate Services in NJ &amp; NY</a>
        <a href="/listing">Buy</a>
        <a href="/sell">Sell</a>
        <a href="/reo-services">REO Services</a>
        <a href="/commercial">Commercial</a>
        <a href="/blog">Market Insights</a>
        <a href="/listing">Listings</a>
        <a href="/featured-listing">Featured Listings</a>
        <a href="/sold-listing">Sold Listings</a>
        <a href="/calculate-mortgage">Mortgage Calculator</a>
        <a href="/calculate-affordability">Affordability Calculator</a>
        <a href="/contact">Contact</a>
      </div>
    </div>
    <div class="f-social">
      <a href="#" aria-label="Facebook"><svg viewBox="0 0 24 24"><path d="M22 12a10 10 0 1 0-11.6 9.9v-7H7.9V12h2.5V9.8c0-2.5 1.5-3.9 3.8-3.9 1.1 0 2.2.2 2.2.2v2.4h-1.2c-1.2 0-1.6.8-1.6 1.6V12h2.7l-.4 2.9h-2.3v7A10 10 0 0 0 22 12z"/></svg></a>
      <a href="#" aria-label="LinkedIn"><svg viewBox="0 0 24 24"><path d="M4.98 3.5A2.5 2.5 0 1 1 5 8.5a2.5 2.5 0 0 1 0-5zM3 9h4v12H3zM9 9h3.8v1.7h.1c.5-1 1.8-2 3.7-2 4 0 4.7 2.6 4.7 6V21h-4v-5.3c0-1.3 0-2.9-1.8-2.9s-2 1.4-2 2.8V21H9z"/></svg></a>
      <a href="#" aria-label="X"><svg viewBox="0 0 24 24"><path d="M18 2h3l-7 8 8 12h-6l-5-7-5 7H0l8-9L0 2h6l4 6zm-1 18h2L7 4H5z"/></svg></a>
      <a href="#" aria-label="Instagram"><svg viewBox="0 0 24 24"><path d="M12 2.2c3.2 0 3.6 0 4.9.1 3.3.1 4.8 1.7 4.9 4.9.1 1.3.1 1.6.1 4.8s0 3.6-.1 4.9c-.1 3.2-1.6 4.8-4.9 4.9-1.3.1-1.6.1-4.9.1s-3.6 0-4.9-.1c-3.3-.1-4.8-1.7-4.9-4.9C2.1 15.6 2.1 15.2 2.1 12s0-3.6.1-4.9C2.3 3.9 3.8 2.3 7.1 2.2 8.4 2.2 8.8 2.2 12 2.2zm0 3a6.8 6.8 0 1 0 0 13.6A6.8 6.8 0 0 0 12 5.2zm0 11.2a4.4 4.4 0 1 1 0-8.8 4.4 4.4 0 0 1 0 8.8zM18.4 5a1.6 1.6 0 1 0 0 3.2 1.6 1.6 0 0 0 0-3.2z"/></svg></a>
      <a href="#" aria-label="YouTube"><svg viewBox="0 0 24 24"><path d="M23 12s0-3.2-.4-4.7a2.5 2.5 0 0 0-1.8-1.8C19.3 5 12 5 12 5s-7.3 0-8.8.5A2.5 2.5 0 0 0 1.4 7.3C1 8.8 1 12 1 12s0 3.2.4 4.7a2.5 2.5 0 0 0 1.8 1.8C4.7 19 12 19 12 19s7.3 0 8.8-.5a2.5 2.5 0 0 0 1.8-1.8C23 15.2 23 12 23 12zM9.8 15.3V8.7l5.7 3.3z"/></svg></a>
      <a href="#" aria-label="Google"><svg viewBox="0 0 24 24"><path d="M21.8 12.2c0-.7-.1-1.4-.2-2H12v3.8h5.5a4.7 4.7 0 0 1-2 3.1v2.6h3.2c1.9-1.7 3.1-4.3 3.1-7.5zM12 22c2.7 0 4.9-.9 6.6-2.4l-3.2-2.5c-.9.6-2 .9-3.4.9-2.6 0-4.8-1.7-5.6-4.1H3.1v2.6A10 10 0 0 0 12 22zM6.4 13.9a6 6 0 0 1 0-3.8V7.5H3.1a10 10 0 0 0 0 9zM12 6c1.5 0 2.8.5 3.8 1.5l2.8-2.8A10 10 0 0 0 3.1 7.5l3.3 2.6C7.2 7.7 9.4 6 12 6z"/></svg></a>
    </div>
    <div class="f-legal">
      <img src="%(gsmls)s" alt="Garden State MLS">
      <p>The data relating to real estate for sale on this website comes in part from the IDX Program of Garden State Multiple Listing Service, L.L.C. Real estate listings held by other brokerage firms are marked as IDX listing. The dissemination of listings on this website does not constitute the consent required by N.J.A.C. 11:5.6.1 (n) for the advertisement of listings exclusively for sale by another broker. Any such consent must be obtained in writing from the listing broker.</p>
      <p>This information is being provided for Consumers' personal, non-commercial use and may not be used for any purpose other than to identify prospective properties Consumers may be interested in purchasing. IDX information is provided exclusively for consumers' personal, non-commercial use, and data is deemed reliable but is not guaranteed accurate by the MLS.</p>
    </div>
  </div>
  <div class="f-bottom">
    <div class="container">
      &copy; 2026 %(name)s &middot; %(brand)s. All Rights Reserved. &nbsp;|&nbsp;
      <a href="/contact">Terms of Service &amp; Privacy Policy</a> &nbsp;|&nbsp;
      <a href="/blog">Property Listings</a> &nbsp;|&nbsp;
      <a href="/">Sitemap</a>
    </div>
  </div>
</footer>""" % dict(IMG, app_url=APP_URL, qr_svg=QR_SVG, **AGENT)

# ---------------------------------------------------------------------------
# Embedded footer assets
#
# The badge images live here as base64 and are written to site/assets/img at
# build time. They are embedded rather than committed as binaries because
# uploading .webp files through the GitHub web UI proved unreliable -- a stale
# or mangled copy would silently replace a good one and the failure only showed
# up as a 404 on the live site. A text file cannot fail that way, and Netlify
# runs this script on every deploy, so the images are recreated from source of
# truth each time.
#
# The QR is inline SVG instead: it is a third the size of the raster version,
# stays crisp at any display size, and needs no file at all. Verified to decode
# at 120px, which is the size the footer renders it.
# ---------------------------------------------------------------------------
EMBEDDED_IMAGES = {
 "badge-remax-select.webp": (
  "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"
 ),
 "badge-wainwright.webp": (
  "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"
 ),
 "badge-nrba-master.webp": (
  "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"
 ),
 "badge-csse.webp": (
  "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"
  "Y/Y+v7uoEV+U1AAAAA=="
 ),
}

QR_SVG = (
    '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 33 33" shape-rendering="crispEdges" role="img" aria-label="QR code linking to dwainwrightrealty.com"><rect width="33" height="33" fill="#e1c281"/><path d="M2 2h7v1h-7zM11 2h1v1h-1zM13 2h1v1h-1zM17 2h2v1h-2zM20 2h1v1h-1zM24 2h7v1h-7zM2 3h1v1h-1zM8 3h1v1h-1zM10 3h1v1h-1zM12 3h1v1h-1zM14 3h3v1h-3zM18 3h1v1h-1zM22 3h1v1h-1zM24 3h1v1h-1zM30 3h1v1h-1zM2 4h1v1h-1zM4 4h3v1h-3zM8 4h1v1h-1zM10 4h1v1h-1zM12 4h2v1h-2zM15 4h1v1h-1zM17 4h1v1h-1zM20 4h1v1h-1zM24 4h1v1h-1zM26 4h3v1h-3zM30 4h1v1h-1zM2 5h1v1h-1zM4 5h3v1h-3zM8 5h1v1h-1zM10 5h3v1h-3zM14 5h1v1h-1zM18 5h2v1h-2zM22 5h1v1h-1zM24 5h1v1h-1zM26 5h3v1h-3zM30 5h1v1h-1zM2 6h1v1h-1zM4 6h3v1h-3zM8 6h1v1h-1zM11 6h4v1h-4zM17 6h2v1h-2zM21 6h2v1h-2zM24 6h1v1h-1zM26 6h3v1h-3zM30 6h1v1h-1zM2 7h1v1h-1zM8 7h1v1h-1zM11 7h1v1h-1zM13 7h1v1h-1zM17 7h1v1h-1zM22 7h1v1h-1zM24 7h1v1h-1zM30 7h1v1h-1zM2 8h7v1h-7zM10 8h1v1h-1zM12 8h1v1h-1zM14 8h1v1h-1zM16 8h1v1h-1zM18 8h1v1h-1zM20 8h1v1h-1zM22 8h1v1h-1zM24 8h7v1h-7zM10 9h1v1h-1zM12 9h1v1h-1zM14 9h1v1h-1zM16 9h3v1h-3zM20 9h1v1h-1zM22 9h1v1h-1zM2 10h1v1h-1zM8 10h1v1h-1zM10 10h4v1h-4zM18 10h2v1h-2zM23 10h2v1h-2zM27 10h3v1h-3zM6 11h1v1h-1zM10 11h2v1h-2zM14 11h2v1h-2zM18 11h2v1h-2zM21 11h1v1h-1zM25 11h2v1h-2zM28 11h2v1h-2zM2 12h1v1h-1zM4 12h1v1h-1zM6 12h5v1h-5zM13 12h6v1h-6zM20 12h1v1h-1zM24 12h3v1h-3zM3 13h1v1h-1zM5 13h1v1h-1zM7 13h1v1h-1zM13 13h3v1h-3zM21 13h1v1h-1zM24 13h1v1h-1zM27 13h1v1h-1zM2 14h2v1h-2zM5 14h1v1h-1zM7 14h2v1h-2zM11 14h1v1h-1zM13 14h1v1h-1zM15 14h1v1h-1zM17 14h2v1h-2zM20 14h2v1h-2zM24 14h2v1h-2zM30 14h1v1h-1zM3 15h2v1h-2zM6 15h2v1h-2zM12 15h1v1h-1zM14 15h1v1h-1zM18 15h9v1h-9zM29 15h2v1h-2zM5 16h2v1h-2zM8 16h1v1h-1zM10 16h2v1h-2zM19 16h1v1h-1zM25 16h4v1h-4zM3 17h4v1h-4zM10 17h1v1h-1zM12 17h3v1h-3zM17 17h1v1h-1zM20 17h1v1h-1zM23 17h1v1h-1zM26 17h1v1h-1zM28 17h1v1h-1zM30 17h1v1h-1zM3 18h1v1h-1zM5 18h2v1h-2zM8 18h1v1h-1zM11 18h4v1h-4zM18 18h2v1h-2zM22 18h1v1h-1zM27 18h2v1h-2zM2 19h1v1h-1zM4 19h1v1h-1zM6 19h1v1h-1zM13 19h1v1h-1zM15 19h2v1h-2zM20 19h7v1h-7zM28 19h3v1h-3zM2 20h5v1h-5zM8 20h2v1h-2zM11 20h1v1h-1zM13 20h1v1h-1zM17 20h1v1h-1zM20 20h5v1h-5zM27 20h1v1h-1zM30 20h1v1h-1zM2 21h1v1h-1zM4 21h1v1h-1zM9 21h7v1h-7zM24 21h3v1h-3zM2 22h1v1h-1zM5 22h2v1h-2zM8 22h1v1h-1zM12 22h1v1h-1zM14 22h1v1h-1zM16 22h2v1h-2zM19 22h1v1h-1zM21 22h6v1h-6zM28 22h3v1h-3zM10 23h2v1h-2zM14 23h1v1h-1zM16 23h1v1h-1zM19 23h2v1h-2zM22 23h1v1h-1zM26 23h2v1h-2zM2 24h7v1h-7zM11 24h1v1h-1zM13 24h1v1h-1zM19 24h1v1h-1zM21 24h2v1h-2zM24 24h1v1h-1zM26 24h3v1h-3zM2 25h1v1h-1zM8 25h1v1h-1zM11 25h1v1h-1zM13 25h1v1h-1zM16 25h3v1h-3zM21 25h2v1h-2zM26 25h1v1h-1zM30 25h1v1h-1zM2 26h1v1h-1zM4 26h3v1h-3zM8 26h1v1h-1zM11 26h1v1h-1zM14 26h3v1h-3zM18 26h1v1h-1zM21 26h7v1h-7zM2 27h1v1h-1zM4 27h3v1h-3zM8 27h1v1h-1zM11 27h4v1h-4zM16 27h1v1h-1zM19 27h5v1h-5zM25 27h1v1h-1zM27 27h3v1h-3zM2 28h1v1h-1zM4 28h3v1h-3zM8 28h1v1h-1zM12 28h1v1h-1zM14 28h2v1h-2zM17 28h2v1h-2zM21 28h1v1h-1zM23 28h7v1h-7zM2 29h1v1h-1zM8 29h1v1h-1zM12 29h2v1h-2zM16 29h2v1h-2zM26 29h3v1h-3zM30 29h1v1h-1zM2 30h7v1h-7zM10 30h5v1h-5zM19 30h3v1h-3zM25 30h2v1h-2zM28 30h1v1h-1z" fill="#000"/></svg>'
)


def write_embedded_images():
    """Materialise EMBEDDED_IMAGES into site/assets/img/. Idempotent."""
    import base64 as _b64
    outdir = os.path.join(ROOT, "assets", "img")
    os.makedirs(outdir, exist_ok=True)
    for name, data in EMBEDDED_IMAGES.items():
        raw = _b64.b64decode(data)
        path = os.path.join(outdir, name)
        if os.path.exists(path) and open(path, "rb").read() == raw:
            continue
        with open(path, "wb") as fh:
            fh.write(raw)
        print("wrote asset", name, len(raw), "bytes")


# Footer credential-row + QR styling, emitted inline after the stylesheet so it
# wins the cascade regardless of what styles.css currently contains.
#
# These rules used to live in styles.css. They are inlined here on purpose: the
# generated pages are rebuilt by Netlify on every deploy, so keeping the footer's
# presentation next to the footer's markup means the two can never drift apart
# again. If styles.css is ever brought back in sync, this block is harmless --
# it simply restates the same declarations.
FOOTER_CSS = """<style>
.f-badges{display:flex;gap:26px;flex-wrap:wrap;align-items:center;margin-top:22px;}
.f-badges img{height:34px;width:auto;max-width:190px;object-fit:contain;
  background:none;padding:0;border-radius:0;opacity:.92;transition:opacity .2s ease;}
.f-badges img:hover{opacity:1;}
@media(max-width:760px){.f-badges{gap:18px;}.f-badges img{height:28px;max-width:150px;}}
.f-qr{margin-top:26px;}
.f-qr-label{font-size:13px;color:var(--gold,#e1c281);letter-spacing:.6px;
  text-transform:uppercase;margin-bottom:8px;}
.f-qr .qr{width:120px;height:120px;border-radius:8px;overflow:hidden;display:block;
  line-height:0;background:none;}
.f-qr .qr img{width:100%;height:100%;display:block;}
.f-qr-hint{font-size:12px;color:#8f8f8f;margin-top:7px;}
</style>"""


def page(path, title, description, body, akey="", extra_head=""):
    doc = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%(title)s</title>
<meta name="description" content="%(desc)s">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Raleway:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/css/styles.css?v=8">
%(footer_css)s
%(extra)s
</head>
<body>
%(header)s
<main>
%(body)s
</main>
%(footer)s
<script src="/assets/js/main.js?v=7"></script>
</body>
</html>""" % {
        "title": html.escape(title), "desc": html.escape(description),
        "extra": extra_head, "footer_css": FOOTER_CSS,
        "header": header(akey), "body": body, "footer": footer(),
    }
    outdir = os.path.join(ROOT, path)
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, "index.html"), "w", encoding="utf-8") as f:
        f.write(doc)
    print("wrote", path or "(home)")

# ---------- reusable components ----------
def listing_card(status, price, beds, baths, size, size_label, addr, broker, tags, count):
    return """<article class="card">
  <div class="photo">%(svg)s
    <span class="status">%(status)s</span>
    <span class="count">&#128247; %(count)s</span>
  </div>
  <div class="facts"><span><b>%(beds)s</b> Beds</span><span><b>%(baths)s</b> Baths</span><span><b>%(size)s</b> %(size_label)s</span></div>
  <div class="meta">
    <div class="price">%(price)s</div>
    <div class="addr">%(addr)s</div>
    <div class="brokerage">Listed by %(broker)s</div>
    <div class="tags">%(tags)s</div>
  </div>
</article>""" % {"svg": HOUSE_SVG, "status": status, "price": price, "beds": beds,
    "baths": baths, "size": size, "size_label": size_label, "addr": addr,
    "broker": broker, "tags": tags, "count": count}

def search_widget():
    return """<form class="search-widget" onsubmit="window.location.href='/listing';return false;">
  <div class="search-tabs">
    <button type="button" class="active" onclick="window.location.href='/listing'">Buy</button>
    <button type="button" onclick="window.location.href='/sell'">Sell</button>
    <button type="button" onclick="window.location.href='/sell'">Valuation</button>
  </div>
  <div class="search-body">
    <input type="text" placeholder="Search by address, city, or ZIP" aria-label="Search listings">
    <button class="btn btn-gold" type="submit">Search</button>
  </div>
</form>"""

RESIDENTIAL_CARDS = (
    listing_card("Coming Soon", "$989,000", "2", "2", "1,000", "SqFt",
        "227 4th St #402, Jersey City, NJ 07302", "WEICHERT REALTORS", "Condo", "32") +
    listing_card("Open Sat 12PM-3PM", "$889,900", "5", "3", "2,613", "Sqft Lot",
        "378 Cator Ave, Jersey City, NJ 07305", "PROVIDENT LEGACY REALTORS", "Multi-Family, Commercial", "40") +
    listing_card("Open Thu 5PM-7PM", "$849,000", "4", "3", "1,814", "SqFt",
        "31 Surrey Dr, Wayne Twp., NJ 07470", "HOWARD HANNA RAND REALTY", "Single Family", "37")
)
COMMERCIAL_CARDS = (
    listing_card("Open Sat 12PM-3PM", "$889,900", "5", "3", "2,613", "Sqft Lot",
        "378 Cator Ave, Jersey City, NJ 07305", "PROVIDENT LEGACY REALTORS", "Multi-Family, Commercial", "40") +
    listing_card("Open Sun 12PM-2PM", "$699,999", "11", "5", "3,049", "Sqft Lot",
        "304 Ridgewood Ave, Newark City, NJ 07112", "REDFIN CORPORATION", "Multi-Family, Commercial", "3D") +
    listing_card("Coming Soon", "$699,900", "5", "2", "2,266", "SqFt",
        "948 Van Houten Ave, Clifton City, NJ 07013", "KELLER WILLIAMS PROSPERITY REALTY", "Multi-Family, Commercial", "37")
)

PLACEHOLDER = ('<div class="placeholder-note"><strong>Live listings placeholder.</strong> '
  'These example cards show the original layout. Connect an IDX/MLS feed (e.g. GSMLS, '
  'Monmouth-Ocean, or an IDX provider that supports Netlify) to display live results here.</div>')

# ================= build pages below (defined in build_pages.py section) =================
if __name__ == "__main__":
    write_embedded_images()
    import build_pages
    build_pages.run(globals())
    print("DONE")
