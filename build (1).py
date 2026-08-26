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
 "qr": "/assets/img/qr-get-my-app.webp",
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
          <a class="qr" href="%(app_url)s" title="Open the app">
            <img src="%(qr)s" alt="QR code — scan to open David Wainwright Jr's app" loading="lazy">
          </a>
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
</footer>""" % dict(IMG, app_url=APP_URL, **AGENT)

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
    import build_pages
    build_pages.run(globals())
    print("DONE")
