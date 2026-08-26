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
          <img class="badge-wordmark" src="%(badge4)s" alt="Certified Short Sale Expert (CSSE)" loading="lazy">
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
  "ry/eeh96qAAAAA=="
 ),
 "badge-wainwright.webp": (
  "UklGRmZEAABXRUJQVlA4WAoAAAAQAAAABAEAXwAAQUxQSOgfAAAB/yckSPD/eGtEpO4TEBpJciRl3fvP5E94jfYYRPR/AmCAsvn9"
  "LK9Udv5MdYcnO3n12nxoBbzS3hB4+obXq9crlKNjwA7bVutUX/IS1ZcFc56oqOU1lmZ1mM251dp007mOu9ZN3dHTqd5CsExfByAQ"
  "3rD9Xyen/b/r+Xq93++RdYm7EsMJRIoluBRNKFKC9NNAS3H4FK2hNdylgkPLB3dSARJIghSHEBeyG1ufmbe8njdmdjYpfJfvzYiY"
  "AP77TSAUxxGlJZ1j+D/DmashsEQx3wlFShhjtooYXJ7SBlTBSFCx+8UbO674UrZ8ARhQ7f15FhU0lfJlK4iXokC3nmgMpJBRTzQX"
  "WlaqffEKIBAi1/sr2/RArAXwp1a52FjzyXLAYrPWjnhglQJ8/ptW+epzwILT7wrWk7LEBoEFtvvliKQjSNub/lgiSAWZYOislUOB"
  "9vWeveM6IECF3ruBYOdhOMHNPm4KYEsYz3qeAMycpTvsZSk+5FjhnVUABoKrxkR99wf45+2weDngoeC0NxZA3dXHUvAkbG5+qB7S"
  "Jazv+b4FBj3dlDhK73Kj5y79cxEeXv+EA26tBVrbfa64B0QQUXrlaWh84CCKVZsvm5kJ8Dzfp+Q+p51y6QYFNr7SprtNrgOOnKM/"
  "/vGxFZQc/LP6aNy+AE8/aeNXmij2bS9MwbXVklggabzkqQua8SJHycpTj3JRDar6z+2rqi65BiBXiDK6+qf/LBFUxJxygwVa1bSe"
  "838lLOp6XcV5IRYrSVhTMTRtJXSww74mJ3V7VgEd9//+htOAnU6w8b6TKXn3h3bT3/MUTzzZi/eaAvDYv+MsXz8ZgXgkrtflG4pd"
  "BJtCR6YTjr5UI3yPxLJksu9XAIFJ+NUlkFi0I8X7c/+DH0FKEi6/EpyJ40KGj+a+i5+Aaq+re3Vx+3pl9CESH+BT8uGvvDUWMEEA"
  "MOXQ2M4aR3Hn/V+brx6j5JRDEzl6EsWFe9eapY8CniF2vTIxQe3Q1ez/K58I1Xya5Q+8SsqIUFLwIrI3/IjQWtE44OUzV5LKgR+R"
  "+sOZhNYKUcDrZy4llaOXLh6M/3lLvLcPPi+9GqXtxnegQBBYAWOFENhzqp/T/qc3AOsf67ILnqLkvtNduxlwal+g+bEO+86TQAqN"
  "Xa/LwugzADqR8Ml7KbYo5YpBHcCwu/ZyYbUFHj6vHemi9OA7Zrqw2gJPnNOCdNF79mxcClziU7zoIcvrlDQ4KcdYXFLE9we6MWcH"
  "wFcvYf/+ejccPsiNPCcNLH9B7dMvA6lYe0VxPuV3Yyx0tvvmlXvBeEVJRM+tAJrATrdv51wfAW7+pVo/bgspnnT7ROcaDXDH5Sq5"
  "HL1f60sStnsZVDROSANL/pw3HwCOrW5FhRhIHVTppv8U4LO3Yj/ddfPHJTL7V7kpZwN88rZE9y3Cs70bIY7yVA5tVoyKZ4mbhM9W"
  "AgGaxFutpBhL7GDGDQ1xuh8lz39UzIYCxXvd2DdO9Qe49qY235NejPGhABw5bVm75yfWwtf3r2NngASUbWyEBKid7rnZJ5Wav8Zr"
  "unZ1ifqpnjv6lKLl8/5sjGd6JVJMpNTXkRkPILAi4atmwDfECd1KzwRQSopnCBWO/Y2N4tSAaqD1vH+jKxOKj7w6CDurxnEBpGxv"
  "xATpVDoNsNcJ5DcUQXzfJ9GOALHB0a14FifleR4aJyUwQgI07hAUbNXFU4BkQbv38ZUdJQbsZDvjyruGXAcprxcilKwerjoCoGtj"
  "S6vl8zzgWZIooUyN6KGg9NB4QoHi/5kT66RGYOWFX5D7im6v2v9u8E0vJFVqrzmpZFlR+Mj8JIprAWInwjb1bKEnGHAlgn70vXUK"
  "0PVB4r12ZXfD+60FkV5Ingm1Jm/7gwc54ycLSA0xjaPj5e0RCWUaR2p4He2VBlPCuDjpO5Jd68F0B3geZkj/9g0avbsg9nfMAh9c"
  "2aSVumwVqQK91kFzBofqr6I4oyR55u7h0/nFo1/jxeX4BRp+sg/vD7fiSZGXKIcfxvW7gmfK8Z3xf/rDMB+1PHuGbn/9YKB9WU6z"
  "9uZ7sEmvZUZjJ14GWPeB9YaNIbENewHYN8BLyjGQ2WkHdslHagHBycgxlTBzABjKDWLHjecAzPqQV54cH1dPNRQ//8dlq9Ia91Ju"
  "XRFR8p3H83rsDBKX5GuB1iw9VEhaoS2kpNWQ7x/UCVsi0B5dfWkR0HEz7H1jVYktX998lzH0UsfDlrfaXNYkkKSGIdUbX3PbN5j6"
  "g5o/asW47gCTxWWP3LNGMRiHHQ6FVNajbMFj9LjjD3fhxx+vzapbCoN+PijOpUbtBjefg99bAT5/olVcvhYIwKtf++SqWWNlxKyW"
  "R9eLF3UnICnMhMvP7ZfgoyLSkSWFlfI8xZ51QXVFsuWRv7dqnADSmDKhnHo1/OZKvN7KbRlPgDykkQRMqqtt3c7g1VS8D17SXYxt"
  "e27aLoP7DN0SqQVcsqHexO/d86WRRLsLXMyVvwL4uom04FvyFO94lhc/8Qqmt3J5Ps5SbHIqnkUTaNhggNbGCKUcb9NtE6/Zh40+"
  "KMWBSTqfvPQ9z8Rl+C7h59cCUSWgRHTrVQq5PL3WFsB6qFCgZITX/pz7XiH/n8sPzHrYbiALfRcp/U4/rNah3k6TP8bWLGshJXRr"
  "cLrD1PcL4t7+aFkmjBXAeAIU6B2rlVIx8bpnC7MTl+Qe6QepMtIw4R1lh0tPrYpIdOZhEUR1oFqGROx9eITmn343ssT0ngPBxUq5"
  "Ci7aNF5V9c3hlnQZnmSGnPWXdTZd1eRQ1RrcvHenZaKkDDC2FpDsBhChbGuFOOm9hPRYFGhYXvTkAEiVgaSRyauhpRHAqU2ef1c8"
  "Esp1cUelB4WqENXyeuO+v/rvd61JwnuAdFkZGJIvhGMvOiwz4ejFeaWTnmtzdWBeXLhHOk5cb8+61S/vtkj1kSGWVFlpZEpdKtjx"
  "3P3CYScAtrq5R8bWFHAvf4BHQm9fUEa9FbrP7v5hTQqvjIzYffsDSNLeDzBVnUk5RvB2PXxxksQR3wkVMXt9pqr6cCWkykjDrl91"
  "OU2o67OlxhS6QsoWG+a2uwAIapudfgdAlFQNgHZCpjus+H1+N/X4vmb6H/oGsT73/CIjSTkCXRagSvhO6NC2NUMqxfkjKyUoA8nw"
  "1B5Rip0NzvDen7Am6k7UpSobt1Sbro618XcCTcQueaTy2D7+Hsee5hu8MrIgDWAoToEI3YoXJ7uftmMmcc//7SMxyXcAYmPXv6sH"
  "pRi645/TEJSRMl7w4bj6gpcE7S2tQaKuDKtu9Kke8MkTGBt+FwBR/CqAB2u8cjBGvrhqnx/XiG/mPfipM7F0hxrfNwBZviuKJsYP"
  "5w/uZ+ProSyMNL0yud0DFv0N8dWVgSs0rRngbdrYnEqc+06ASwwfPTrg2D6pXwGpsoC8AkT0VKBTKbzwl+WRdcl3A5yRjUvNPvDA"
  "1MEmQLoxJqkZtV9FIshOe65Y4wQtZdDaIZMzPuvmgUG/I5SsMrD/rbMCNbaUeM6NP74p6jLOzbzpYE3EUtJ4sez4gxUh3A6k+M6o"
  "zvqb/jF6VL9dBuYjTCks9N0ePIz03Xk7g0gpbBRWTod1y8+rDPB6JoKRrSHG/LcYYwC3zUQAI+WJMeWIMVIk0hPVbZBYt/iJcT+A"
  "VspVsXF7FUJx5BvK7izU868n+5sA2QqepLytYVP+f4n4qRS4WLeVZ4HAlOelvHJMEJgi40l5Gruth4q0NuXHRvnRh4wxKlICjZtt"
  "nf1iVXU+yq8rJN0YtHGiLFOzvglSgLHgtAwX0q2x1kp3gDGAsdZKkRiLOjGgDoyAK+pWDCqmDGOtke7EQEJJa003YgEr3RhKikno"
  "sd0GoFDdLqkj7jjEOGNKCIiY8PWnx3VJiu7FVzfuB21RElUVIABsgApb1QsC35TlW8AGQWBK+AEOjJAkYC3EZVmLiu1OvCDwyzAe"
  "hKWCwJNSJgACW0q8UsZGPQu2CcavxZPaodVhUsKifXbJrMK2r5VGT/aYNd5iBLAa6mTANuY9AoylXBHH0J1TsyeBGEpaATEwbvYU"
  "wFLSCt1qRNkWambOni26bDHFnilVvngAo3YEDswCWAFjYMSsHUAMYMEcfEQfgOp9MprYokTVp/mfbFsXaRogD6ogHvGI43IxVHTW"
  "AUfcNEMTYwEFNtcDeSDAemUZG7Lb1Q3NFwvGL+UJmADOWPcgEJTyTHc9lDSMf6G5GZ45u6vI3yrGF4WLzwEWTgesJ+D5cH7TDWB8"
  "IA3jFn84peiAm+sppABNNMry3llfbQtVkY/nvVUI85NPmeCcEazGbTvAksUjK1bc/lZYMcBGzgiWuOEIb2XBrFzYkDakgEmn075g"
  "NdYpGKgbh94oiOdPO/30I9OQMpKGC7TpZ7sbT3Y5+dTjagHqDj2dJYuq967i48Vqd96e/AIJYJelqrDmlg2kovHgexionHn66Yc1"
  "gMVLwci9lfN2APSeOaceaSHjGbvDhR/rF6fvKJ7xCar2+722zoAJ++93GOVHDy7dFuAJqd2OTHkH7PX0v/DVOfDX9nUfP5niq4en"
  "HCkagSI2ikfMTpwm7z+RFj9U4LhzWH3BS3gRoJBrgXbQuGpWW9viaVBhRWHtpj7X3PTL2DvyZ6bpkKJJL7XxwCWDLxvB7b8s6GHn"
  "suniJyKIN0JiB10Z4uuxgMGH2tMO5+0LP8RLQNnvYC+JKGrZ0vrGRKQqBXM2q7rOX/4RL9UZ1f/o+3zaCbP+OEjCoCwc29aXEPpC"
  "qtK0JOpFccN+qSWY9McQ5/1qcgdP+PeHeDiT7QcY+wX4QjBlj8OrGFfvx0LppKtACGCHqOqfjw+QjIFcm1T2F2RiLWMe+9F43+zx"
  "sVLb1jqykv5G43QVwytRcPkCuXS6AuDI88ZHofHBH1LFiDR4mk8GH94M9pP/Q/SeRDV3yxEggd33gQUdFVx3JX66XbPDMklLHqad"
  "NnkHigsUnv364InECzZsG08iUs5AlBMRL0oGHZ1S0P5NQAayh+z0zAJ85zRs6Q9EfTYgEtmDL/CgORerdmOCFF6Ra1fV+IM9AIUg"
  "Ay0K64F4+THCHm8qXanK5pG0OIhhYx5A/BTpFEBid77++2CAZBM0h4BNmDkjAR7+DJURL6m66B9joDKwwU+7Mlz8B7x0B+FGbMaB"
  "8U68qQpn4hTuwX9ffS7vnrto2xiMt+DZ3WcQt4ERtUE1LH2psTFV8Lw3XtxzX1vtuhJFdV02K1/8Y2BdquDQ2PMJpatZCXKlyo0L"
  "hYLGfzlROmMPxYUFxT3767320K6DYc8v1Y2/tD4NSTzx6CmR35gtKu1iSET8Yy6drCFoFBIqRGbigc3AwmfGU/z9mzerdv7trIbA"
  "wuzOVHLGnyhe2xZ5KED/OTUu9Kfsh+voevxw9+Vf2dYe77w27VCobFGnJIXNQ/jyeUirhG/943v70+JAQPq1wKdPQVojxDqVgHRf"
  "0YLrmVXNd6gu3lXiGMEEAslLmeszuvRoYcoiZ3a7MnGqTcluvwbdUijHBAChTv719CQE8QJ8gZBdDgPVl97HM1EaRr3mVPWlEQBz"
  "uzJc9Ee8dAcDK30QSBcU65TLwIxigZcosq18FAP+oTu98G4e1lcGWugCUYAtWaENYjPwCH8N1C4Fz6m/937TQ+NH1Se/cV8rvmgP"
  "RDVW1dyDJ4NfLZTOZdHmv1283cA5dx/RF8t7z/zLHwzRM2+8b23YTekkwlbQw6CK+F/zdgCLkQwc96Dqiz9rCCyc1JXhpUUYL6R2"
  "NHgCFVFIcQcQ+BFAsK08xLicl5m5w/PvYvwBW5BsxTqngEgDmIZNcSHsc4SPi8LhGx0mZspFuISk8sg1P3klskgPVDXf2dWh+pPd"
  "vSinpUxFmI9VVxwCe92hivn4d124xETP/ZnAp4c20Hx7TzpaBwRv/hPPtjlypGDXzz6aCJWBTZ+XT9F9VCpdQHyXSDVQiCSVJKrb"
  "yuDr688ecCDpFhj2/cxaGLApUlEQUwvpIye9siBqqYfPn2qsS4eJhQhQPBh81r8eWY3fg1h1+eUXLVedePERfBqCgqTjv13x71g3"
  "HSPs4UgMcRd0uCjfBkhPIMrFSHnqjERgVOl2r2lAYKf84Y3Y+d35YCgS67sEodikkzjZZkC8iEtINjdUt8nhexF3rehyOLBwyeac"
  "am5ulBnTkZhV960mQ6TpTDY2CJ52ZQ4a/NIqvKS8BLY8uO6+I7MVxxx/Tr2AALZ9Xup2qys3K5VWfAgaO9J9far7ewnak4KqnkcP"
  "jYV0lEQeSDZQsckCqZNcju3PsUSmswtEMX41CcUuAbCmKHH814Z5U3HCFb9Ythk+efS9DV4ck4gnO875e0HlS446frwL4xwYiz9z"
  "1vbEvgUwZF0SK+UreFXhHUeelWHX31XWgAcIFCqReDNsjl2M386up+8MXpXS886c6uU9SSLrdwJeTPbI3dVlk2av6quH1uJb8Hj2"
  "VaxXoM9JuxNr0TfTeAPSMPWMmZ+0JrbjseVkSHCkBK5SXVc9+oRDgX6DPonFhvnt5qChGAWrSVMGpAcC2bHe/D/9e7e64ceTgAUS"
  "vPr1TTXVEwbI2LQJoHljn1PRts1NCdqdFqk47Vr5I5Hygiz091vaRckcdDCl36sB7azA8vYKkgjqV/MNEjSpAGcqL2kaa+ljQSgu"
  "ulm19oJ4OirUmgQDdEGhkBIFNYFrLdKyAA0dX1x1wCWUlBK2/a87nTH2rHVen/4AXbRA/rHnP7Y4VyoJjS8kRvXV2WNsurxsCg44"
  "/PUXCylsFd02eFBZAeAomSjfYAfJkmUN2cSbCuGGTyuCKCnhi5e9cmlr7YEQxmbju21IotWN/Tsr0hRLGrJjmjbk6LHrcn785kOv"
  "T6oNK0FLSO7dzMrqaQAtTRX9Rowd1lKb+fAZfGItlfJAgeb/zAKvqhyjzSuHNI4f/8UHMWx672BkaHWYbPpXu9Hl84cONFQXsOlO"
  "+qdBvjEJNn7mrNMOtQDrbnx7hSHSIkPgjTv8hYPBGVl66+L1qSTy9vmf0SnKjAecYh9b5nqEkNj4q1/MOKPBUlJQkDj2gHj+bcN/"
  "PvP2dAaq6F7AgyTyLPeOB6SinMC9/ejEo2rZDBDfUadDrpxuP73nP03p6JXjT7oiIDQISqx8gxXLVy+uzZDrqPJbXv6cDI7SKeAm"
  "F3VRl9FXl1IV5Wk4DF3VIqBGSQ0bODo9LwQU0BKqqODSXss78ysq0BKA2IH9vKRVa73NL4xNjwHXvH5zKnGlYmX9hsqR6Vjlxj6j"
  "dxtEAKiigKdrv6jeF4ZVYU1h3RY6Qr8ieXk9FTgjCqoUO6doWfpfVboSQuei2Ael+wC4MVRNnKnMUrK5Kxs+85CIiYMC/U8bzgYB"
  "SBIlKREXCB24GLJVxDFJCdE4SWEdlkoyVUD47L1rYlPK5QrMv3m7O2xSCD78v5fmzUJA4wKRUrIKOGYfnHqal/Qolfos5N2M/x1M"
  "gXQpjQtEWk4SI97WE+mRHwWpM2eNrwEGDkxHZYVe7a1p6mHJO96XkZc0jj/sLFJNb1M6+NXhY5bfsujzDk69yxJ0AFINNa0hGsfB"
  "lPMmDQOvqygxpvGiAyYY9NOnbhj2y+2Hk17zNp4VxBqCujRPzG64c/oASl71CxX8+jSNgUHwvY5/p5mUpcwvFqVXhE6Ou2qIB34n"
  "iGKroLItRrRUJdR05LaW2J6JpuL+I66aAlQYfNHuUgWpvhcgvu31dSQhh103EmigtMjIqdcMDp/7xRLOvAGyUZEHlXECifqpgcdc"
  "Dr4ooolNJ4N2umYkKy9dtC419PiLoRIJrI/4PkElLPjhqnE/OrvUdb8EggqoTPl4Ynn7IuWSo8ro+ONb68gbUz/ypNMhUERBfKiM"
  "HMWC4gHpBEF7pIJrhUIPSt94tDhWfpAnT/lzDkZk6R0hxZOvyGxxvNFN8fl71c6/vpXJ/1NNNUDL/JDNwyFH8YDLGqkADXEU/3Qv"
  "5t8EMPTyav6FdgG0wGd/3ZEP7m9mzEU12u6T3P8WsOSR6XzycYEtwEpgyhk454mGaf+Lu+l21BVp6iDKw8rFllw15IAQ+GcLnWOh"
  "wFZVZSs/Vg2EeXpeDRRCSvchVNrKMjVBRydQYSn94L/JUGbWo3yposMVUWFpo8y232fIRUCFxQnaAZDcXkE+pNwqFAEVyVFmZUi3"
  "0V0f4lPuS0+SYetKQmpaNb5LyhJV48mGNhX8+qAnuqUTCPqmowRDezOeUF1TJKrWi5s7o2wfn84Wx+AaQFvWkRmYLlLP72hOGFxT"
  "JKrGT5q7yPbxIvE7mh011WVEWwqka1N++waHKNRVFm3JkarzQRTrw+ZNIAqipPqmokTA+q0bEoZWgQrJxo3U9vXLaFuNNyQril/j"
  "98CGVM7ancjYskpHCSC+6VGcAOIbVCCJVMDzikpq5NR6hiSCrk6AygxJR1gEJLHS1VmkAmjkML4ASQSeV4aLHcYzJBElPQ/QyGE8"
  "Q/dxTPcSCKWTSOjIUWwqU0TtSRnZClxHQQVVelgPfo3Pt7l4lv83C4hvKN/z6HbJqh4UUnwXX3lzOdapHLk/SfzNMtYlYE3iALEk"
  "urXEkihgrEvKEkuiJYx1yVYw1iWlrEETtQbndFsYIyTOWNS5HlnjkqIwIDb00Pf4povgQEQVwKBbDYMDEFEtC4OjpIjqVhDBlRIB"
  "hwg4tqUIqIqAao9EVIs0IuD/AyqQ+u5XXOiBtd8oIwkzZrz/CNXHjZr3T8/lg59U3t2cpQvwfOviEAJAbMyoYwuPNvkdTD1i8d+o"
  "0nwM+ER1c6NbC1JDC3sdMv8ZqtoB8aKitI343v5LHg8JQlIH7havfyZ3yASWPb9WuwlCCDwTh64obUKZdmK+5dnPtj8ym3p0fr5E"
  "Jo5KBIfv/uHTHRCgorH24BtubchuF708u7394KOuDcHu9Hj9yS8kaYe6BMATFxalQgaf3XFsAfEO/d+nTsw7P7JGxOTsvg+FJ7wd"
  "ZwuJd935j8yJNa3qErVGNI68kN1+/hIhhLDfXD499uvDj+G1n+Jl8kVJaI0LAfFENDY25MSb65l79/YXs6lf3qaTBJcjQD2TD/f+"
  "2T0dJiAPyresQMTkX96wuoUBwEmHz+blhx4IfjN4w4JXtkDqxO1fex6rKhA05Cph1Jyj2PTwE2+QOfR7NW03rZ595LEsevXe5Yz/"
  "4bFj1j9604pDTtu4/JEth0xtXHbvqhiy1AoISBrG5Vp88HMDThkYF3zDQ4sPnfHmMyEMPnhCnyX3rTF+vP0RZ/YdRJo1973DD6Y6"
  "J+/9JbhmwKag8eEnlS3sc9Srz2DVfcsorN7Q57zDHtwSbyA1+pZ9Vc0bp2fvmcxfzspl84UZJ94ARhOF/LrOvMkcdGE6sdx8WT57"
  "46l8dPz6hw4kSV792YrsmdfZxDL3kTOvNWsO//Le45l3Dgm0FTYoKGhXnP+gekiYsLp15BlDcAZO58CfXBumvQ7vuBm8WvUplWHI"
  "Fedr1WAe+qWMP3Um8Oacyhk7g45lTdJVNXvu1WCdfssATlX/c9s7HXPNIcfuCsrUeb+d+6g+xrhb9+O3eheA+GkCryXuN2cdqHDw"
  "ng98VMc79zf12Q623KkMPWkpKJy86IOr5jYWuup44tmmwAOcUtIOyN/7r7123sFh1VSCAXwqWMHs39eYhfrYiY0+gYWxJ1987xI9"
  "mRkPtgLs/P0FZz6ihd9P4+LCG7ct1ctA+Bauyrav3aLaup93wAl0pGxHOr6fPTc/1f9S/VOfa/V3Ra4rIZ/qyI04gaRQnbMTD3r1"
  "w87Kh+5G3vyenb8l3X/v0cRhNudNZ79fPHL0pA/qW256i8AH49tSpp97dt7js4CMH309ho6MpZM2tYPm6qwxC77eHTICQQYuUrds"
  "n+zdSodn8gOOWcHkr+dn4PJYVTedDPptVC1/P+ZPql9P9usgbzJu6e9msvfKL//6lW74yyd6FQgksD5nTaaaOEZIkemMpAvWX+3b"
  "hsv27dMEseQLfgVZwuDCrye35UAoP851Ug95YtWwQFiwxNolJy2dpvMfXvXB2G7ScJW+eVRD42tKAUjRwIQV/7JwYaeqrj2Ob+f6"
  "ituZ+lUhmWXfXzWwEWgbgXfqZtXOJR2qS+aIcQRDPfbsU0jWv73LwArSdKypStUxwI/D1oh9zyRZu6pugE8travy6Q+X7U7rAhtE"
  "iZYX9BmdeW/NwDRpvIZKnIG+fL52Gpu+cqofT/ckLeB5Nrhfb4P6m1YM7A9p1q6rPKbw6SjLNdq6pFPP+jYSqOA1soct1d/J07/5"
  "5SCg3zjMj1X12YNf0KWHDLXZHIMunU4fr8p9ec+kIwEWPtK3dghVjoEXTmQIXLMhOfBQgHl3flS478d/HvzXx5caojIETJ0ZHj04"
  "89JGqsXvDwYYxbyLH+Lxwz5WXbenkYyA7xv7pD4AqV1OnjsIyN9T5Z+vX48SHtf/O/gN/R3It406+M/i26rhN+9exOd/fWh/lE92"
  "9Njv+UXzD+Go+eeDV6HgZdnyfvNY9+7KgfUq+inULNbPEmzfseTefb0AW4ZWIu6RV7C2q3ndM2+SIaF7B+Hru66NP3zg4e/xZtjy"
  "3DC60oZlrHr41on3csaCRX+ZAIGAtfC/714SGMBOUOTzGI5fcH8/+OW7x3DGe2eC02+bGF4+a4IPI6aOgvDuvigdVUL9znvsXkPd"
  "7oNALGy6qQ9R15gKWPxEu6j0hc57l66GNdc1EGVGAgv+lgeWQ+aHR45szoMiZcTQdUv1Wth4awMbc2t/nSYxwnrglqpP6L/7lEkV"
  "YAARGD5lhBHgvncFhgMD95gYwOgpdfSfOhRivm2Ade+AzQD4upTyM0DGA8i9S0lJbfo8AsiEhS86gI53KLYBTV/GAJkwmLk3YSYd"
  "UraD+DMgiJcAdH1At579EjJsVQmCL5pAEZ8yMxRrEVZQOCBYJAAAUGoAnQEqBQFgAD45FohDIiEhGK2u+CADhLMAaY4HZf/r/Nj5"
  "Z64vjf3HfYTMd2vMd81P9x6lP037AHjr+pT+5/8v1DfsX+4XvQ/8z9pPcZ/cv9b7AH9g/yPrbf8z2Hf3O9gb+T/2P03P3P+DL+2/"
  "8/9sPgY/Yf/0+wB/+PUA4SL+n+fXt6+p/jf5n/iHyL9j/tf7Ef3H/3f6j33f2/vt9Bf330O/kf2e+5/2j9tv7t+5/xd/rPyg81fe"
  "v/F/mB/a/kF/F/5D/d/7B+2H98/db53/eP853NWU/2j/JeoX6rfNP81/af8t/1/8J6J/9b/Zv2v9yvzr+rf5r+v/up9AP8d/k3+N"
  "/un7mf2b///Rf9m/0X9Z8pn6x/jf8z94H2A/yz+h/6z+4f4//pf7f6TP4T/g/43/N/9v/Ye1b8z/uH++/w/+T/Y37Bv5P/Qv9V/d"
  "f8x/6P8h///+594HsW/a32P/1d+/9atO5zFROiRsFVFWpcb7cKN7ydJWlztjxbx2aInnn7MVV8HyLhD+vicjJp//Cwy9+KwWMRNt"
  "HrBppeAKvQYo6JlhPwNLbbFAlECrRpwnccp+x+3NhSCr09i7+rl1emKkMjOATJFC8Y4pS+NoQAq/48gNeKeaMH4RX7mAYaBQXnyQ"
  "jWmVwk/ZPYoa2nyGrvPaufZxRKWLs908x0SOsv1lPXTDkQ49U+GK5i/xpjWrG22BiqakdanziGnmoeSRBYJOZRSEDfSKmnUZuHxA"
  "ASRyOgZFmHUH1l9BLAvSxcrOzxwwvuHRzGqVqVsqxVW//qubEtajM4EhY3KqAqH5WZB1aRCxHKUUHD+d+kTkW0iem10qKcXvnFzD"
  "YxulBoCJ/zgz7prMUpRSeZQn7ye0teFREKR/pmzQHBQfmVlgLa/KHbrlMtP7zYPR9b/Reogt3S6A3+VkdADoh52HA0XVv5MYOWaB"
  "eEQjXTBjrarg60gXuXgx5sG8abZK6gggRI8uouCY/XIUHnhZcZ2kzR9mZ7+Jbnf31wd+Jvalxqlea8r706T/Nt5vNoSNwifh3K+k"
  "/dVwOZdcTIjqtAvb/xx8UPMmnhOUIQVLoQ+8O0uUaY/4HoxAZKmDRsjhy4FdnF+Z3gWYUevD49pKEIHAYQsMXZij7DDHYeW7QAD+"
  "/6DgF+AhRMpJzvV7udJKWWVawjZQ2GilhX0NO1dWRbNPH1ng0ymmgkzWp1HJWFkvYMqI19Sv6GOYulpBpYY7e6mxmFSIBfxoneKy"
  "nByYNoIullzD6EK7APWS8w2tbad2pgrt23nfbSmU1U6HrbLinrK5qvt5u8HUGUJd9rB2mLmNWE0YsqFSUFBLRF3Jj1bKhOaBfmKh"
  "g9+4GI+YMzdCfxutqUWxgn3JzlTDTLnEDBnnITcTAiONle5oc/Pqev3OKYgaEf5+frB+eo2g3tytUPy9bDRalAEzDkeiVGO2GU5C"
  "IthbGCqCwqDsUo3wS9OoQkdPIHtGmBXwxS0vAtslaYxQ+L4KmECjFi1mac8P8DltgeZJpkN8pjhdFq6aTZsOWPQ6HuoNh8DHVCDp"
  "5MHPkUzouYMgLeM5gzmUU8UY3M/GuRG9sSty/YeH3RSxqDiBiCsMr0oH0QX6WS8/ZAwiTXsf3zv9A4t0C2PqOaKGpmt2S6o1TFHf"
  "syW+BHPPDY/1IX1iR0qiPv3MxJSS+OhDJPm+mS8ANjo+rowhtjY6kDs/fHK875VswN4VJ0VcOOYzSd3wglermGQfvl4SBQUsnjHu"
  "55acdvOQYzTQO1EsPYmS0OO3VlwZ2+k/JGwbS2jeczH2Sqq4dfEqjKO1fLvOamm8SuLNBjqdXmJAoDQHXtxUdHSmKRZvDEQOM85N"
  "nniiG4y+Y6pYx+HPkS6/GWCEOFJ3bu45a4AMsLpMdHpb2AdqGzCTOtFaPSX1pe6oavdriwD2IK5RPRuz7RH0CpHlalyXj85RxJ8b"
  "6MMaRTEtfeUYwX3eTmfwoyDeVY7UzlADz+DkB2Tl4oIhuLMQAek1y9K3gP57QYS1wp5ay0m2lKDIlE9lXHvUsSIHVNWzdKapV0Fr"
  "LpS88GIXk3H/+Jz59rcex7mnQdlAuHmn96/9m20Na9dkOFYLJHLghzk44daB9TaO38MMXpb8KscKXAHgxJrz9kJCvHqW6lL8IWGV"
  "kw6+fkG7ic/VipgbqvH51kIlRHm8ToBiUL7PqBAqb2QEhxtITo9xkH+EFRhDhUwVwy23P5wuSBz48W7MPmyJqhmaPKKozWhEgsvj"
  "T7YMmLJhKq75wCn9w9NZ7gA8GEwk4TsoRCGh3uVeBkEbPTEVCtURbb845s6FRL3u3Hx47jYrYF2eG/UzbxPRCsMCH4AAhP/WWTPD"
  "eEXdbIV8UzHZUd0syX/cLaIRUte1WxlXpoy4rF8YPmlhr3+1Do+EID2UAnUaMjiyEeyKSEIAsXlwYUnpEf/U+Z1/ITn3st2Hsz9P"
  "1qVLmlbG1DowSI3EUhn4wS8lvqghY46DVflPHZ0Qgt1qsfWyxaemje6xnd5DRnGXntSWBpKFKsIg+2Rkf/C3TsUKGbvvdZzLId2q"
  "768mqLaczCfQtV+FJgMed/DFY6ZRlqQ2xECU3Yb4SnJT0vyrgNvnts9b1jsxqCSA85EMS1Pbif9+1lFqzQq+KfYAskX4eZk5J9OY"
  "Ptrq3zAVEAjl5hOAj9C/2UZ47K0cgDSvdL7icSPpJisziHWswznYv52jAOJpKCwsIhuCUJz2x1Qo7mlTEUfnfmqPdjRkH7x3tHhM"
  "xAIcjIhgZrGiMmm0tCYOKsvi3rhRQ9ZJLaKIyu6Ar4KdpTbFSuB6yi4A3H2EnumRqFkhkYOsmh1Yhs7Mnp6OGvxAArvNigmQxNsJ"
  "SiKbR4CV1rouVVp22QYH1GU1Oo5GMwIT9b3di/eaIFkQZRRHk+x60r8OZ3k4HCyJa8eSbGfQh74wlbJ2eJLrUwbXqh86a+zxZoaD"
  "xJQxLaA+PphPD03f4y4XeUugHPDEv7LJ4pZ71qvan4Uk1zmurjrqLNPg0yZ/jn+EbLuG60B+7GjR4fnSSG71msnjC/lx8DVMz00b"
  "E2BlEIuVP/Zh7UF/isCkrKe5G7tgiix+Z2294BK2OwVrWNyZsMgZZMBSEy+jHim/6BoMKtrBHpdSeRIYMWHv5bRIpF4dBB60D1eJ"
  "1ciQqMfoLT09KZHjlUWf3r1Jx+VC8JBfGbfA/ygSgwYZCAvKzh+uqLFV8bEuYg/IQQCbGjdTG+9brkG7EJi4MiRHJEnlg/ZXgOp3"
  "GhvqisUyVTQRSJT95aUNOntNeBElZwB9R4cP4OnoDoHtSDGWBBGQVw7R9hCx+fCfa+9wGFRfufFcTi12CbE7V5SByta+eK83Nn7L"
  "YAcwQh+5Q9165wM/uOhK2VP4HdABMfK7yWyt37u9R9x3nGjSkpm8IZ1pqRYkNfdDhejGZ04KuYUIKzQcYK3R5LaV9exYsojIlCKv"
  "G3E7Co8Qu1+9dstxJPqK2titgzetNMaSJz7mOKxVF/n4B8lWQ4xHNs5kezyo/K0b1+olxXKt1SymN+heljs1LXrsRzkbJIGAPThu"
  "L8NKx8k9NL5kfVjBKoKX4zGSMPwxiU1ATjqEXU7dPjfTBGu+TuA32aceeTvKzgH1627zp3GN4LLE0dFAb1Q7U7WChfNfvXVAwECI"
  "O97ztIwlCfooI1zS2wQ3g3MC/ftbg+9wLVVL/50v4UuohqhBOAAABhVdCEEpo9PbjM0oPbVoji+nRONstofu27kYKGqQAqaTQGmg"
  "jFMyw38ePX8XgwizKfx4+dk96fX1+nYLf5b6qDWc/DbqlAW06zAsapGDwZXW4BRBPalPAu2L0fglf2QwQWHtr/hRImq0Y0vbMc8X"
  "l1RE7wffr2aJwT17d9QTFr1iSP7rV/8ZYiQ/dRqmOxz2sQ0gAyLZU8aCSXr7QnYsquYZ/1V8HyMLbcdkX+D6C0RK+hS5I9v6onTI"
  "8rXlFToj/OTWizb+Zm9RqeZHCyz707PMU2KclwBuY44r6C5O85K6OPuwKNYB8mBhOaNUdTYgX6XDe2zKO94RdJd7DOc2PHFyI0jm"
  "soXwIuvCXgiHnnyTRJ5FsvGRQKlUjrkGvol1TjQ26GgeZTX9uzxw9CkTgd7NeJPQSmlJArKIDYY4Qbni7LW0MolhsyaHp8D120DO"
  "qpSATGpJnqS4Hi2EA26mbD20cmWj/UAiu+6lDwfr9ziPqmy4FPz9409jRkTF1a0EgUOlP2y6cG48EsQQwbjqi7Uq/WUY1Xfwin4V"
  "iAqPJ7vgRlufD17oWIjojrgkV+oGN4TwQLwFcb6hpv466JCO1SMYrgcH9de4NlG0rBsUhtXihawt4VtZ/zGI8Q+69DmpTvul3e+H"
  "D6DSRAdZkXhJJi5DpoOujd7jv9StYwdHIH3+3+s/lpimxUdhya6PhmUOVdrYWzfDNQ+b5cs0JTEseCrHmlFtCk3cKWKcZy8hfUcL"
  "qyLiFZKWmKJRlQ2urWp7EpPzVddMdrjPl95SnFuGF5ohFQDXB0rnqi2is38du7rXwvRTyroGHHLEm8KzK0fmUrqQtQSL0+7ccKUL"
  "os3dGyDBjBNozMsAjx25YVCqSf6fdBppuKfuUId9xJ1z/4iUQzU8djGnmcgAWQPJwDFZmcBKBA7B36HAHAKzE442xDte+007Fx6T"
  "FEH7RyrZtYmCxf20R8r9QNhYvmL+m5wC1PQWhuU7/MLCnDxHOQzRN/jUaSc8hW76yarCWxg07aQvAx0P75eH3r6/mnNXv4uf5g2y"
  "MjgRC3DSw9Z75jCVzgkBz3VdZHQAhNQArArDOilhudbnLdlSY8bdU6yHPQSX/1l7///tasYmc21peFVFsRI98YAAIXsNf5QHzUi6"
  "0AUC78pn5oW2d6X3YMkboKBPfwp7dD+SnSrCx1iaO0gdv8fdf8kP7h3EVD/i/GldkcN1oQSX5O2CqngZYS/m3pEc8MeJFoBbR2HJ"
  "MWVo1yDvwnDu+2H71X66t58h1+rOrvWQM3FEAz1La7NSjxMhfbHp3V3FQ9cPBxUdBf9d5UEaWuXkjgefyVoB3munnaHF6V23DrCu"
  "YR7AV/TY8wG7EtHM+3aI2E6DnQmYzXeFz/8by3H1wxFeIxqCwoKTekWB9B+/vJWtZ14qQhux7FpQL4CRfQv+QvzIwTvLxAeeesm1"
  "LkPDDoqNGJUSwl2HW6kaacsOA7Wc/dD932aBsXOgjlhwQdwTeRYRLtm1vrIiwaBqLCkjEVtUfuEMa1gxNSzEqWk92AbCBPSv9hGg"
  "Oq3HFoeAXCmN9ee5EJFeUJyhufH3f2SVMSbAisBJG/KbT+juIPpE8tC18Lf8M9s8HGcVj53iT6Nwqss5z1X14jai9KSFa4r1c9pI"
  "f0eLMzDiKEHfYzGM2MCASdhtmg8EVlRWvJRR7cCzI2MXCZD4vQk5gvHKptQ73cfDvWskNqqnVj8We/6qlOwPDLX189T9Tqkasx9e"
  "VXcXjOLpXDIykZchySVquYSnWrqYVWXY+iq5iIGhiev0llHPP0MQOfEIioybziB9sLwMwOEfhdXNwS68a85HLQ6HvikqtJxaERPp"
  "ETbVoUHUkUREv9rTLPI7szLYN9yugqss6e5a/rcHj88D33ent7woAbWrW5lFj39cvCm+odrfTchELQsLTvlGck7ppQPT2I3DaxvZ"
  "89WHMjHj5FRpQJO63n5UhD85+ethyBBfK7nzhOeYCGOYjQ6KKZXUhgKwH+4lVxETWDuV8qF2ZN1yLDW7QJngFIp6U6iAkZjmf1hX"
  "WB2+KDyH+HV9A3ke5mzs9ut0WvriTVOSRWP3BGq77jl130tv3Ep2e86HRw5Am0K+LJfv4i/fPw8U0TwPon5lSor0QdFnwoSbVTvC"
  "0fL6VFJ2wahWnDYC/Cu9zBzi9D6BBXH4xNTBoKhpwUjjEQyzF3chpXQ66ZZzdz+qOJkOZ6HIiUSPTD/fmIcs2CLWdbyPjk4Hae9T"
  "aHMgBHHsj4ZbZwpHYTzO0ToC8CyS+Jj6iuoF4J+8ylKOtleVGHTElrFwpGQ955mxcLF8VKKu8s9/ByNZMp9Vkf45PYQRe/t9Lmy1"
  "ggZsWBtP8qxGuWgCeJTVspja4OhMbhGk1UIdKDTU938SpjnlhzuDzU0ixMQZV4IxPtwnQQjaFUg8gvQxZO0Okgpej4pMh1b/58RY"
  "6hm7OJRWqIw43q0fU/dRj9LTfPQKAlktpIU8IeNxwcIhF6WytoXFBBtMhwPmRQuULZqxevHbRAfY5mHWqvN/23MRbW1o5HGItDdh"
  "ZdEAirKiLuDvgDFcfdRTm2y84k1FjiMmYItFQMy3p3bWwS3c9KqS1dilp0SSK+7e2ugAB81ExlKdQu4pnmouJZ78M6OO4XvjweF1"
  "nDebeOZLiI3RHzA8U+8gca/ZeZQseakrzijVRduTqkpB/oPT8w9aBlh8ee9aSqS1UvxF/GWTkxtVBSc20nhJlt9iqiNi+sQJoFZU"
  "GP/H3no08D7jWgXU6IhuDplt04QyJmtPmK6ohg/zFsrmA/qEekvTAJek+0U/KSLtpVxJrPdkG9I5hRAnJ/8L+AOOIkhk64mpxfHA"
  "3XFcg2f/KiCQpL4CkPUerHdoGdj0tufe8dC3dWod/ExXWhunYwJzLLGP4G01WPlUTTVrYRbcMtRVAe+jxl1VnvXhjHBgd8ZAAf8S"
  "eWEA1105Z7uSg9+x/piUyBMDtuE+Uxk1DYBz/Gwa+2shAvAKUj9NR9RtioCqsPqXrt4Jk4B7F+/Izh3+0xM2FtTW+V7NM0CNwST7"
  "eBxnNbscq5QjeLnppswikcusJsplpHp5h7MRdxClhsdCrCszqypctw0XgQo5BMBfu/znQrny6NFupcZPuqqeemWUh3y/yZDn3nG1"
  "x0IRe0wfk/wiFvNLuJVXr1v+H1P5cmCWokgduAP0fHxFYYvrPdBVa5xeqUyVIE11Zx+YM+6yQFqoCbu/EVMf/Cg3gBEejV88MP9d"
  "uN0sOFVOvemuHzAtCYm2g7JWMtsNMSbFEkEAVnZrcw8SPoNIOs4Wl+vuzSsTxfvRL3HgZ9h1vdp1wrya3VZy0EbVRpN473zlUKnT"
  "af8U8wMsCGontwbicPxcY9LSKuxzth3BkM6W3VqaqLrnhs5K9WTenqBgjW5Ebkg5S+RGyrlyY0xesDnSp2t1S9tJSEgvgUVGfx5O"
  "XsOMXJcAYDVStZ/fBtBfYl3YJiE/8EsUkCF+D8ZBVlNa0MwkZAFf/KTEN/h2obCp7fgvT+yLeebXv9PNEt//o+OmB38GENqQE0Df"
  "CRXhSncSbmy9kLN2o8V+72b/zy5cy0mf3/YV0gwDxplVxSXizmq9kkfl0PFlOhMR8BHdbl7XpNja1F77r5i2UTF+xszKYgJXMJar"
  "oB7ZKDBlt/qMC97K0hOlZqjjEuuRaqs7vFi0psfTEonB8fjeemP1A7XBLrIjJtXqHpDUB+XGoENc2Dnqk0+FjZ/U2gfleUnq4900"
  "dfXiGxXg7BePnIjHNpmyS2Wl4CsdrnKndbOqlzNwjo94pb7v/zTOb8X4zwZtZLdvvZHJhfjLhyW0LbJweU46lPYOoXaAsDSP8tUJ"
  "JlpEWMRLx6sKeS1IzcZSpNCg/NRzoUPB9EtOAdBMfTBxM8vqdoGreE5cz+ZvLZWb/2x3famiWE+u9C3jub+/ln7t1JlBTTW5rHSq"
  "7IxTQcVBNZT/U/JFw7bVL01/pXlZWs6Tu9J/dUYVkKj5S7yiYdl4XJga5xATkYHZwgU88O6m+WJp9pAzv1xWpLU1ysnraL5InPoG"
  "XPHcuoazGVKpSkFGzCxv8XOhVhwlpvEMJ0frWkpwDr7d8lakCtoPs9PMj8YIq6YKUcUEK49cIPyGcaj8imOvROWuOr044AcRVATV"
  "uXJKjptxkBwUQJuysgsROy31SGCZhi1wFhTubtmP/f5ZPYoBWoDbSNdwgBSXlHAzBMjaismkP9btEFC2CdpKOuqdwwcxCatfomGf"
  "0nJnuxA2XTLTZoooo5o00fvLScu4iNok0qOL9RxRbPWS8UdAearGYv2GESXHmw2kruhV2rTgZfXj3oOm1mNpKsCE4qGbJJMnNQTr"
  "rS1LutoXhmvbrkLnahEGoEi0wgeBuiTfDTiGJHHuX33sWbHaDY60sl2obT2qKoAMeiWhUyPB9hR/GIa8YRGJT/zAKiSbHq0MJIkA"
  "m1n2UrAZmBUjoGYi50ipdEMv4ZUetMLoaVXQTId2Qp+ZXle05ZdnqgGEwGnHD8d5n+Dfy7v2y6k0MEg8iVpRy2zbceSFhwiJ1UCp"
  "c/2q8gioCM3fZVGiJqMEgi3wdyUkkT63Hh6Rg+K3I191iXvevjsIwzv7NrKdICgmGXBL/wpbESgQOVtmLWHfunNSRSr88l3pV3Il"
  "8USvyMsyNC/S+0CuCysei7+7IfAR+hzS89V6BOegTWF/hrBpMtGJ08JDpYhJzyTHB3iyRa+nFNJ22mM5ekcMND1DiYfIJcx/fzP9"
  "CfTilWAzwnIRFCRnFoCyydZQAiYFsK7yfD92ATiRFL7JU/LrlIrbXJIHemz9wmEpi0ZmBc6JZEar4ob51puVtcwp8gL8g1hFUQFR"
  "t9Mzgv0dVxv9NpJF1SYvJdmTSWW0WTcO7X58BnG4nbmrnV0ENMKvb9402Kl+I9dqqbzJPYP1es8xX4fpP5iZBtGOe4OcaEhml9/K"
  "95BaaBd7Y+tAhXTJpNQk9EiWD6tj8lyN8gdzdctN08K7Y9iA7zjvEQu5TrNOg4RlrNLrWexh3/E2fc8rh7FhIHMYuZjxQMdfgoIp"
  "nEm9WiLqbcdSbOLcbR9hBpf8dg1Yw/wxysnPUw5CzxVpO4h8uVS+Lcl7RvkmSR7yqlm7tOtbqAUvX3c8M2y22QE5gM5XUdz7RKac"
  "udae/gC+PDDsH2u+6j3V3bvIYwQOyssqmzKgi/elDGQpDN45fb2WvIz91AuG+nFDG9QqJZrMrMBcj55FPcNK/CHh4RF9Nmyc3Z9/"
  "l7EkgDXtAMdeJtU10mU+2sQc5r91W7amMc3Xm9SGt/yEoCnRr3TxQocmidZ/XJENzZdY7MGfYBLvRng9pG+AyNqQNdo3oDToUXhD"
  "LzWhNXUzGnmox81Raj1lmA7zKpOhUIcQ5Eo7WSQMzQozIrqO8AxbhP+SaxMaioVIpDNQEm9NELBrvt9r/d/jKxx6KMYbpbH+O9kD"
  "HMU2xpFEu0fILqmEffwZn7FhraxhBijjUY80XVfDLTM+l24C7dRFljtQppBwkB6LQhVwJRx6u9yCs+Wz7bwUlXtJdvr9LPDvmHMU"
  "+ossDDhYxKvnI7AMfaWioQu7LyIKx6WD7X/TMDPUnAVKVQgLQet3LHnOliSp759fkPE9q/tf+yQ/uVTWAb5EgKhZy+bCXy0pZUes"
  "jUlCWDAQ614mBuBbU7FbV1EcGQRAQxuK44CjTMH428IiZeZU1VbahtUqLelozO5IeY2OtQC1nOveK3fFxDz3v9kpAxZkAnME5CSi"
  "Yq9liQqL/AEcPNvgFO4xWeuwyNEPBUfB9yDZepkQTjJCyGAJJPlvPOhr1hb39I1UwBl6NjXeQLHCJmj4nCuvD3wsQXNXKeMgxiCW"
  "MKdvQo3SjcYQmByiBuctxgab/1UO8nT4gVY1LexE4Z6ANC62wCOmADZoFb/ZQI7BxDIpA47EskAD5rJCP5Tn9/fra9c0fUoY0c8D"
  "4WzaLYGjLnQXbC7sNCsh1xY/2xT0EerOfKpjUcCBZRoIdfhBP1O+Sh6f6G+2LKyFW6fOcgxBUeyPb7MeDIHiF3yY0rXsYmUDTSY/"
  "JyEezrcIHr9fvQibHL+fg05stXeZQQF96IRXfcut0oduB/isbj9EUVrutHTHGq8dGnzUutAcQD+jSxhDoKDS+VTGWtA7z1ewYxFI"
  "kk9rf58AoO8KbADPzXVBZbV/InguhQiBkXYy3SMwYq12SVq/SPcKV2lCjEVsQhK7eSZkKr0dsPTarc1pQsbPFR9VdUDIcl1ZJnv4"
  "0Ec9XL1NtvOruPKt53zBZTA2ApHV1FLxpc79P84u+YKZJlNu/wRQ3RWtF1Hprdo/StrsPLhLfNF4K3yVZyIeFj2IIxGv3yvNmcx7"
  "asCZyEiuRvqSCKHCfbn6iqPnpKtUx+tSnjOUn9/yWbk0YSMqMVx4DiHuHyAlThtYaCQHg4rZkpTKxWzqtH7bN8Qj3j4HZd+fj53u"
  "byml62B3F6c+Fe4ehGugQEN4Mv/n+sW+WlXgtbuS0zqmRcw9iUHCY4kUn+nGAJZeCmGyz++AEmAz2Ya3/jcbuvoEZeimYy0TQ77X"
  "3zAcdovTJNSo8LCH+so1RNGZs4hAEJBY3Hi1uBZ7PxyL8VifF6fTbftcMh47RwZ8bvIo7ZCEwlTGUWnTG1N6nbobgFIhARA/6rMe"
  "2WHvkqKr1R1JObZypR9JhkCygYKVAQcuMIzm/MbTGI+N3omGzpw/r3IMwIjuLWtVWsBc/VqZtWwsvDfHw1EPOVTl1XBl8Ta4EeSC"
  "7+r90jvdW/LnuVos1cncUVqsIZLaq6JY4EjHgVcq2zb7Idf6ktpBDU/ZDMrSAMh6Qhg6Hvr4YdCzoksNH2QXvH76wePKxn7VnYV1"
  "oVI4/R96FncRplvTR4zwJ4/8GSVw4ABBI35yzmteDgABogUOiFz3C2fqaQQB7R224GYKYIzjREOkYH0HxC5iuYrxIDvnC8gs4Pcn"
  "KmqB2Bk0cv+2jSJEYSo+FkyeaQAmJhsUyOEdfaLJzhtxixGA78G/PaZRSaxZM0R7L6Y6lB/j9pizillsrJecsEk3q2fTBUwIOtM8"
  "PELIjZzSeaErrzEXoxI+3Q+tEWH7JyLgnsh8F5Ax2/V0v2PeX6og5OwKjtCALc53ujy5K/Y2+ZHu5F/ZXeaA3K4Ej/ksriAmZF8J"
  "rVdm4C2eiXfhgPOYzOAE4BwwaUUEFcSapCfCAB7SJI1kPHdwuzbfo7oRExxwuB2FpyGf/MOeFBtn/eCvSb2gHeF8E7DrYCZzE7fl"
  "RrTw4UjZgVqXW7p+tGvXh4d86oxplXtx7UrAuee/v4vI+PNnjI7Zy97crUwABxkRvg5xIMlUisr/B3ErGSxxoO9P5S8Ps8QlG0u2"
  "3dWot+DPXA1B3jXTR8W/ud3GbxNuR7KlnPwamzQNDasl2//0xNHisZuo1/xzazazN4ygfDSWlUVXFwY2hUX72pfZcTPF/KPLcW8v"
  "AbnqI273t/1QiAA/NgQo0wHjZ2bEwcoyj54jhz5pwOn1vrdYdP8dMuipXARJW1cZfwNmPG/yQakEmJ+2akDaqLO+2eMGvjppGiP5"
  "skMqR19s3ksAm1z7bB8sslb97I6ai5/1/D6KltUkrZD8CQUuwYAiTc4iFA/oJ/oqtAqrJxvxOE1pDhp8sxRQ+M8T2BGpAwUwJQeU"
  "uv+e9HQKpNDmCP3S778ycOuaLmZ6C7+YKk8OSlAe1RJwNKGrKFnyDmoMwFvXZnPqbe2ySHKuEbGsc9D/5uHgWJv49PQsL4v7gl0o"
  "ahDy6KybyELM56jyvXj+Etm5Y+6YFPucnFbuGj/mGhL8PUcZw5RYpOhtc86d7K/fv3Pg1wS/oiVCjGt/uqQigZeAaNdAmvy//Ez+"
  "XJRBibjTZrhKpZoSbOG/41SnFh4WB431nrNb/4QNxTxROy4NXOUWkQriFlRL8G3Wn3vNJNoV+LH9G/OQupBSk8Vt2s0E6XwTdsET"
  "tcHs8S0Cyx7sd82TyV4k3Akg8BtENDWcotcI8eqdVX7zFnEMTB+raT+MqgoYk4sQU11+X4q4AIjAeGlPU7HOMaYeiusCEutwzSHx"
  "y+FvlkopSIbf9UHJvleUk/frAjFsR0SDbpd85ox/JC8rLhRLJVPeSqp5r76gLQl+JDvZwiNeEahgM8Gt8LzweE8rI/hQrwPZe+xS"
  "T72fv9/Qzct+sASoEKt5/N3vCwNc0wFz6mSANweQDk7oSQY25qJfClGIREhul/hJUoHS6mldWdkuVD2E73kIhGtCB8ExmlvHHDFe"
  "0IaiWqcRmWZ/i2B+V+vBf0ZJldLJpvUcu9tqncN8bVyi/WksIz0HqJtk2ami3VcJrs9mCciZoZWI8UlUC14BqUwoxChLUhadm5C5"
  "N4bDPc+aaAjKY0+ItO5BRuMnAW0acj3fKZ6WjQ4yebVUcYbvtZiGqmOcyEURs7RXrKzzRmkX8XOoKHpA0WFtQbNIaPSH6DOI/bA3"
  "U8lu2/xDyK3mfu8cBObltEz+HZ8l2/xnrpQCU76M31DIFawfaCUzPcwDy55smAF9Z2Lu1pociFS2bRYAmYQ078tsFmn9BXw3cFCe"
  "mnVleAkcy4gLs7raokzKDGuxL4ulxCC3GSwOFlgq3xdWeJ69ExyiSm0K8DtxmcxjcxSYBOmgnUYbBFnLwBzKRpMIEMIFhxnX1msQ"
  "1sPEU+nUn3ZMwrpOwb6oMkx2LlXtaYtD2kBsz7OlUdnisZPXx+OcwAAAAA=="
 ),
 "badge-nrba-master.webp": (
  "UklGRlpCAABXRUJQVlA4WAoAAAAQAAAA5wAAXwAAQUxQSNIfAAAB/yckSPD/eGtEpO4TDtu2kaTYu/dK13/Bm70aIvo/AXMFvP4K"
  "nO353ZfjwAIotPacPw+5XaDP87zxrjdtn+d5oy7wW2hd4qHyd+vUs+eJIioEF0AzJtEIqI4xiRIlLknANQkIWUkSwBnM1RFmXADX"
  "GUxKhVy7AGpAbSlttS0DQdu2cfjD3vZTiIgJaJWmSvSsY5cX+lQus3JINzSvDLb2N1IkZH0RQdBQlJl2lVSWprzmt3qqJK1HD9ZS"
  "5H////VSsm0f4fP9+Xxj1axJGBhAWgWxUAG7u+voPvbu7u5y79ajD3Pvct9PdFcQW1FaQCSkYYKZWbPW+sbn8/5hhiGOMyImwK9t"
  "26okibbV+phzmXl4cuZmZmZmZiZp/wiLTPLe4pb3VpmZmZkZkiHcbc05urDQzC31iJgALt7EqS2+5wMVHh8KQKYRL7z7mb/69g+n"
  "VYv9nYX899/6iUf2me5FV185B7cq1ltd0e79yD5ATBrgeA83fmpB+OrTjy7bi41Sx9ununSwDphlRU1YIIN5ox1wWNCnxb6Zcywf"
  "+WXc01VBzXLUWrDF7h17mwGu4fW2YQzQVEh7Tr03QblCEp4Y0BphkHCW4zNPnjuTeqKjjLdYWDsbV/3zZT05aCIgqELryZVyuSWH"
  "sOjtwjkJi10GxLxaaxIpHiAlADPVCgMC7HJ84V2vX9SWJ7my3oAAYezM2/7qnGriAYGB4a111zZ79tSuqljEvB2GbM0mnnbaRSFU"
  "AUKBrpE8ZzqxkMGrBJaw4KmFi+e0keUg5AUQgAAsQH1EHoUkGtZsvvvfXwOw5WpbiKOGrp5kpH3BDVfMjlSDBCACfRUrCsRUCMyy"
  "AWGQ5LHSOffkKXGWAUJzFsJMJXJw/YODNR2iY8zW/713+yiNSkXnDL52QpjWUy+7cD4oAdDDyoHVIx3EKdBkV4ERIoVMmN5TVs/e"
  "kmvmKWm67mRCgOCznXV1aY6I0SLNLgpdN8PNSZdfNodx9hrolseFsNVMDdomZgUQIuyaUOJoCBshbNFE2KW3IAAF2iOx+AAfFlof"
  "3aULhSuuog6Tvvg4aWN4LkG2rWXq4k0khUt01ps4ndC2ZQU9Obzvh7/jkJYAE0YNZ2inHu/wsZ/nwpKQqw9dKaHGkOTy+J5aupgX"
  "MAI3z++lUTEIjNYJ8JIU4dECgzYIG4FKwAd92cc92WfE5ypiVCvw/EdHHS2BYqReLfEe2xjMxrTdWQxg4ilUABNcpJAx5w3c3/Wz"
  "P/KptAJQDSqAxKn72bBgw0KEF1dZhLWk4kecFVJ6oQScfqXtBVUACbzKaBMR2D6LwqmnP+z9b0FCUIIigKIwLXR2Rh6QrpGkyNBw"
  "1vRgC1szAZywADJDmVxkBJmcV1jl2ReOTBWo7+0sIhRqzVOuxj6MdJ1iCNQPDeQOBQbMvBEOa59DMxJQwr1LCFszAiNAS2l4soLA"
  "Ycyuxw5crEJDQgz4uKvy/OF4KHFlpKgw0qwdcmCJNbYwOuSCFe4mOKsMFGY91ux5um/xXCkiHqqtwac9A1ybKAFBrZ41QdJoDaA+"
  "J7DgOZ8P2ZbOAzhZKap7WgGD5MkFvHzTOwOlhK6IxwjpCT3Sr3hbALFSEAfErJjVNoPWWJYnOoNQGLAmCl1FQEyDYoj6iv0Qo/bV"
  "EFVFh6eU9oFTkcTDl7lwE7TYniymx6zqXd16ztRi4jJ0JVTE4PPBykiOGnXUTZoxaEbnk4AEtMFojQEBmvNZmrcVQAw4vfDmuWED"
  "HfFVkFdwSb13GLyzBeEaBpevtBzrGtkjdmpPUbSM71N6eCoYo+lIVk9BvAvY2TsZBHhTSM6J0RqtE2DAmgiYIuAljGNwpqWzGxhq"
  "XIHqPHmzv+nJxcaSDfjpR2BtuewSyvTk/GLeI+m2/37dgRcAaebYYqmYEmOzH9wg1Bu+kYFmEWz/ef+GT8W9LugCDGjBGIYDfeyb"
  "BBi0Kg4Hage8k6D2u+/4xfuq5hU4a0Gi45MHE4PiYQnQ4YFcUawT75Ztu/lBcOcyNQGx1lCHkmPbtNmA7++pAOqMHXnih357LPQ1"
  "IgEeosNNpnB7WGK8qs2HUyTLokiffHg2XSGgx4nzijGLRkyjluLTJSS9kBMVAIE/lDhVsD0D7oTIWp9+0lgqejDiBYbzQJUo1MCy"
  "9iWY3QHIEWknMYqRFgBJoBjqjLxFawQELYDxnhhMNRARxq+QxPHJ5w4JYdIPRMTn9BwadEJGqQD59NMObgk8x68BEOtniuicOQQ9"
  "179O9tyujIOMaqWzzQBoDc4O1OLjE0cSSw/DqBKdltQ9IZkC7uLrV/9636GjYLTTkQoQoFLIic5RBbPeIPR/7ReUg8AtyQEFpBWA"
  "AnzzwlORhAp+AKJIWJnWlnlSDYV1IzOnVUaGhirpUdg3DW7Pbk/Hm2BPlqOIbJxZQMtc4Jrz3nV8I4uR3/TnzXVBzXpl78nhkHk8"
  "kr2lLs8opnVWz6Ajykdg0n39t56+/wcnUi4BegTaI1tE+ti9Gef9B/S+pURrFhjttvKaL34RUJKSL//s/QfA5QZMKUFy+9zBAPEA"
  "SPPK6e018kIBdVcMUZy+dheTLuhRMEewb0ezVx6BS14Bex1Rg9GcX51LSlMv+dKPe8eDelTdsWJVUDDOW0CZjTgMPtwUQpcXmgTm"
  "Q5AIIq+eBkufmsWs6xbPcmLscYDmaQo4s1oTlYEOls6EmMjAp3/zN757KAoQtgM74KACN+/4zKPjTaBLS3OJZ6SokyDPVm1Dohdf"
  "Rs6cCydKXIAkLHeWEjoP66buaDgG51cBHh+m3vn7Qp1IEGt3NL1oBwL1pFwNbFJvYo8rWwgbTLqK/dSDwK19pmoRGiCFAhhxgYZi"
  "NbBYtgtHqZcw2ztE/SCOINj4k/t22si+TcYyYNh4kLASGjl+TMHAotNTzWwp8CtXhIRZM0rx9fo7IS5SkA0nKZl3kIgS6DKGA9Rb"
  "QXMkX/uT+3bZ8A4QEZoRp8u3YIpWOF5NAExb7D1oC4LfDsXUBYH6rBk1LiBRGX7plRecMWhbCE3RRRSyfPId618+kIvFJTsbgMHg"
  "tEHyBDvPQmqrizMYbeT4sEXggiWHQEOAsNpHGuByGxprcpVBu3ioA7/41bAz4rxOgCJQBBdaIDj1Hau+8aSKAdpCQIANBlBogrBR"
  "jjsrBqy15thJBMLKnIvLkDfjZPMATJ6ieSaI926kWrnIRM3Nu8DRN66blSLEpQqlNHmeT8Fg44rxBhBEhACqPQHxjYD2jdece9Jk"
  "AQnpPGGNoXLWR/6wD7SQ9D7xEpxUEDxjZoEwWjBowaA1AlNgdGrwFlRCwmibQVsAgeEGIPgsy7KcIJbzhGZQynDw+V99+pp2CIYS"
  "54LolHcuV/JGXDasGmJMFfW0dxa3WsFF2rTFuWvvOPMpKzYRIS7XiMuzebP7yFFvq3GZGO7/743Js8QBzyCmkaHuuS9fPjEAnUUi"
  "IG1kg31g8zykrXE/R22NT/3cf36tlbJCa7QlW4pTFt8y/91a2SYA76J98Dr98gmPSSBwxSYF0xs68OgGUM7oglomY6kGULflzpJD"
  "hTiDGybpbyTeYUohI3tnVxjujKInH/bRcOc154xDOcxh3l+2ce+y6cINKp3zJ78MCOc+PHhC9IRDL/UD2IVN1WKso4iqU+oIS2WR"
  "ATfnTpLSHjvSxGpTWhj5Xd+Cm2ijABmOAnORhoklIG4Bs7cuBVChJQHiYOpfffkvotAB12T0y5NWZyLZSNoNCKmxYOO2JwxCuwin"
  "qQ2KOoKSWFi1LpGiZGrgjdPz6DIE+0aA2v4etJe4YIH9FaASi5nz1yp0QVDth3Jy4NCrc9txlIoAYggCAVuuRgsw3iAhUG88Vz+Q"
  "GHxWKDCwNG8BzGKJ8T4qF5iK8t+/t+7V0PkkySrX0KUuBlorUHmLeRNbgBGC0/btxhZY9h4IpNWnbhRDMYLMuUAoMcMHZENNTNAA"
  "Vq5oBdNWQClcZI/if/2Rp+sAUchVNFYcUC1bZtwsqHPgCITCi8UpjNtYwMfTTw+1FoutlpPb934hS8nzqOnXr/EgpWRJ7vn4yVhy"
  "EtorjV78zX0Aol7XQI3tHAZCYFIHbMiHgCYUhKGz4p//18+/BpkT1GlOHMrgF8eR+ViSEj7gvRENJI05afmyCtY1hNU9tJRNld0F"
  "5YbRmrt6DYDAAwFQbRNAPWOGTce0F977jh97GfoCVgI8PPv6H7NYyigRK96ZwoTuUt+zZEcBKJ7DCrzt7swGVIwHVMMAFDk6mTWs"
  "+uEql+4c1LYQh8h4VEWOM1WVkf1bdwITu4Xq3wPF8Nr3H/cmSntBQqAj9l6QMSATH5H/4Z5XUxyx6xtEFIkKhTjL4o5JOuCwBhjL"
  "JZes/LUSaJ8po2u5cMnqJLOhArmPgDQwR8eL0LehpsM/WFErQVPE2nHkzoRyfKVOdPv9z20GTrxiYtD7b8AxYXjT/iQK3COAwIXf"
  "2jiU2kAPY+MD2Lt65/5aUpxcf/RRjMd0dLeG6oltv5IZRWSZf1q8ZeNgCjKo4spnd0PDWhQJbTJk2osossfhdZ7Zu+rkajvjDznu"
  "AwvJ8icBZi5h7MrKJ6+aVMRUvq5QNwHjdYoxHNoz0GiZXnvof/dah+mZ0RHaIBk+MKxpd0jup4hFNwz8dpOJaCCBaQOfGsHnYcT6"
  "P1Ru76bprbxPYEE67ZbvXX5DBCQgiigSgaaIHicyxECbMrocAL3JMgR2jJEV31oMLf+hkIiojsMrUoRaI43b02eWHxSFQnHylILN"
  "nELIYmpbz8o3HqQE4IR85wkSFADrUV22KVpwjolV2FmTArWC2f2/N8xdQCYtHF69mJjjOiGgrywK9PXPMtnhiBDzGaGuvAniTx9q"
  "MSUFGceYiuBF6N8/7MSm+3dPnwwx448YeLawoKBM3RQMPf3CJUtigIiNf55B74vJld2Wc1bKAms29FK5cso4nn165m0c3zuWNjmw"
  "N3TO6roV7dd2srW57Ovn2Di44lOnXRFzbEfteCW+MObIn17aVihpSyA7tvbMSwsui0bBn1fG8JsdSxZxbEc8DDy8lfI5F47jN3ef"
  "+/0Zx9dT3+onHErB+g1PlpfM2rTisq44qlBoPeGCCcckaap4smzZqpKajni4WXhWaRgPRgzgmbc8zeTFvUWaWpS0DYqN4Y2bY3j1"
  "lEB5ptAcdAg6SvB5sUVWeRuPDEP/imalkoc+jUge63/6gTmmOeRvnyaNdjGCx292huPT6T9sZWwla67bA52DE1BJw+bIo0BYBFbt"
  "jiU3pvaGOT4xYEBQ9XixJI0cd+CvfmZQApzLpUNyL6iImSrKOLUBf/LdFY8Rvw8c8JsXIHAKYIz3jFela86CCWJiRj+xVCzG5eB3"
  "M3D/PglcXmnzzgtHVRQQFIly9f/DojC8+5NY69UrQJgro/MEiHqKxqDDHgRFmDcgqFeAiKMNB17Pmfp6wtjOQTyjFb9nv2JUXUp9"
  "6x9YLDbSeEH0/Aagu4BQ31RnYhFnZJKU6GTMcF47bmDHK4MctphurzkqE3dxLBWYUKZvVx04hnpPsEq9M+ByxlSUSbM6mjsGvA1M"
  "g7GnGPYeyDmaKs35SV/aweYfc/NF6390mNHtN55M/f7f5USZWpK8EFqYfkvrM4/ARZdVQYd+vL/7La1k1sxk5a4Txph+/VQ1UfTY"
  "7w8nYQq8feaDvzoWwLlXtLPzv/tgCIjKRBpHjvDSSwvlTf/zMibMEzfGRdeHbPztvqNC6ebDPwVad+05k7Z3bOk1GTCh1blprcCM"
  "GkcxqwWdp1TZvx4WzQNkwuCzS1ohZswS0PjYzBYKk/+5gki5WFnXD3vrQB0TdJ09md9/ZH9fkB2VwBbquZ5+FnQOPd0/1B6zeUK1"
  "vt9DlMLChbCmmDBmoUcovwPIX9iFIdcFwmwNmH592y7mPbz031OA064tytZBIOXonnD9EGkSgDWM/quTN3KEuvLHF8iCry5jzEUX"
  "pmz76W5G+9abq3Dw0d8+wNHNLQqNKnRf3vPwBrP92kUbHgRSoNYCOsTYXW+cR3AGIP3g2RqAgbde7UZuKmWuxB8/uR6IzpiJyeqe"
  "WqmaUkj9GokSOH8WuqUM1Go9NMNg0UmojsM5eq3/k1y7U2kEFqZcBOs+vhRTajjmzwRv+O/P7iHO+yafJ0oQmN0dYpactP05uLn3"
  "UhzuaDuro7ZpKwU7ArpvIrUJBUyp4bjgi4ugnhuS6UOEjKtcrsw6lQjCJODgr3YhBGuB0KSYC97vCJyuIciVs0G9AN6DqrXgvQoY"
  "hGyn+ma5ua5kgMRA/sv1SBTAgQbkEVt/MyCBT4Mgu0vpIXY/ud3F5y1c2183IZVL5lvDaC2ojqQ7OXNJC86HsHIgZdJfbEfC3DP3"
  "thKQqM6+ZBLeCRipC2DlU4fmoggJQgyaeIAcwFrKl2YcsShIFppSloC1IKqAtagwL1SH/kGu2a7EymHTHCSwJEAEPlFEmbORxiiT"
  "vHzeWak2LbDkYlCyhEzD03pnJ7mGkCrM/BsHomBjgBimXdiNYzpJCnDPN3fMTfsphsjxyPwpqUXs38wCazisPPZSxWqfJiXJG8Ex"
  "AHr3xHHAYU81ejuy7/Qy2AltkKt6U4zYM4k52ndoCCy2TwpZG0UQ1gJGnNMG4nWUhaAUgwAtiBGnYrEFlDCM2wJrp0M56AiAl0A4"
  "uirjsVYlBPvW3GFsQKSgjxZQqjDCrc8YBBhhEzbqx7ABHJAz8yYIOgcbcRUaYioC1LGIGgCtYQTYwStbmtOmp9YymIKvHyoGJYE8"
  "81hzBgEigfhcwYhSiGxpBI4SAkSONmjGmhag5g+T3QAykEwl5u2Z9YLMUjIPZCbbBbaWILchHgVGSgSgCImpzXx35Y9+sO9v/j4Q"
  "xha8i4DcClgz82GNd6ocVgjbIEBMAJtlc4THW3jExbfHwM0jOM5oBZQjva9Pkf5XZ7zLM4BA0F1p90Rh7195Yt+uEkB7CKbYBkP7"
  "pKdNhO3e8H+wxQAy3NzwENsKo27Y+7drZ7Dl991fc8ti74N9Vy1h9z+0FBldDUEi4LVf5zefzNFsFv4vlC1g4OX/exfuat1mNGe0"
  "ZBCMGrFjAHjxxXfhVAoYtNDyoK3bHex7sfleH8rJQyNk3Y5s0hK4PwgMWjBNlV9rLTeGRm2tgdvbG7F6h596Nnp/s0LYtYyrK4Iv"
  "RtMY9qTgDvzRr71BdYda3BLhGZChFrdEWJgo6olTLUMbYpf/wW+8Sdg1stsyMtQhaZnO6E2/838uZJDnU2DZSmiFllDqxC0hCf1r"
  "vz5z16idOyBZ9lXLKfD4eufbgJFRKUXN7/kP8aZ7My3g1kFEdcta5tw7lKJJ6yAjdRZWDTIfwdgiinKkIopyWEFUAXEEVgQTjBlG"
  "YTAmgCCEZoz+EhgZVB3WgoqiIDIGypgqPP/sqEAAEwQYePw5azi8SGBSFjyrP60EQUschsHo0BGI84dBQRilKON1LjzggGMaZiiX"
  "K7kbBYHhsM5z5C+9+e6bGb8CqmP9f12OzfFt1TN2OI6jW53WcgTHe6miYvOEE+cNPN8Mij5PRtnQ5gmzTsk29CqoNY28ck7r9le9"
  "hiSpPatj8ybCSjmAs245C8JysWh9na5TW1DffL7fLmo9IDXBaxuYN8MGuRUOrhmGE082CIdWDUhJcjGNjJNPFhWWBBCUClA8ZUKQ"
  "rd0NxCTAzFMCNfQCpZCuq6+dTFAO6FnYeHZk5umQG0Nt3T6YsqAI0ly7i2KQe5npzXMCTNSAN75pw0f3UE0THYWNEljyrt6vPZ8b"
  "dQVyJr111v/8NHcVUqq3z37291ApAV98+YtAMbBFD7PfOl1NmP1q/dTbOmsr8bjAfd/lE7eKNgqWF7++Gd70hhBh41dWUbR1EzTh"
  "+rMBfnQClKoWplw70x16dA2QMnrRO8sgr50KRTj3j49dCUW4+vrBnx9ccjWMhBGvf/txuO5d3SD93/odcVx3aGKzLBDlEzs/fceB"
  "Dz2xMxeZ0GkYOVCPbFfXVYt3uCaR8XWCaVde01JtQNqU6ScGTOidEpaKpemXv6gvXj69ULDUqE698U6AlmrvLMa54lPBZ85nzJ1f"
  "XU71fbcDDH7pt7tqYK2ZNMeCwLY3zi0SmQmdJ1iYoPugvtNOLRBecT5A+sUzKti5n1b92kkh4Ul3UeTgRMZO77oP3vBuRn//J3v7"
  "wGhOVpsgtaW/vPGcyTy7/KdbiW6/qcSan62x8RW3LmL3ASAEpr358pbmLqBJ540tyjnXv3NCVJz3qaU1rS39+OyiARb/y3mM+RcX"
  "HhwPj/lF1bH8S3sIz5w0ijWr7n4SxEy/qruf0flzP1wIcvNF+z1wzYXw+L3hHeci8xkdbbj/DKb+YJ3qxnvmMveezVTvmPn6Ydi4"
  "GebPGWPruvsehChnsw2bdH3hzeTGbP38b2rmo58SnvvUUqIzbyfvndJe90qxeNGds/zuuHOkGVQWdKPZ5MUPzoIzlqqmqn+cB7ZY"
  "veqv/L7hYrE1mF0aOWBvB/rdW9BaggwEJWR0rrisbPIvfa/R8Cw+HZIszr1q3wc6I969EGpBuGAu/GdSOPsm8Lni07L6d0/4m17N"
  "cx15Q9cbRjTPL+0iA0GxBsB5NClZ/vuLe+thtg2BjqAunPW3K361tSlQtCBFYM4l4RNrPOedtxfyjotPXbpy6nVZSh5AKc0Z6GC0"
  "PQTtd3zzZX3pbTe/8XtNPfDNT7/z+1/0vn7zF34RPuaroKlgFkbIfktw9YeuLEF0C5go0HHbB09l+AUwAeCGjAIBqEj8+h994JeQ"
  "Lvzin3/E59E8sFQ1yY7bEc57961duRb6FkO+CuGILVyx7a0j2/o66U3AN8IoOPFM89zGnLPOhkbQc87MJ9b1XAoJFeitIp07i4TQ"
  "nH5Ayz9W1f86GRY+nd9TgOu+vTL+1g/Du3zwh1IItvqexR+8qgz+JRgOA/gm575lvuzm3TnA/RFcV5xCjkcuO2HO227ryv3B7Oh2"
  "X61LYMIIexsJqQdcbgOYNFSHagBpYIgLjbAFUmtdPhJ1XBquagZBnp94fvPPvT9Xrf/pnWfDTR+4FFh4B/1l4P9uhyo0yZ5QyyRf"
  "9zAjBNqpCMCnntYyCVECc4J5bw7mJFhM3T1AZqGrQHdlzFLn3DuUIsBZAieWQNpD9QjWQJ+ltRATGsAGAL0VYMRViXLwzSgf6iJy"
  "2GCAE64ppVkuGpx4QfP/bblLNRs+8PN5UKgCFw8QTwPP34HZ7jsDBxxIPZATExlGGkSCRAdg0fulGINnxMUGMexJwN5jVqxP/cW3"
  "nRdBIIzt8zQGkiwKxKtLEgYKBSPGQCotUyBFlLgwdWDHbQ9uVdW+L952wVlzq6XCdQXieAO6Z3PalJasvH95HXKzrFnN2bCBkwLE"
  "7YzWDDD2GAS49VK1i9NUy6ZfPNxvJfczAdL1j81SYVzGinNgreKcRDb3hJp5I2DI6i0ICJB39088/b9UdXDTuheXvb0ayrUG93so"
  "RZt6sx+5sfRzfxyBPFdIEIWBGOiO4CgaxNQgds3mfhvw3DceOhiYzv6GmFngwRgDqgAKIEBUAeYVgy3YggMCzWoFYwDUNSzwd0+8"
  "rmN+FbgpABsQe44D2ZaN+3LwrBWGmoeeKtSBqcsJ7LhW2toJaCHsfnZXYvB+qsJhJYgg9+AdlrEDILhu0es1IACsRV2ej7KRGwJm"
  "XfvjsT4K3Do5o4WJGS0rFLRJ40YEszZUw1F166VqrxwdURGUMxqSwaxYcRHktSaHEsBE1cPCUF0r1XlAc9BFXVBPbTkyMYRAobs+"
  "2IALPzWvNaLePW//wMi4kwXDw1RaRIMxQA9jwM6aclIE9X17BgE1oLLKcxIWQmGzgfrevbXYYgoc24Bt9x+4/BorkB2CpKEAHUcg"
  "E7b9ou+q6yJg458al5wLQ/RXIg7bc3nXvWuAcy76h3kUrvvu/zxw8K193Cssf7L1ylkmPzSGS1M3hgSay/UfndIC++7+3CNAHmiu"
  "doXH0+jJUe4Kq7/29c3A0ADIsbDsum/bJyoAhZ6I1jYB715/A+gJu+7b8YkIL7L9ycbi06BV23rVJYSgOnVR92fvFnHu/C+GMFdn"
  "m/q4D73ACys7LutB2qJAICjEdixLWL0aWqD3Fz95BnCYiPFqOA6aaJ7menS23nf38sxRmRyIHgto7nUhkAVT79hC4QwDO5av/Rug"
  "Ac29LgSvNhtCC3DOotprvU9tw8OcC9qZ8Kfl1tb6Zt4B+cb1a13LYScLDlGbA6XL3ndFCcqTAWW8Ibg+hgHP0cwR6r/71u/q0EOr"
  "DJik9vCPX+Kst17XkWuJMxQm7zCAY8rfOEQNbP33lSegA4XJOw0EELUOR8D559XdK8u24GDe5W24xIN6sZA8fNdQNuF2JwFtw217"
  "IyrXfvzqMuggIOPKIeiSKiBHxR2Gf/6Fnw/DWGKVgK6TWPHt5zjvfbd25b6UXWwBpZ74+Z8uPM1gigAeRrbXAWwo9cTP//SM02O0"
  "aFOgA6j3MnqoK8xdmTEV3N4DEAd4xsIrEHQE2//oF0pcaRPY89B/bxBLmgcMrdyYu/lD4ONyqELArieHzwSas8H9L/7wj7+qgGx3"
  "bXcGKdYpRK1htrVfo3JPBNJOqBBW6svuetu/liWJgRwIqswawnJ92V1veFMrKVgLjSLYYm1UpY7VWMZoFqAM5Ak2YLaV052PpUuA"
  "gRx2PfCD1WPAwMM/g7+pQZqkTiGQ7ffsfBswZo7w+Me/90dfjgGkQkUAr0Mha2ZUCwrDHuxd5oOiP7R5ay4kNUW0CGFbcWzMBkV/"
  "aPNrOXgBgXqzGEXlfJQdQXzOaAEotdcyn+wf+5H+HTM0HR500Nz//G6E3EPjlR2wKQHvVQGh/9mRrUDihPEv/vmPHiMwLaUWw67e"
  "SdRRIKsP54wTVlA4IGIiAACwawCdASroAGAAPj0YiUMiIaEZOnbwIAPEsYBnrgd2b7mvQecrbf895Q+4/rnypOkfOf/tfV9+lfYL"
  "54/mH/bn1Xv9x+4fvA9Ar9nPWY9Vf+7f9r2Ff2S9OT9z/g6/uX/X9IX/xdYBwl/8581vcx9r/GvzF/D/j/7h/aP8Z/of7h+z3wRf"
  "1HeL5g/z3929RP439mPwf97/bT+7/vF8cf53wV/Kf1H/O/3j8gPkC/HP5b/iP7H+5f+M+GH3D/gd0BtX+X/33qC+2H1j/Zf4D94/"
  "9d6Vn+B6Lfmn9q/4HuB/yX+ef6z+6/u7/lv//9af6z/Vf0Dzh/wP+u/Yj4Bv6h/gv93/ov8T/1/8R9J381/3P9F/sf3D94X5p/gf"
  "+X/jv9J+1v2F/y3+l/6v+9/5f/1f5P///+H7t/Z9+0Psf/rJ9+zyLDsuglzDuwdT9Ehd0cMPjajv2xkVAKMH5CQQNN+vAevj/Bdl"
  "fywcD6rf8ejkGVQpw88XsSEGOhz1GeIXvvuSYcJ5fI9O6ilW5SORuqPCDF7+3z2ahoycFLEDoLjhtpyhXfjrVMBE/yF3RoGref1P"
  "clIMwzwz0ot6ghupsRobeI/pqwhL7eRh/iNanUGfMtnNuwBz6u73mQtbHSg36dUWS19aJzVbcxnDu5uc3I9NjCA8Em7Dqv/Qjtpl"
  "Mn9AGjA18Zo4cPYk5ewTZ9piw7bJAn7rWxNuaNVMDd4Kp1mTbo38ZtJXZAQC254BPdzCVhW6Gj0TK3aaRckuk8npH+PLLM53xoJ9"
  "tlL7Gkl6ff+7m0ItNbrA1TAU1ZzeZk5RoYFlZoVRxJxN0rFIZ8oHvS3jFrbXn1BIhrdKtkz2otfyxROTaQq1ip72LG3EvWx7mADg"
  "V+b+ctlgLkHs0oJrqdvXu/WtudnK1NBHvWxNfGCR/nFfAFxZdHMUN5SDCqkLWKNhxJGa85M27Z1GeOZKMpc98ZvBwh6pIzSKDuPL"
  "+xpRp7q9Q3nH8lJFUT8G0OqHS9ju4wu6Wz/TEPwe6Z8TDyWsFSxF5HMGtMjK6Ghv+vdiGSB1kpNIIXYbrCtys+pAru1fiWESwUzo"
  "1O1umw69/oyljH/pzjg8mcl8LfMgzIud+9fABXs5wmez4/vyVGTIvy43hGqvFNTgIy1cXozzbtSvdBVs1JAA/v9gGL4mpC7YuFsc"
  "Rvj8iIq8hpWxHXyz5HTejLfxEvhjmRARVGWT7b14mPIR2HimonjcrR8pTWS6AT+KQE+UU4HBN6GHykiR7lFyds+0ZMPFtjktSHUO"
  "cB3mauUqTsFfculgYFSyTiOtOXjDzmCWTmer+QnLArWxVC2U8y8w9BBOOMjn64BhT6DBa4049TWk3os/KsQB1DbmVWIEkW0wAehi"
  "TRI9ov7thlLolGytd526ykf0oTUvkP5uRjDG4M3OB0lGlxIp9sJlmo6iD5TVDVBIKhjxY/O34OQVFa8Slgt1wuqJMSLSJDWvAVuh"
  "7Z9E2yAmLIiuHg/JD1/CKD7tGSneO/2IXntNyS+zEDA0M/8atmYwxb1JdN2Freh21TswffoSvgBFfAbdkn16oxnauU8O/kOk3Cba"
  "FzMA9xImMEavSLvnX6O/+aDtyq/fvVjmCkg0q2sLKVI3uiMF96Cfjbh2nkZM4HXsjgebXwyEvAcx3endgBpcM/Lb5dSzEA2/cuZL"
  "elxFq/rt3MsqAaDo57k3AEfoKrCb195odTOk8Z6lTm47+3SbsRrH1Fib9kcBsh+xg6l6V32ZwuX/n9JiBdy854mBj+8U2MZMoES5"
  "6frioZR1C+SWGsDKjq/dNPciOAxMpXYGXmFJ0+3LoEbaje/64oPW8QjJTLJiUx2KRUaMv+t+xW5l+3NbwyuLiV0Dr3ivyDni8OKI"
  "ssQZ8RjjmFhCVfpjjZqkyAR/lvYBquvCyqM0xk0vUR9diQKOnKC1nGyRs3MotYG0quQRVORQs+KaZTd2bo9cBvDNdgGKCsw81yO6"
  "kFJMEFO8t+P64Ey1T2lrnq4h3DEnS30B+fFD4xML22yvQ6ODWTshGSYVbndTzndgtNDvFOoQ2Lf9M2D0/HO8oByQsg5fHTMJIrQI"
  "aHm4LxdMmrK6vKI66sjG9i1FwKkxP9Fk5sWznebwux0037SnWSmVisutZIP0VqufYtlsYu5zdXAAJtAyM31VgGsY20sgmI/EvD3Y"
  "ANfUGmTW+tRV4SG2maYJz8NBS2XNrmFbeTZCDzvvq8WZRMxTv/V6XuB3ZlH2j5DCUElYZs2WHQdTlnzxbFkOQEDPMQUu0ZAkfqo6"
  "kkpbMusVNABhPVtqJAQDb2RKu8xiE8d656Cs5bglfB7xfUX/LFg7E7K6LppAkHCxB2UEBvt0Om35OaaEpQlCbowuwkX3b6459PAV"
  "jCgqtVWzvluZMCn2sGyPda8km8xE8CBPAI5oHMGhsIYvsSzooZ6HtcYb9PEDfcVlABQMgLrKuPk6dp2EHCTM3GShZuO64PdypqR9"
  "p6n+GWF+FA5+bzl8hvmzMkZE/3EpaPrFcn6OAOwYVRtUr5Ze40YgL7i34OcMGsR8P0/LnIKF0Ikgixz+y2NfJ546pFPDl4d8J3KU"
  "SHJsvBg5OFL7p7wT5nQk+SN33lyvT1LTJk8nPFwGxNhtG6hNKwG9PAzQRVFyGgy5Yv+0qt8Z+rkrJ3cbi6Kjg5j4clUiyuSf/znF"
  "ReXTOIKvWRJdq2QUCRar4k8XVIR1EezR7RiwdSVD8ELscOP+PAhP+FgXR1FWlJC43jqGcTkaFyv133sPu4C4FS2cy3uPY7WmTjfu"
  "17zE8KgUdauWJMvpGwiBKQbzq+m8Vvmz7IAD7aCLNL79HLp0dtJrRNPEskrkY4ERqRP1AJZLBnxznDT2Jn8MiZZLpJRagJEFHzuO"
  "cwUQdGmk+IrNnfX/gInA4bJn8O2cQ9AUq9zjbtE7fQpIs38E5LSlBWx5oCynWJk4tczKk6ndISP7sD40SekMBT4ASe/730ulJNrw"
  "Gse8ZJEZR4JIJE9R/7yvortxacF0zGAO+8/CBQQnXdzlHJ0CxPKxiDJL5YD1tF9+12739/aHQjcfjKsAIgrkRBnfsZM7g3B4/HTL"
  "Er6VmSmzcLJoMKEsv2TVO/4fVh9CKYqqSaMC4mVHWHLqPBwCkFgYz53YxywmdieyXBhteCoVJdrMhEdJh3YMDDGEz5AmGefSDD7f"
  "dm1w53njGg+ylnh2lANtG1KEG4ownUPaSVWbAkIHYVW4f2lBL/S7mqW9awCy/1fisXu1wlCfV5+Glm6DRF45ntfo2/tGeWncHGdS"
  "G1cBFkUGztBT+4gFnhngCKb2PQ1x1SNOAh5b4irTXez4oLCoKa+BmPGoyO2rhpeoPkC/MlddD5skUq3KrIBrcRdnIZ61JAnHdbjS"
  "hqQDExra4jluBCx6YKdAuoKvOsyGM388nmcw94cIJulGMusK7UNWS8XHC8qNi9m2yw/UFvoF8mZlVznC/3bFI1EF51XoUE1vrlhf"
  "zwLGkVunVj8gVkR1ZpzATEiyvhhQCEjT+lSOu2psZ2fobxj6zjR/q77rf0xHYaBbr4eTanT/y2fMxc72u/nof2n9KaxSiwXBt0Co"
  "GA7fa0R+sTUfCUGay7kVn/PwqiwLvVSk0Jmflr3nES4VfBEOmv3hwKz6b3x9MPhQQl9BByDNfGvUV7xNUCLSJeGkmMRPg11k4TzV"
  "GLd9hJ2Cyi4hEEZPcf8bKqPIi/9L02ZY41R4mXEjjmJ3SBqikv8xLK3T4s+XE6ckZXL1YD5jMUKUPfyS8swjGAWf9j2Il99Vi94w"
  "1tq78y6TFawfbKWJmk92ytK5dPGf/hKCn2/P7tW2mNhbbAuB+MysF6cHFYiNIDCeML73L/6Lfx7NpDiAQzodTs9aqpXaiYUJU3MQ"
  "Qo6EYrND48btdfeipyigIaFgjHhmRAzST04YXm8lmhHQ0xOey3Ljb9ql1GNmPhdpt9G18x3Tj8aHcvlc7iguMADLSPfTJ+MtxjSF"
  "4CiMRi11+0b/PEfyP1Pzcq5JVnOd1H826ilzlqC2AeqwcJ0sIKHll35TE+s21JfLyzP7DrIKvz/KW69y/sLGqAaqL7ATvVVHAugK"
  "DtZHyKCzzEzBODKtrOjOjpxeQvOfVqqD71lX7NRdvgd9/EFAKk9C/Apx4OlV6UyE9chAUxnSbs3t1zYXD52XWfXI6bjeFEXGgxRU"
  "OffZyeZlC9pKsD2o5ZjTk3PNH16GNUJDuQoHoly7tNybvD/m6hqUidntOnGQ7lmQDNGeKO1KutFZExRWmvaMoXQhe2J8GKAjfkkY"
  "h8ItZx7Qe8uRCtp9qyR5ZlWY3DdoBVMY2nH3cVCXPDZ2hvQJp2fozkroKOibaLGbPKIixoefNIarHxFTdgzKvHriNR/1mb86Ry3s"
  "Kq71hBng/RSZxeomaZvOQFYXpHvSex7MTP3v0WYFh0cLXHXawGjxJcYJfPEYvm6ARXDErOEDQtTpIpPTbSwjC4wCQpVT8BJ2YYZ9"
  "w1Vr4UzhNP+ck4quQrfd45ypoz5608uxFd5ykeKiy/DQTeOiiV5y28gTdVc+suwdhKvGewc8fi2p504jpKVbOdrfHJZ9eyMJp/1f"
  "0cEGmTEtUujhq3OoAKMusMpLGZWDFVG+JlszVSVSMjkMlyaBLGbfCn84P4YxpsEO4aPBaksLRnuG5Eo+D/VDIXTHyS+U9Kl8pwd6"
  "HnF79KMvH/KQuydg9yBzpgXrmSFI/H4+thMnEDg8IF4+tCe8t53AUpM2l5EK6UCpovZHYDCTLncNXjrFHIChqyx5e5WR5GJNPE4O"
  "AA3P53ckEf9aiDwI2dn9iFSbEWPd1fVzAcUIzH9kcw03PWe28kc0NDaHJogmE5QfyaI4Wzv932jGrdXcfi1q3RIsYB2lrE11Jr2b"
  "xEU9ADSUnDsfFjd7WiWiCTDUgvkNLoTopaY2Ikj6Bu+vKarwGxzfnGwwDcEu4u65WWdTI4q3hpPxC819haCWQCzuS/8nwWq37Ssj"
  "IZiGP3dhfkCC88CCxR8cDRu3BNI28Uutqhe6EhICRoSyem5XQsOh3h8ikdw538V4fvokTRRnjg+AMbIY6pcRZJMyQQT29t261Vr3"
  "cLCSMfmdwT9LKxishgUQFa3cExMZDVO1GA+Ap5bCECnmwLdsE7/I6VgO3nZm6OjhKWShdChf64/VS7N4xfjf1+WJ8NlmWRhwSVho"
  "EPHngl9BOvfhSS5ulKDVldXLS6oRxiNZz2dUw1sJm9dpWLrqLJWdumUJu4dlW8PKfqHrhae/pNrn8wzZaxI8OLvQVhdsyFEzpDYU"
  "YISM3KxoZgARGY5fz/y0/3hjujzmZE499Yur9nkFGNJtNeg14IZxdQBHOKlR36DMpb3FtOvq01FHubGvKHQD0MDdJGrZi2hsUnMT"
  "W2mbYu0qxQbZgesFvwVFDCPwx7bak4b/jNogXUYvbq4WUkzkaxA2/+TaBNBt6SFiw4K6sxn2csGh44f0/QYp5ARs4vo3iCRsbLAa"
  "MDabQd0H4Anvqzd6N+7nLcNqsBjxmmka8AmAJkhijksXmnjW2tB/8TNsdX4jel5xT61ey5UHkURH68Oi9z2W0dRIXQcPsYhDdwIO"
  "VumndoXhxKXgPa7JZz0DEwrSvQI6VScev5a33IRcN1O0TkZ0xFMrNNMgQkc6JfrWIg0M9phRiGSczzFqA2mNXTGQOVFeuymbpOmN"
  "Zi3oxIGyQZxT2fPsUkVa4gKPvpQQ1m9DTBttkjsJuiYInzcBlDKSwbffO7kO7hCgQmxvsE1QiQNZVm52xXonCdhCj99VAMv/bOd9"
  "nzHPlXpjH7Rdvkv9o6VOQhIWUxB9hctRpV75qOZETPhhurqZ60HLAKkp5ueJnj7p3P/mbVWHj07uyLhlUlbYybYyACuiHV9QDWIU"
  "pO66R6HsbA99WnXoYwETnOT5gM1+IWNYB3TpFc3nzcbawqxTfwMBoopyv6pgJrH3r3VkMHGGA+W/fnapO2rPzGSJnCm6FMZeAd/T"
  "/vkINmvmLkezFSq9RICx6YovZdx52TkqgvnAAw5gFjr/Kbcp2BL2acY3BTiBZG68BrDtaiZ0G4YviKUSPaV8ydnyUlL++R2yc8+4"
  "tQ1bTS9mvWR8o3Y/47VZIN95B5GlyfCqlc1X1GuOL9jqN8GZSIGbwVTh8D+ZLwsxrDqYy2qRUQASj0cqm+mo05F1xo/s5Yg0Gu0+"
  "YSL55FZubFUNfP4ZkFJfok5Pg31uERj9brGoIl59Daw8m9vUKBW912n/0apYpOKI0aRVw2ZTq/KiY7YXSzcz5tvoT/UXa1ujIL1A"
  "X73azyX0XBGP8a1qCWsOcP81M/ZwMbAcTmwPORLslmv8dnizKhLc0rYUcJOkpq5Q08cogyScSUUu/jDd/uimuyfFf3lWb3gGu+ON"
  "GerZlgEC97dMkIp8AllNcUBEqQUDNzdq9l9E5ViCOD8Zn70jyLk4VnEIMFL6rQpnLfPngenp/f8MVW+d/r/3pPnWBRXrTbkzcyWu"
  "GU4+mb1zTpK3+5gkn/n28EBjfKtNDA+q3AK8HH1rrjsVyOzh5tDMs5LhHqvF5MmU6Xt765IM0qpelUmYLQu5jsl9mUiZ5H/wpNEz"
  "Fzs+EUmaqZVp9lY3LPLLd0jHsKch4rnPPh3IHndqeQLvOJHst3fFlD/D8k1wGkgNoOiXTswWcMZpYk9JsPBnVIP5rgOEB2x2pej4"
  "G4eagX9acmUGjYYejFvpSfD8H2ZY4OZyebyj31XlrFEHV3Plx0zNk3arrT2Up2+v3rFlMk09A14ynOTaWwsEkEj+FVnAE/bjkTEx"
  "RcdzllkA11DbfhhZqIDN8BzOqigRjdJHhyywisH+SYI4N0cYzt9+T4M+aJPpYLhpUu04YqNZnlVGZuEdabL7NmeFFxJimpXc7Oth"
  "tjAZIw69bMfcM1ghj+PrkeccaIi15a0Irb40AeuOlr0nCNNGgJfxHE7GHxEDLIGAIYY0ATcjJBHsqAoLU+b1RbeeJ0bZXaECPue5"
  "lqwFtp49CSmm85SNErQHYgRoANMmj30hyrSNBDb40eYf6WkhSJhAMBoVI4E8nI54FB3i1cUFP2GhezxfJvHA6OtC/dYStqv5nmKQ"
  "EQUt8mEl6tXLCwLnymTjAYfbRsAfRw5p6iRsoXZv7z2guD1v2wcWK2EcskkmIeafugLbT/Ght4e7I4W1l1CeSH/AcgcqCxDoFu1m"
  "OZZwmzv7POEGH5iqLqs8jbDyopv5j0QCTwRvIL8uH0a3XMIG8kp/tcdH7IJfeeeIb2Ype1GEfautGyWWxuhB+p9PcInHNgjCxA8x"
  "u9Ydr6Loy3r39S2lun5I2sIbIzIIPFytjk+Gyz4e0b6XQzckoNgJeRjbNp3+kouk5ybKmaU54kEaslrb/uJjcAeomPHU0+REseK3"
  "0ipU53bB9uK2BDOJBLWlRQ9AmR4w+e6HZgJsNkgu4K2o1Le/Yvss1tP/MgAsWjt+Xza/zXFtrS3lz+KT5hSRRkh06P06xjpbcUxx"
  "pgQvjo1NA4PVZrkppjQD0GMojT6T70bnaOwj2oXhdYlQkkMNw53LfZgVMmLNFYquxUuRkDOhLAUt4cdsrslRZvajDItYxM/9TB6s"
  "ixtV23zO54PMP3ZHlxoVvwkfdMchw/kZzkyuDse8OcSa+A1Nerw4t9r8e+krkNNm70nmaaXkej3eDPzOU0+f8Xpg0S1KdofKPgMv"
  "1i5X5jL41zhy2mYJenUeub2a2DV32JFw58LiLkB+asqAYkCGhFNTyfyqhcwzIFWxduTnnxga//vj4eyR0+APpK1+SNmYUohDVfXg"
  "O8A5j4SV7P+t6HxteKMLMyCz/kKZ0BQkgyKkJvEIbRYTkQxyDby9PnMc41EKKDfaN9jhfsLBYhZqZB/1E+1zqRA/P00uqJ+BsQUi"
  "5/8q+oJUe+LMTve3HO1kYwRaqiuKv1Ill/bzq1jfAVTqMMEZr8Eun4hf5R2ROTTmTOabnJJYntiN6ojjTLAaRdOrI+QB+YxckzqM"
  "KPAV3bhTN/KbqNHqBKYKQVA5U9fHuLIsLUdSTVs3DENilSst1iLJ9Z++j1j3PWWQbfU+AzYU7MMWN2WCKOnme1YXPDwZaO6YvFfe"
  "oQZRZTzXAYC0fZ901gUnHhQJR+R8aUo3LbaKMM+PPrjtXnYOQSuxmwKeyDpVfVAeqapmq+u9ynB2ZVtH0/juU7dJOy7GPdHLqJEa"
  "d0ZVd+lhKIrjfdm32/T8EWAiub1BzXIFLVlcYuNjFAiAnN68bAApzUiA0JJEhG9Na0u5XsRycRVDLUVfU9/tvX85gbbxtzEcBxbV"
  "67sEQjucfh2VyTu0asjqOTn605v38neOWst7J10p62DKa9A3Biw0Uf0VPBa37quNgNNc/nT01eAfoQetrpqwfQKH9/pBrrUf10rg"
  "nJbENhmGmE66qZx7kIknf583KGCqYD3Ob5gcb7jZJbBhAA5fGxUVwM/ZVQwsfqkAVeo3zaces2ki7VNFbzSeq8ZjCVFKN54tr5YJ"
  "m3WGq6nctmL/Y6Y+FWFEcAmFmXlZMSU24NWLPme8aeIang14oubgD3KEo8J9Tc0rt0Xy9hf99iwJ+bGiK+/78MB55/Zk3WBXq9Wu"
  "coGi55HBqALnD5Eo+7k397P1w7xcZUK42uNA4iDtpZt435plgias2AkSSB43R+Jz2zJqzcU71d6uAPmuxVv7AWhy0jVWXb0674nL"
  "bnbxJpCceMqyppY6P+vnCwyxg4KZ0J4VdAfXeh+h8t7XhvAf500PmEyXIo5d+lTVbqSUAiYqMrl8c5ktkwIXfgcachbKUOwS6fV4"
  "wujXhFB7MSroJ33pZaoIERQs7tQSxj5tJ7xN9P9ujB/kdSlD/63TOoI0ZfMJsTB88ResLJWX88kfxC5jRgW5x8cEDRV4ouXP4zol"
  "2eZ3aZrbwSmqQv0WIbuV3EnaPMdooa8Rejns7sVcIp9TAHe5viE/PQZxQd7nOu9gkgXtu1KpXu1RmhzmkyNEgLpgfwUUFSpyOyNH"
  "+Fx7EV4QlhAVqscmKox0NY/UQbJduXQavhnFqoEihi8ELfICm3Nj783ev3t5qSqPtLn4BTvPRD4UiokHTAvLso4MpijKr93k/1iY"
  "uLS/UyE1GI+MVOnK1VrU9I5yJOAQwqOhfpa5nzdSGd6EYBftY+edoK/PlEYO57DOZo0rvosIVJHKRi6LZ6Urd0J8slB2OOAmhnCK"
  "dehLzojqGkXAp2znwRziRo8EMAtxDjX1MiitgXVB7UvzVFqk+AAkWUQKGCAbPYt9/Y6Mt5ooZI8FSmCZ4oSYQVyTENrXYE5XzXnk"
  "dE4dobgheKHUMZPxftHsdw8HbTp2qzP5nsYPaTN/a4dOPqKv+ZdvwwE7RmKgc+ST41cWyIFFuibdTgkumQOh91JFg4nd3nQRr4+k"
  "NDoAJFRIYmzA0KrpGTBtvMRAWP9PqmauVvGdRjqpPzIr9++1nb1B6yfEujjxGfbDPn+ugGb+bmteiaNzViRIoSMyNLrtbUO4nChX"
  "f76f12KyH/D9LiS5rexmeL2NWQDtM6C94C9NSoqlRkdU+M+hk/RyrvjwQVQPOLIiSehRa6GZ/Jm5KJJhN2K1ldojfWf68sgljATY"
  "gu6GGD6ID7a7QH/DM6+bGyx2Zq/bRVV3WUmmnnlqpL2I9wukYpA6PrkkrNp3fAG0coOY4Zhz71vQ1RqS/9pcndPIwnyUxHluSt7z"
  "msdCCx9386EZeYzOCw4dMUiB9mg3xW3Y7jgCSSa2hZk/cLASjKbPVd8KtSSnx/1VkmHRXDIztHxfWQpzU3JAyAmpCyGJEYJYOzHt"
  "B1NKnSIYWLzZwhJkFxhJmePcG32SwkkDwvghRWCJrqdSzKKWP6hxqeXqLCYyFYMzL6wbZzhzocOXLrq1tFgNy2zfPuz3PMyu/FAD"
  "5jrva5SpG8xUDyXqG3xZOm1HR31n0ISkSG0PpT2jdu5Nycm8szER/XpC7QKDpceayVNmNg/+X8UA4/I3aXh3GmtpvkoU1pIE0jeC"
  "jxCNH1d/WmPrR6Bq36pP2rMsahvBj2XP24EO+i3Z+NnU3xLxXWN0sLafQhiG438s/S8ZhGPWYDSaIBzjZrwWdkq7/d+R/3P0ruvB"
  "TKShVpFzLfvY/j1QC8rvUrP6qxfdXH78NVM+USf2dKLHyCrMHFVPwnTq2ZDuiGB3qbckP9QwCaKNeDib/4VbSF4raa6NliGizraH"
  "cVr/aL0P06e4/oX5w+z4q/8ZhmwvKzLnoNXavcgDS12qFvs8pJDfLu9WQcLX1FkmmszD0dHQDpY2ofH1B0OY/JBc6SZhWe/DnH5R"
  "bSEIuNxVP1IsBm/LetGB2pKNMz/smb9YWQr8dTH2BWiTrNCE9lNJ744vQ1UThv1MeK5jFg1D7nXmDY2KiDk2coll3UkgE/rk0i7t"
  "28auvPJa3TIDDtmFXrHlEYvDKP6tlLIEAOj7exKQu/C7uudQhg12ogbk5dv+pHoMtgTXAAqqlY4xuCbpkJFMjJrNk0cjReOEnVSV"
  "GkYBLQA2P+/KoCa1B84O0GX525QxyV2Ld4qLJ6feDS9JbsaPmxWXrpeHHH+YdmzspRwNZgJ/DuMOVd1pkuQPUls/Lv8wlJ+qNP/y"
  "SlvR9ysgTAteL7XkCEib3wWJUcfG252ObEDCVspqh0XJb8oefL6CFBLel0jbGk2zIziEHz2ggbCotq6oLbgIM3O6XaKae/ZzXRMR"
  "jU8cr+x3amJ0k55QBKNhBbmYsDbempwU53rIhVFtWxocPqYcgwiloO9iDai4NwhyWN1d7OfxxS0eYS+cATBLbjH4Pn7lK+IUDApk"
  "6qdQLXOJpFv0IasJHDpcTznjy9xE9XfeBmr2mwOssNXNJayzJPK/q0ZnuwZmvexmeAKcTK42c8YyrQ+v38YpPfbrGPB282Pmrf8+"
  "+knBRMdLOPy1ugQOrHYbQw/cU8Z9iIpjnaVRz2uGWLU4FyWxdDxwGPI4abkePQzzlDFQWGxbVQpPr6XXsRwjxwsLGnE9XmunkcpJ"
  "4LT+6pwnp+aA27TNviIJzM5jfsyVRAHi6lkPOPA3GT8e8iB0IlvOoUL6mQwzyuq2VY1AtEXSXZSJ6yhiwFN7xKt4iTOWZMuXgjMz"
  "i7LOFUCsS8w2S8/9YYQekxE4KTGUaSeX6a6UOKYBLBav0BeQT+36j6mmIpG/Ju6JBC5/TUJy1Rs08MZw+NmQvJ165Yy5SpHR04k+"
  "CO95zVeBtjcUrv8Poag70odjMpLo1sVOqeqogn91dZ20v6ma1S/hMRmiDiIwl4yslInaWiH+BlHWxoyKkyzkrJgnFUFsCw0n1Znk"
  "cbz5PZsxUYpyRN2iOcFOROyUTOiLo0vNycgOgHBc5sEK9rlA3exntMviV4wiJFX9b5cC0kqxLBvsNJWV/+IB2cUCJ1wyGs+fWT0n"
  "EHOzi33LCvjTrjB3diZ3EFDLHIjaRlWIP/Svrd6IgXqMGgWXagN/bDNzsha83U2MihI/PHK95mNbpn4eAC9HP72r0ZPJSqm805HQ"
  "s+IuL/R++ArwHyA4pzeMcQbEkp2R/se5zMt3+fj6EfsBuix4odz6QTtRMXioHRHSeTq0MNBI/NGFO3cLx4nSk4NKBjKX7X9RrL3B"
  "++8EwaVCJDbIvJUFfisLXZckCK5GfhzIrlvNTrZHvBafB1JVhWQYo9t4YYWuMxdWeScxkQptRAiTQlNyN46rJv0GxNbgLKK2ixH5"
  "81Flie0dnDl0R/ihrweXyy9WgRANHnA0Md0lHjcB948+pFp9KOQC9qYAAAA="
 ),
 "badge-csse.webp": (
  "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"
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
/* Credential row.
   Sized per badge rather than uniformly: the RE/MAX, Wainwright and NRBA
   lockups carry fine secondary type ("SELECT", "New Jersey | New York",
   "National REO Brokers Association") that needs real height to stay readable,
   while the CSSE badge is a single large wordmark at a 5.7:1 ratio -- matching
   its height to theirs would make it twice as wide as anything else and swamp
   the row. Held at 36px, its letterforms are already the same optical size. */
/* The agent column is 1.1fr in styles.css, which leaves the badges cramped.
   Widened here so they get a full row each instead of wrapping awkwardly. */
@media(min-width:901px){.footer-top{grid-template-columns:1.45fr 2fr;}}
.f-badges{display:flex;gap:26px 30px;flex-wrap:wrap;align-items:center;margin-top:24px;}
.f-badges img{height:54px;width:auto;max-width:100%;object-fit:contain;
  background:none;padding:0;border-radius:0;opacity:1;}
.f-badges img.badge-wordmark{height:40px;}
@media(max-width:900px){
  .f-badges{gap:18px 20px;}
  .f-badges img{height:40px;}
  .f-badges img.badge-wordmark{height:30px;}
}
.f-qr{margin-top:28px;}
.f-qr-label{font-size:13px;color:var(--gold,#e1c281);letter-spacing:.6px;
  text-transform:uppercase;margin-bottom:8px;}
.f-qr .qr{width:120px;height:120px;border-radius:8px;overflow:hidden;display:block;
  line-height:0;background:none;}
.f-qr .qr svg,.f-qr .qr img{width:100%;height:100%;display:block;}
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
