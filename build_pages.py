# -*- coding: utf-8 -*-
"""Page bodies for the Wainwright static site. Called by build.py with its globals."""

def run(g):
    page = g["page"]; IMG = g["IMG"]; AGENT = g["AGENT"]
    search_widget = g["search_widget"]
    RES = g["RESIDENTIAL_CARDS"]; COM = g["COMMERCIAL_CARDS"]; PH = g["PLACEHOLDER"]

    # --- Live listing data pulled from Ruuster (Morris Agent Team / RE/MAX Select, GSMLS via Ruuster) ---
    # Order: Dave's own listings first, then the team's. (Dave has no active listings at capture time,
    # so this is the team's current active inventory in his market.)
    PHOTO_BASE = "/assets/img/listings/"
    DAVE_LISTINGS = []  # David P Wainwright — no active listings at capture time
    TEAM_LISTINGS = [
        # id, addr1, addr2, price, beds, baths, sqft, lotAcres, type, statusLabel, photoFile
        ("f9deef2b-d411-4dc8-a870-282d863bdc94", "7 Melissa Dr", "Denville, NJ 07834", 1199900, 4, 3, None, 0.71, "Residential", "Active", "12ed99a2-d496-40b8-9e48-bfdaefcada6c.jpeg"),
        ("ca4aada4-c02e-4553-8013-27da1ba5deb8", "72B Hook Mountain Rd", "Montville, NJ 07045", 1875000, 4, 5, None, 6.02, "Residential", "Price Change", "016ff727-3303-4027-8074-fe5d5c41419e.jpeg"),
        ("954b13ae-4ebc-42c4-b772-94f9d6017fa3", "156 Kingsland Rd", "Boonton, NJ 07005", 1133350, 4, 3, 4500, 1.58, "Residential", "Active", "0f504cc3-3cda-4cac-b604-0d21b0eba263.jpeg"),
        ("f011a3eb-3e3d-4fd4-995c-e5f6e6cd1f0d", "4 Unneberg Ave", "Roxbury, NJ 07876", 799000, 4, 3, None, 0.98, "Residential", "Price Change", "d5b342d4-c799-474f-98a7-b4387a97a559.jpeg"),
        ("049632af-bfb0-4407-862d-0ed2adc3b7b9", "68 Sowers Dr", "Mount Olive, NJ 07840", 540000, 3, 3, None, 0.2, "Residential", "New", "26a14e23-1b2b-4a54-ade2-7e86ec8ef54a.jpeg"),
        ("db84fbc6-a9b4-4cb0-8427-5d411e828cda", "381 Drakestown Rd", "Washington, NJ 07853", 499900, 4, 3, None, 5.25, "Residential", "New", "4c081ed6-ec25-4dd0-8a37-3f3dbd3c4a97.jpeg"),
        ("185b927e-944f-43d2-9ac3-9c431aff489f", "149 Roessler St", "Boonton, NJ 07005", 499000, 3, 1, None, 0.14, "Residential", "Active", "78598330-5293-45b4-9099-6a3e9bef8629.jpeg"),
        ("36fbca1c-58a4-4439-a818-22c66f59878b", "6 N Mount Olive Rd", "Mount Olive, NJ 07828", 485000, 4, 2, None, 0.12, "Residential", "New", "4b2b66af-ad9b-4080-86b8-296aaf1d5c58.jpeg"),
        ("fd4faf24-6be9-4a27-ba3a-8282782f209e", "903A Green Pond Rd", "Rockaway, NJ 07866", 339900, 1, 1, None, 0.28, "Residential", "New", "b0f7371c-50df-44a3-9e27-ee09cc5e9b21.jpeg"),
        ("4c9d2475-8b2f-49b9-80b9-02e000f76a9c", "680 State Route 15 #26", "Jefferson, NJ 07849", 225000, 1, 1, None, 0.02, "Residential", "New", "cffc982f-e201-4bf8-b83c-5d241b93a3be.jpeg"),
    ]
    ALL_LISTINGS = DAVE_LISTINGS + TEAM_LISTINGS

    def money(p):
        return "${:,}".format(int(p))

    def carousel_card(L):
        lid, a1, a2, price, beds, baths, sqft, lot, ptype, label, photo = L
        photo_url = PHOTO_BASE + lid + "/" + photo
        size = ("%s SqFt" % format(int(sqft), ",")) if sqft else (("%s ac lot" % lot) if lot else "")
        badge = "For Sale" if label == "Active" else label
        facts = '<span><b>%s</b> Beds</span><span><b>%s</b> Baths</span>' % (beds, baths)
        if size:
            facts += '<span><b>%s</b></span>' % size
        return """<a class="lc-card" href="/contact" title="Contact Dave about %(a1)s">
      <div class="lc-photo" style="background-image:url('%(photo)s')"><span class="lc-badge">%(badge)s</span></div>
      <div class="lc-body">
        <div class="lc-price">%(price)s</div>
        <div class="lc-facts">%(facts)s</div>
        <div class="lc-addr">%(a1)s</div>
        <div class="lc-sub">%(a2)s</div>
      </div>
    </a>""" % {"a1": a1, "a2": a2, "photo": photo_url, "badge": badge, "price": money(price), "facts": facts}

    def listing_carousel(data):
        cards = "\n".join(carousel_card(L) for L in data)
        return """<div class="listing-carousel">
  <button class="lc-arrow lc-prev" aria-label="Previous">&#8249;</button>
  <div class="lc-track">
    %s
  </div>
  <button class="lc-arrow lc-next" aria-label="Next">&#8250;</button>
</div>""" % cards

    def listing_grid(data):
        return '<div class="lc-grid">%s</div>' % "\n".join(carousel_card(L) for L in data)

    CAROUSEL = listing_carousel(ALL_LISTINGS)

    # --- Fello home-value lead widget (David Wainwright Jr / Morris Agent Team) ---
    FELLO_SCRIPT = '<script src="https://widget.hifello.com/search-widget.js" async defer></script>'
    FELLO_WIDGET = '<fello-search-widget widget-id="65e6de7958d5ea002da97bb8"></fello-search-widget>'
    def fello_section(heading, sub):
        return """<section class="section band"><div class="container center">
  <h2 class="section-title" style="text-align:center">%s</h2>
  <p class="lead" style="margin:0 auto 26px;max-width:700px">%s</p>
  <div class="fello-embed">%s</div>
</div></section>""" % (heading, sub, FELLO_WIDGET)

    # --- Ruuster IDX search embeds -------------------------------------------
    # RUUSTER_BASE is the team's consumer portal. Two embeds are built from it:
    #   * "my listings"  -- filtered to David P Wainwright  (MLS ID 234919)
    #   * "team search"  -- the unfiltered NJ/NY MLS search, kept as the fallback
    #
    # DAVE_SLUG is the only thing that needs filling in. Ruuster's public embed
    # keys off the agent slug, not the MLS ID, so the MLS ID is carried alongside
    # for display/attribution only. Until the slug is confirmed, DAVE_SLUG stays
    # empty and the page degrades to the team search alone -- an empty filtered
    # iframe would look broken, which is worse than not showing the section.
    RUUSTER_BASE = "https://morrisagentteam.ruuster.com/listings"
    DAVE_SLUG = ""          # e.g. "david-wainwright" — confirm in the Ruuster portal
    DAVE_MLS_ID = "234919"
    TEAM_SLUG = "glen-baker"

    def ruuster_embed(slug, title, extra=""):
        src = "%s?slug=%s&status=Active%s" % (RUUSTER_BASE, slug, extra)
        return ('<div class="ruuster-embed"><iframe src="%s" title="%s" '
                'loading="lazy"></iframe></div>' % (src, title))

    RUUSTER_MINE = (ruuster_embed(DAVE_SLUG, "David Wainwright Jr — My Active Listings")
                    if DAVE_SLUG else "")
    RUUSTER_SEARCH = ruuster_embed(TEAM_SLUG, "Search Listings — Morris Agent Team, RE/MAX Select")

    # ---------------- HOME ----------------
    home = """
<section class="hero">
  <video autoplay muted loop playsinline poster="%(work_bg)s">
    <source src="%(hero_video)s" type="video/mp4">
  </video>
  <div class="hero-content">
    <h1>David Wainwright Jr &mdash; Morris County Commercial &amp; REO Properties Specialist &mdash; Representing NJ &amp; NY</h1>
    <p class="sub">Expert Commercial Real Estate and REO property services in Morris County, New Jersey. David Wainwright Jr delivers proven results in foreclosed homes, office buildings, and investment properties across Morris and Sussex counties.</p>
  </div>
</section>
<div class="container">%(search)s</div>

%(fello)s

<section class="section band">
  <div class="container">
    <h2 class="section-title">Why Consider David Wainwright Jr. as Your NJ Real Estate Resource</h2>
    <p class="lead">David delivers expert real estate services across Chatham, Denville, Parsippany, and surrounding NJ communities. Specializing in residential sales, market analysis, and investment properties with deep local knowledge and proven results. Whether buying your first home, selling, or building your property portfolio, trust Morris County&rsquo;s market expert for personalized guidance and exceptional service.</p>
    <p class="lead">If you are considering NJ for your next home, or need help selling your existing New Jersey home or commercial property, David Wainwright Jr. is here for you.</p>
    <div class="cols-3">
      <div class="col"><h3>Residential Excellence</h3><p>David delivers personalized residential sales expertise throughout Morris County. From established neighborhoods to exciting new home sales in growing communities, he guides clients through every step of the home buying and selling process with local market knowledge and proven negotiation skills.</p></div>
      <div class="col"><h3>Commercial Solutions</h3><p>David brings sophisticated expertise across Morris County&rsquo;s diverse commercial landscape. Combined with comprehensive property management services, he helps clients maximize their real estate investments through strategic acquisitions, professional tenant relations, and portfolio optimization for long-term success.</p></div>
      <div class="col"><h3>Estate Services</h3><p>David specializes in estate settlements, working with families and legal professionals to handle property transfers, probate sales, and inheritance matters with care and efficiency, ensuring smooth transitions during challenging times.</p></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <h2 class="section-title">Listings</h2>
    <p class="lead">Current listings from David Wainwright Jr and the Morris Agent Team at RE/MAX Select.</p>
    %(carousel)s
    <div class="center"><a class="more-link" href="/listing">View All Listings</a></div>
  </div>
</section>

<section class="section band-2">
  <div class="container">
    <h2 class="section-title">Market Insights</h2>
    <div class="post-feature">
      <a class="thumb" href="/blog/somerset-county-market-update" style="background-image:url('%(b_somerset)s')"></a>
      <div class="body">
        <div class="date">July 23, 2026</div>
        <h3>Somerset County Market Update</h3>
        <p>Somerset County had a strong month. In May 2026, 357 homes went under contract across the county, up sharply from 250 in May 2025. That is a real increase in buyer activity, and it bucks the trend we are seeing in a lot of other New Jersey counties this spring&hellip;</p>
        <a class="btn btn-dark" href="/blog/somerset-county-market-update">View More</a>
      </div>
    </div>
    <div class="center"><a class="more-link" href="/blog">More</a></div>
  </div>
</section>

<section class="section">
  <div class="container">
    <h2 class="section-title">Commercial Listings</h2>
    <p class="lead">Beyond residential excellence, David brings sophisticated commercial real estate expertise to Morris County&rsquo;s business community. From office buildings and retail spaces to industrial properties and investment opportunities, he applies the same local market knowledge and client-focused approach that makes him a trusted residential advisor. Whether you&rsquo;re expanding your business, diversifying your investment portfolio, or exploring commercial opportunities, David&rsquo;s comprehensive understanding of Morris County&rsquo;s commercial landscape delivers results for investors and business owners alike.</p>
    <div class="center" style="margin-top:26px"><a class="btn btn-gold btn-lg" href="/contact">Ask Dave About Commercial &amp; REO Opportunities</a></div>
  </div>
</section>

<section class="work" style="background-image:url('%(work_bg)s')">
  <div class="container">
    <div class="box">
      <h2>WORK WITH US</h2>
      <p>Contact Dave Wainwright directly today to get started on your real estate journey with a Residential, Rural, Commercial and REO Expert.</p>
      <a class="btn btn-dark btn-lg" href="/contact">Contact Dave</a>
    </div>
  </div>
</section>
""" % {"work_bg": IMG["work_bg"], "hero_video": IMG["hero_video"], "search": search_widget(),
       "valuation_bg": IMG["valuation_bg"], "carousel": CAROUSEL,
       "fello": fello_section("What&rsquo;s Your Home Worth?", "Get David Wainwright Jr&rsquo;s free, no-obligation home value report &mdash; an instant estimate powered by live market data."),
       "b_somerset": IMG["b_somerset"]}
    page("", "David Wainwright Jr Real Estate | RE/MAX Select — Commercial & REO in NJ & NY",
         "Commercial real estate and REO property specialist David Wainwright Jr, RE/MAX Select, serving Morris, Sussex and Warren counties in NJ and NY.",
         home, akey="home", extra_head=FELLO_SCRIPT)

    # ---------------- Simple page-head helper ----------------
    def head_block(title, sub=""):
        s = '<p>%s</p>' % sub if sub else ''
        return '<section class="page-head"><div class="container"><h1>%s</h1>%s</div></section>' % (title, s)

    # ---------------- BUY / LISTINGS ----------------
    # "My Listings" leads the page. Source of truth, in order of preference:
    #   1. a Ruuster embed filtered to Dave's slug (live, self-updating)
    #   2. the hand-captured DAVE_LISTINGS carousel
    #   3. nothing -- fall straight through to the team search
    if RUUSTER_MINE:
        mine_block = """
<section class="section" style="padding-top:40px"><div class="container">
<h2 class="section-title">My Listings</h2>
<p class="lead">Active listings represented by David Wainwright Jr &mdash; MLS ID %(mls)s.</p>
%(embed)s
</div></section>""" % {"mls": DAVE_MLS_ID, "embed": RUUSTER_MINE}
    elif DAVE_LISTINGS:
        mine_block = """
<section class="section" style="padding-top:40px"><div class="container">
<h2 class="section-title">My Listings</h2>
<p class="lead">Active listings represented by David Wainwright Jr &mdash; MLS ID %(mls)s.</p>
%(cards)s
</div></section>""" % {"mls": DAVE_MLS_ID, "cards": listing_grid(DAVE_LISTINGS)}
    else:
        mine_block = ""

    listings_body = head_block("Search Listings in NJ &amp; NY", "Search every active MLS listing across New Jersey and New York &mdash; powered by Morris Agent Team, RE/MAX Select.") + mine_block + """
<section class="section%(band)s" style="padding-top:40px"><div class="container">
<h2 class="section-title">Search All NJ &amp; NY Listings</h2>
%(ruuster)s
</div></section>
<section class="section band"><div class="container">
<h2 class="section-title">Featured Team Listings</h2>
%(carousel)s
</div></section>""" % {"ruuster": RUUSTER_SEARCH, "carousel": listing_carousel(TEAM_LISTINGS),
                       "band": " band" if mine_block else ""}
    page("listing", "Buy — Listings | David Wainwright Jr, RE/MAX Select",
         "Browse residential and commercial real estate listings across NJ & NY with David Wainwright Jr.",
         listings_body, akey="buy")

    featured_body = head_block("Featured Listings") + """
<section class="section"><div class="container">
%(carousel)s
</div></section>""" % {"carousel": listing_carousel(ALL_LISTINGS)}
    page("featured-listing", "Featured Listings | David Wainwright Jr, RE/MAX Select",
         "Featured residential and commercial listings from David Wainwright Jr, RE/MAX Select.",
         featured_body, akey="buy")

    SOLD_CSS = """<style>
.sc-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(320px,1fr));gap:18px;margin-top:22px;}
.sc-card{border:1px solid var(--line,#e6e6e6);border-radius:10px;background:#fff;overflow:hidden;
  transition:box-shadow .2s ease,transform .2s ease;}
.sc-body{padding:18px 20px;}
.sc-photo{height:172px;background-size:cover;background-position:center;background-color:#ececec;}
.sc-has-photo .sc-body{padding-top:16px;}
.sc-card:hover{box-shadow:0 8px 24px rgba(0,0,0,.08);transform:translateY(-2px);}
.sc-price{font-size:22px;font-weight:700;color:#111;letter-spacing:-.3px;}
.sc-addr{margin-top:6px;font-weight:600;color:#222;}
.sc-sub{color:#666;font-size:14px;margin-top:2px;}
.sc-meta{display:flex;flex-wrap:wrap;gap:8px;margin-top:12px;}
.sc-meta span{font-size:11.5px;letter-spacing:.5px;text-transform:uppercase;padding:4px 9px;
  border-radius:999px;background:#f2f2f2;color:#555;}
.sc-meta .sc-side{background:#efe2c6;color:#6b4d16;}
.sc-meta .sc-src{background:#e9eef7;color:#2c4a7c;}
.sc-stats{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:22px;text-align:center;}
.sc-stat-n{font-size:42px;font-weight:800;color:var(--bronze,#af7b34);letter-spacing:-1px;line-height:1;}
.sc-stat-l{margin-top:8px;font-size:14px;color:#555;}
.sc-meta .sc-pending{background:#fdf0d5;color:#8a5b00;}
/* .search-widget carries margin-top:-64px so it tucks under the hero on the
   homepage. Mid-page (commercial) that yanks it up over the paragraph above,
   so the wrapper cancels it here. */
.mid-search .search-widget{margin-top:28px;}
.sc-thumbs{display:flex;gap:3px;}
.sc-thumbs span{flex:1;height:56px;background-size:cover;background-position:center;background-color:#ececec;}
.sc-specs{display:flex;flex-wrap:wrap;gap:8px;margin-top:10px;}
.sc-specs span{font-size:12px;font-weight:600;padding:4px 10px;border-radius:6px;
  background:#f4f0e6;color:#6b4d16;letter-spacing:.2px;}
.sc-specs .sc-sqft{background:#eef1f4;color:#33475b;}
.sc-desc{margin-top:12px;font-size:14px;color:#444;line-height:1.6;}
.sc-desc p{margin:0 0 9px;}
.sc-desc p:last-child{margin-bottom:0;}
.sc-note{margin-top:11px;font-size:13.5px;color:#555;line-height:1.45;}
</style>"""

    # --- Closed transactions -------------------------------------------------
    # Populate SOLD from a GSMLS closed-transaction export. Until it has rows the
    # page shows an honest empty state -- it must never fall back to the sample
    # cards, which are other brokerages' ACTIVE listings and were being presented
    # here as Dave's closed business.
    #
    # Rows come from site/_data/sold.json when that file exists, so the list can
    # be edited in the CMS at /admin/ without touching this file. Anything in
    # SOLD_INLINE below is appended -- useful for one-offs.
    #
    # Deliberately NOT tied to an MLS feed: much of this work never appears in
    # GSMLS at all. Commercial deals live in LoopNet/CoStar, and off-market and
    # REO dispositions are often never listed publicly. A curated list is the
    # only source that can represent the whole book of business.
    #
    # Row shape (all keys optional except addr1 and category):
    #   status    : "closed" (default) | "under_contract" | "loi" | "active"
    #               "loi" = letter of intent signed, no executed PSA yet. Kept
    #               distinct from under_contract on purpose -- an LOI is
    #               non-binding, and advertising it as a contract discourages
    #               backup interest on a deal that can still fall apart.
    #   category  : "reo" | "commercial" | "residential"   -- drives grouping
    #   addr1     : street address            addr2 : city, state ZIP
    #   price     : number, or omit to withhold the figure
    #   close_date: "Mar 2026", or omit
    #   side      : "Listed" | "Sold" | "Both"
    #   source    : "GSMLS" | "LoopNet" | "CoStar" | "Off-market"
    #   note      : short free-text line, e.g. "16-unit stabilized building"
    #   prop_type : specific asset type -- "Industrial", "Office", "Retail",
    #               "Mixed-Use", "Multi-Family", "Land", "Warehouse / Flex",
    #               "Single Family", "Condo". Shown as a chip.
    #   sqft      : building size, number. Rendered with thousands separators.
    #   description : full paragraph(s). Line breaks become paragraphs.
    #   photos    : list of image paths. First is the hero, the rest render as
    #               a thumbnail strip. Legacy single "photo" key still works.
    #
    # NOTE: this list is for transactions Dave REPRESENTED -- listed, sold, or
    # under contract. BPO assignments do NOT belong here. A BPO is confidential
    # work product for the ordering servicer, and publishing the address would
    # disclose that a specific property is in distress. BPO volume is shown as
    # an aggregate count in CREDENTIAL_STATS below instead.
    SOLD_INLINE = [
        # Seed data so the pages are correct immediately. Once these are entered
        # in the CMS they are superseded automatically (see _load_sold) and can
        # be deleted from here.
        {"status": "under_contract", "category": "commercial",
         "addr1": "415 Totowa Rd", "addr2": "Totowa, NJ 07512",
         "side": "Listed", "source": "GSMLS",
         "note": "Commercial office building."},
        # LOI signed, no executed PSA -- deliberately NOT under_contract.
        {"status": "loi", "category": "commercial",
         "addr1": "285 Route 46", "addr2": "Dover, NJ 07801",
         "side": "Listed", "source": "LoopNet",
         "note": "Industrial building."},
    ]

    # Aggregate credibility figures. Addresses never appear here -- these are
    # counts Dave can stand behind publicly. Set a value to None to hide that
    # tile. Update the numbers as they grow.
    CREDENTIAL_STATS = [
        # (number, label)
        ("4,000+", "BPOs completed for national servicers"),
        ("1,000+", "REO assets managed to disposition"),
        ("30+",    "Years licensed in New Jersey"),
    ]
    # The years tile says New Jersey specifically, not "NJ & NY". Dave has been
    # licensed in NJ for 30+ years but in NY only about a year -- a combined
    # "30+ years in NJ & NY" would overstate the New York tenure.

    def _load_sold():
        import json, os
        path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            "site", "_data", "sold.json")
        rows = []
        if os.path.exists(path):
            try:
                with open(path, encoding="utf-8") as fh:
                    data = json.load(fh)
                rows = data.get("transactions", data) if isinstance(data, dict) else data
            except Exception as exc:            # never let bad data break the build
                print("WARNING: could not read sold.json (%s) -- skipping" % exc)
                rows = []
        # JSON (CMS-managed) wins over SOLD_INLINE for the same address, so a
        # property seeded in code here disappears cleanly the moment Dave adds
        # it in the CMS -- no duplicate cards during the handover.
        merged, seen = [], set()
        for r in list(rows) + list(SOLD_INLINE):
            if not r.get("addr1"):
                continue
            key = " ".join(str(r["addr1"]).lower().split())
            if key in seen:
                continue
            seen.add(key)
            merged.append(r)
        return merged

    SOLD = _load_sold()

    SOLD_GROUPS = [
        ("reo",         "REO &amp; Foreclosure",
         "Bank-owned and distressed assets taken from assignment through closing."),
        ("commercial",  "Commercial &amp; Multi-Family",
         "Investment, mixed-use and multi-family transactions."),
        ("residential", "Residential",
         "Single-family and condo closings across NJ and NY."),
    ]

    def sold_card(row):
        import html as _h
        esc = lambda v: _h.escape(str(v)) if v else ""
        price = row.get("price")
        bits = []
        if row.get("close_date"):
            bits.append('<span class="sc-date">%s</span>' % esc(row["close_date"]))
        _chip = {"under_contract": "Under Contract",
                 "loi": "LOI Signed",
                 "active": "On Market"}.get(row.get("status"))
        if _chip:
            bits.append('<span class="sc-pending">%s</span>' % _chip)
        if row.get("side"):
            bits.append('<span class="sc-side">%s</span>' % esc(row["side"]))
        if row.get("source") and row["source"] != "GSMLS":
            # Worth surfacing: it signals reach beyond the residential MLS.
            bits.append('<span class="sc-src">%s</span>' % esc(row["source"]))
        meta = '<div class="sc-meta">%s</div>' % "".join(bits) if bits else ""

        specs = []
        if row.get("prop_type"):
            specs.append('<span class="sc-type">%s</span>' % esc(row["prop_type"]))
        if row.get("sqft"):
            try:
                specs.append('<span class="sc-sqft">%s SF</span>'
                             % format(int(row["sqft"]), ","))
            except (TypeError, ValueError):
                pass
        specs_html = '<div class="sc-specs">%s</div>' % "".join(specs) if specs else ""

        desc = ""
        if row.get("description"):
            paras = [q.strip() for q in str(row["description"]).split("\n") if q.strip()]
            desc = '<div class="sc-desc">%s</div>' % "".join(
                "<p>%s</p>" % esc(q) for q in paras)
        # photos: accept a list, or a single legacy "photo" key
        shots = row.get("photos") or ([row["photo"]] if row.get("photo") else [])
        shots = [s for s in shots if s]
        photo = ""
        if shots:
            photo = ('<div class="sc-photo" style="background-image:url(\'%s\')"></div>'
                     % esc(shots[0]))
            if len(shots) > 1:
                photo += '<div class="sc-thumbs">%s</div>' % "".join(
                    '<span style="background-image:url(\'%s\')"></span>' % esc(s)
                    for s in shots[1:5])
        return """<article class="sc-card%(pcls)s">
      %(photo)s
      <div class="sc-body">
      <div class="sc-price">%(price)s</div>
      <div class="sc-addr">%(a1)s</div>
      <div class="sc-sub">%(a2)s</div>
      %(specs)s
      %(meta)s
      %(note)s
      %(desc)s
      </div>
    </article>""" % {
            "photo": photo, "pcls": " sc-has-photo" if photo else "",
            "specs": specs_html, "desc": desc,
            "price": (money(price) if price else {
                          "under_contract": "Under Contract",
                          "loi": "Letter of Intent",
                          "active": "For Sale",
                      }.get(row.get("status"), "Closed")),
            "a1": esc(row.get("addr1")), "a2": esc(row.get("addr2")), "meta": meta,
            "note": '<div class="sc-note">%s</div>' % esc(row["note"]) if row.get("note") else "",
        }

    def stats_block():
        tiles = [(n, l) for n, l in CREDENTIAL_STATS if n]
        if not tiles:
            return ""
        return """<section class="section band"><div class="container">
<div class="sc-stats">%s</div>
</div></section>""" % "".join(
            '<div class="sc-stat"><div class="sc-stat-n">%s</div>'
            '<div class="sc-stat-l">%s</div></div>' % (n, l) for n, l in tiles)

    def sold_sections():
        """Closed transactions, grouped by asset type. Under-contract deals get
        their own section below -- they are real work but they are not sales,
        and listing them as sold would be inaccurate."""
        out = []
        closed = [r for r in SOLD if r.get("status", "closed") == "closed"]
        pending = [r for r in SOLD
                   if r.get("status") in ("under_contract", "loi", "active")]

        for key, title, blurb in SOLD_GROUPS:
            rows = [r for r in closed if r.get("category") == key]
            if not rows:
                continue
            out.append("""<section class="section"><div class="container">
<h2 class="section-title">%s</h2>
<p class="lead">%s</p>
<div class="sc-grid">%s</div>
</div></section>""" % (title, blurb, "\n".join(sold_card(r) for r in rows)))

        if pending:
            out.append("""<section class="section band"><div class="container">
<h2 class="section-title">Currently In Play</h2>
<p class="lead">Active listings and deals working toward closing.</p>
<div class="sc-grid">%s</div>
</div></section>""" % "\n".join(sold_card(r) for r in pending))

        out.append(stats_block())
        return "\n".join(x for x in out if x)

    SOLD_EMPTY = """<section class="section"><div class="container">
<div class="prose" style="max-width:760px">
<p>David&rsquo;s closed transactions span bank-owned and foreclosure assets, commercial and
multi-family investments, and residential sales across New Jersey and New York.</p>
<p>A full transaction history &mdash; including REO dispositions handled from initial
assignment through closing &mdash; is available on request.</p>
<p><a class="btn btn-gold" href="/contact">Request the transaction history</a></p>
</div>
</div></section>"""

    sold_body = head_block(
        "Sold Listings",
        "Closed transactions represented by David Wainwright Jr &mdash; REO, commercial and residential."
    ) + (sold_sections() if SOLD else (SOLD_EMPTY + stats_block()))

    def commercial_closed_block():
        """Commercial content for /commercial, drawn from the same list.

        Split in two: what is available or working right now, and what has
        already closed. A buyer wants the first; a prospective seller judging
        whether to hire Dave wants the second."""
        rows = [r for r in SOLD if r.get("category") == "commercial"]
        current = [r for r in rows if r.get("status") in ("active", "loi", "under_contract")]
        closed = [r for r in rows if r.get("status", "closed") == "closed"]
        out = []
        if current:
            out.append("""<div style="margin-top:38px">
<h2 class="section-title">Current Commercial Listings</h2>
<p class="lead">Available now, under agreement, or in negotiation.</p>
<div class="sc-grid">%s</div>
</div>""" % "\n".join(sold_card(r) for r in current))
        if closed:
            out.append("""<div style="margin-top:38px">
<h2 class="section-title">Recent Commercial Transactions</h2>
<div class="sc-grid">%s</div>
</div>""" % "\n".join(sold_card(r) for r in closed))
        return "\n".join(out)
    page("sold-listing", "Sold Listings | David Wainwright Jr, RE/MAX Select",
         "Recently sold homes and commercial properties represented by David Wainwright Jr.",
         sold_body, akey="buy", extra_head=SOLD_CSS)

    # ---------------- CALCULATORS (visual placeholders) ----------------
    def calc_page(slug, title, headline, rows, result_label, result_val, akey):
        rowhtml = "".join(
            '<div class="row"><label>%s</label><input type="text" value="%s"></div>' % (l, v)
            for l, v in rows)
        body = head_block(headline) + """
<section class="section"><div class="container">
<div class="calc-mock">
  %(rows)s
  <div class="result"><div>%(rl)s</div><div class="big">%(rv)s</div></div>
</div>
<div class="placeholder-note" style="max-width:720px;margin:24px auto 0"><strong>Visual placeholder.</strong> This mirrors the original calculator layout. The estimate shown is illustrative &mdash; wire up a calculator script or an IDX/mortgage widget to make it interactive.</div>
</div></section>""" % {"rows": rowhtml, "rl": result_label, "rv": result_val}
        page(slug, title, headline + " — David Wainwright Jr, RE/MAX Select", body, akey=akey)

    calc_page("calculate-mortgage", "Mortgage Calculator | RE/MAX Select", "Mortgage Calculator",
              [("Home Price", "$650,000"), ("Down Payment", "$130,000 (20%)"),
               ("Interest Rate", "6.5%"), ("Loan Term", "30 years")],
              "Estimated Monthly Payment", "$3,286 / mo", "buy")
    calc_page("calculate-affordability", "Affordability Calculator | RE/MAX Select", "Affordability Calculator",
              [("Annual Income", "$150,000"), ("Monthly Debts", "$800"),
               ("Down Payment", "$80,000"), ("Interest Rate", "6.5%")],
              "Estimated Home You Can Afford", "$585,000", "buy")
    calc_page("home-sale-calculator", "Home Sale Calculator | RE/MAX Select", "Home Sale Calculator",
              [("Estimated Sale Price", "$700,000"), ("Mortgage Payoff", "$310,000"),
               ("Agent Commission", "5%"), ("Other Costs", "$8,000")],
              "Estimated Net Proceeds", "$347,000", "sell")

    # ---------------- SELL ----------------
    steps = [
        ("1", "Marketing Analysis &amp; Pricing", "We analyze comparable sales and current market conditions to price your home accurately and competitively."),
        ("2", "Home Preparation &amp; Staging", "Guidance on repairs, decluttering and staging to present your property at its very best."),
        ("3", "Marketing &amp; Showings", "Professional photography and a targeted, multi-channel marketing plan to maximize exposure and showings."),
        ("4", "Offers &amp; Negotiation", "Skilled negotiation to secure the strongest possible terms and price for your sale."),
        ("5", "Contract &amp; Paperwork", "We manage the contracts, disclosures and timelines so nothing falls through the cracks."),
        ("6", "Closing &amp; Beyond", "A smooth path to the closing table &mdash; and a trusted advisor long after."),
    ]
    stephtml = "".join('<div class="step"><div class="n">%s</div><h3>%s</h3><p>%s</p></div>' % s for s in steps)
    sell_body = head_block("Sell My Home", "We love working with sellers and look forward to sharing our home-selling plan with you!") + fello_section("What&rsquo;s Your Home Worth?", "Start with a free, instant home value estimate from David Wainwright Jr, then see our step-by-step plan to sell for top dollar.") + """
<section class="section"><div class="container">
<h2 class="section-title" style="text-align:center">Our Home-Selling Plan</h2>
<div class="steps">%(steps)s</div>
<div style="text-align:center;margin-top:44px"><a class="btn btn-gold btn-lg" href="/contact">Talk to Dave About Selling</a></div>
</div></section>""" % {"steps": stephtml}
    page("sell", "Sell Your Home with David Wainwright Jr — RE/MAX Select",
         "Find out what your home is worth with David Wainwright Jr's free home value tool, plus a proven six-step home-selling plan. RE/MAX Select.",
         sell_body, akey="sell", extra_head=FELLO_SCRIPT)

    # ---------------- REO OVERVIEW ----------------
    reo_services = [
        ("BPO Services &amp; Request", "/reo-services/bpo-services",
         "Wainwright Realty has vast experience completing accurate and timely BPO reports with professional, time/date-stamped photographs to document property condition. Our photography team captures the true picture of the asset &mdash; and great marketing photos should we take the assignment."),
        ("Initial Assignment", "/reo-services/initial-assignment",
         "Our REO Division understands how staying on top of timelines can make or break an assignment. Our detailed workflow and protocol keep us on schedule, with an on-time task rate of over 98%. David Wainwright has been a member of the NRBA since 2023."),
        ("Occupied Properties", "/reo-services/occupied-properties",
         "When people are still living on a property, many factors must be considered while completing tasks and serving the client. We are sensitive to these situations and create a smooth transition with dignity and close adherence to all regulations."),
        ("Property Preservation Services", "/reo-services/property-preservation-services",
         "Over the years we have built relationships with highly skilled, reputable resources who help us prepare properties from the day of assignment to the close of the transaction. They make us look good, which allows us to make you look good."),
        ("Preparing Assets for Listing", "/reo-services/preparing-assets-for-listing",
         "Foreclosures, HUD and REO properties require special care and skill to market. It starts with a detailed BPO and moves through every consideration &mdash; it&rsquo;s not your typical &ldquo;Zillow, MLS, open house, postcard&rdquo; situation. Each situation is unique."),
        ("Marketing Your Assets", "/reo-services/marketing-your-assets",
         "We are constantly reviewing our marketing tools and tech stack to give your property the most effective exposure. Based on each property&rsquo;s location, situation and best features, we target the venues best suited to the audience for your listing."),
        ("USDA &amp; Rural", "/reo-services/usda-and-rural",
         "With over 16 years of experience, we navigate the requirements specific to USDA and rural properties &mdash; servicing these assets in strict accordance with USDA/RD guidelines."),
    ]
    svchtml = "".join(
        '<div class="svc"><h3>%s</h3><p>%s</p><a href="%s">More details &rsaquo;</a></div>' % (t, d, h)
        for (t, h, d) in reo_services)
    reo_body = head_block("REO Process &amp; Services in NJ &amp; NY",
        "Full-service REO, BPO and default management for asset managers, servicers and investors across New Jersey and New York.") + """
%(stats)s
<section class="section"><div class="container">
<div class="svc-list">%(svc)s</div>
<div style="text-align:center;margin-top:44px"><a class="btn btn-gold btn-lg" href="/contact">Request REO Services</a></div>
</div></section>""" % {"svc": svchtml, "stats": stats_block()}
    page("reo-services", "REO Process & Services in NJ & NY | David Wainwright Jr",
         "REO, BPO, property preservation and default management services from David Wainwright Jr, NRBA member, RE/MAX Select.",
         reo_body, akey="reo", extra_head=SOLD_CSS)

    # ---------------- REO SUBPAGES ----------------
    def prose_page(slug, title, headline, blocks, akey="reo", cta="Request This Service"):
        parts = []
        for b in blocks:
            if b[0] == "h":
                parts.append("<h2>%s</h2>" % b[1])
            elif b[0] == "h3":
                parts.append("<h3>%s</h3>" % b[1])
            elif b[0] == "ul":
                parts.append("<ul>" + "".join("<li>%s</li>" % li for li in b[1]) + "</ul>")
            else:
                parts.append("<p>%s</p>" % b[1])
        body = g["header"] and (head_block(headline) + """
<section class="section"><div class="container tight"><div class="prose">%(p)s</div>
<div style="text-align:center;margin-top:40px"><a class="btn btn-gold btn-lg" href="/contact">%(cta)s</a></div>
</div></section>""" % {"p": "".join(parts), "cta": cta})
        page(slug, title, headline + " — David Wainwright Jr, RE/MAX Select REO Division", body, akey=akey)

    prose_page("reo-services/bpo-services", "Request BPO Services | Wainwright Realty REO", "Request BPO Services",
        [("p", "Dave Wainwright has vast experience completing accurate and timely BPO reports with professional, time/date-stamped photographs to document the property&rsquo;s condition. Our photography team takes quality photos to give you the true picture of the asset and good photos for marketing purposes in the event we end up with the assignment."),
         ("h3", "Turnaround Times"),
         ("ul", ["Drive-by BPO &mdash; within 48 hours", "Full Interior BPO &mdash; within 3 days"]),
         ("p", "Request a BPO from Wainwright Realty and receive a thorough, well-documented valuation you can rely on.")],
        cta="Request a BPO")

    prose_page("reo-services/initial-assignment", "Initial Assignment | Wainwright Realty REO", "Initial Assignment",
        [("p", "Wainwright Realty&rsquo;s REO Division team understands how staying on top of timelines can make or break an assignment. Our detailed workflow and protocol for these assets keep us on schedule with each task. We are proud to say that our on-time task rate is over 98%."),
         ("h3", "Occupancy Status"),
         ("p", "We inspect the property and submit an occupancy status report to our client within 24 hours of each assignment. We are sensitive to complying with the PTFA and all other local applicable laws. During the occupancy period, we perform no less than weekly drive-by inspections and make no material changes at the property. We also provide a drive-by BPO within two calendar days of the assignment, including several exterior photos of the subject property."),
         ("h3", "Vacant Property Registration"),
         ("p", "We complete the vacant property registration and work closely with our clients to confirm the proper registration documents have been filed with the appropriate municipality.")])

    prose_page("reo-services/occupied-properties", "Occupied Properties | Wainwright Realty REO", "Occupied Properties",
        [("p", "When people are still living on a property, we understand many factors must be considered when approaching them, while simultaneously completing tasks and serving the client. We are sensitive to all of these factors and look to create a smooth transition that includes dignity and close adherence to all regulations."),
         ("h3", "Relocation Assistance"),
         ("p", "We work directly with our clients to offer relocation assistance to occupants per their client&rsquo;s wishes. We request that occupants voluntarily vacate the property and then offer relocation assistance. The base starting amount is determined by investor guidelines, and we continue to offer relocation assistance until a lockout time is scheduled. Throughout the entire process, we comply with all PTFA (Protecting Tenants at Foreclosure Act) guidelines."),
         ("p", "On the date of vacancy, we inspect the property condition and coordinate lock changes so the property is left in broom-swept condition.")])

    prose_page("reo-services/property-preservation-services", "Property Preservation Services | Wainwright Realty REO", "Property Preservation Services",
        [("p", "Over the years, we have built relationships with highly skilled and reputable resources that have assisted us in preparing properties from the day of assignment to the close of the transaction. They make us look good, which allows us to make you look good!"),
         ("h3", "Initial Preservation and Maintenance"),
         ("p", "There are usually many people involved in reaching the same end goal. Sometimes our client&rsquo;s clients need to step back and let us do what we are fantastic at &mdash; preservation and maintenance. Using our procedures and network of vendors, we bring in the most reputable, reliable contractors for these tasks."),
         ("p", "Our preferred vendors bill according to HUD guidelines for routine property preservation. Larger repairs, such as boarding windows and door replacement, may require bids from several vendors to ensure fair, competitive pricing.")])

    prose_page("reo-services/preparing-assets-for-listing", "Preparing Assets for Listing | Wainwright Realty REO", "Preparing Assets for Listing",
        [("p", "Foreclosures, HUD, and REO properties require special care and skill to market. There are multiple tasks associated with each transaction. It&rsquo;s not your typical &ldquo;Zillow, MLS, open house, postcard&rdquo; situation &mdash; we treat each situation as unique for the best results."),
         ("h3", "Valuations / BPOs"),
         ("p", "BPO drive-bys are considered &ldquo;grunt work&rdquo; by many agents and brokers. Not us. We understand there are many steps to preparing a property, starting with the initial evaluation. We consider it our &ldquo;hello&rdquo; when building our relationship with you and everyone involved in the property transaction."),
         ("p", "We complete an interior BPO within three days of the assignment. If the property is occupied, out of respect for the occupants we complete an exterior BPO within the same three days. Our valuations include full exterior and interior inspections and photos, descriptions of the market area, and sales and listing comps with photos.")])

    prose_page("reo-services/marketing-your-assets", "Marketing Your Assets | Wainwright Realty REO", "Marketing Your Assets",
        [("p", "It doesn&rsquo;t do any good to prepare an asset to list if no one can find it or if it doesn&rsquo;t look appealing. We know you need it to move fast and efficiently, and that the asset needs the best exposure possible. Wainwright Realty is constantly reviewing our marketing tools to ensure we are giving your property the most effective exposure. Based on each property&rsquo;s location, situation, and best features, we decide which aspects to promote and where, targeting the venues best suited to the audience for your listing."),
         ("p", "Our REO division combines online, mail, open house, and print where it fits best, tapping into our extensive list of connections."),
         ("h3", "Listing the Property / Multiple MLS Coverage"),
         ("p", "Once we receive the approved list price from our client, the property is listed within one business day. A For Sale sign is posted on the property, and we advertise using methods customary in the marketplace, including multiple MLS coverage for maximum reach.")])

    prose_page("reo-services/usda-and-rural", "USDA & Rural Asset Management | Wainwright Realty REO", "USDA &amp; Rural Asset Management &mdash; Meeting All Requirements",
        [("p", "We offer various services to assist businesses, borrowers, and communities with their applications for funding or their existing loans and/or grants. The New Jersey USDA market has some nuances unique to our state."),
         ("p", "With over 16 years of experience, we are ready to tackle the challenges these properties can present to inexperienced real estate firms. Navigating the requirements specific to USDA and rural properties is something Wainwright Realty excels at, because we realize USDA/RD assets are different property types and must be serviced in accordance with USDA/RD guidelines."),
         ("p", "We understand that typically, for a period of six months following the foreclosure sale date, almost all activities of servicing the asset must be approved by the USDA/RD office. This is why we are so selective about the vendors we bring in on these assets &mdash; the relationship lasts longer, and it must be right.")])

    # ---------------- COMMERCIAL ----------------
    commercial_body = head_block("Search for Commercial Properties", "Commercial and mixed-use real estate expertise across New Jersey and New York.") + """
<section class="section"><div class="container">
<div class="prose" style="max-width:900px">
<p>We have years of experience representing buyers and sellers of commercial properties in New Jersey and New York. Many properties are mixed-use as well &mdash; we&rsquo;ll help you navigate the neighborhoods to find the best fit or the best buyer.</p>
<p>It&rsquo;s worth noting that small commercial properties often catch the eye of local investors rather than large national firms. That&rsquo;s where we shine! Need assistance with valuation or disposal of your commercial assets? Don&rsquo;t hesitate to reach out.</p>
</div>
<div class="mid-search">%(search)s</div>
%(closed)s
</div></section>""" % {"search": search_widget(), "closed": commercial_closed_block()}
    page("commercial", "Commercial Real Estate in NJ & NY | David Wainwright Jr, RE/MAX Select",
         "Commercial and mixed-use real estate services for buyers, sellers and investors in NJ & NY.",
         commercial_body, akey="commercial", extra_head=SOLD_CSS)

    # ---------------- BLOG ----------------
    posts = [
        ("somerset-county-market-update", "Somerset County Market Update", "July 23, 2026", IMG["b_somerset"],
         "Somerset County had a strong month. In May 2026, 357 homes went under contract across the county, up sharply from 250 in May 2025&hellip;"),
        ("bergen-county-housing-market-update-for-may-2026", "Bergen County Housing Market Update for May 2026", "July 20, 2026", IMG["b_bergen"],
         "A look at where Bergen County stands this spring &mdash; contracts, inventory and what months-of-supply is telling buyers and sellers."),
        ("union-county-new-jersey-housingtrac-monthly-may-2026", "Union County, New Jersey | HousingTRAC Monthly — May 2026", "July 14, 2026", IMG["b_union"],
         "The monthly HousingTRAC snapshot for Union County: pending sales, active inventory and price trends explained in plain terms."),
        ("morris-county-housing-april-2026-market-report", "Morris County Housing: April 2026 Market Report", "June 23, 2026", IMG["b_morris"],
         "Morris County&rsquo;s April numbers and what they mean for buyers, sellers and investors in David&rsquo;s home market."),
        ("passaic-county-housing-market-what-the-april-2026-numbers-actually-mean", "Passaic County Housing Market: What the April 2026 Numbers Actually Mean", "June 18, 2026", IMG["b_passaic"],
         "Beyond the headlines &mdash; a clear read on Passaic County&rsquo;s April 2026 housing data."),
        ("sussex-county-housing-market-what-the-april-2026-numbers-actually-mean", "Sussex County Housing Market: What the April 2026 Numbers Actually Mean", "June 15, 2026", IMG["b_sussex"],
         "What Sussex County&rsquo;s latest numbers signal for one of NJ&rsquo;s most rural and rural-adjacent markets."),
        ("passaic-county-housing-market-slowing-but-still-relatively-tight", "Passaic County Housing Market: Slowing, But Still Relatively Tight", "June 2026", IMG["b_passaic"],
         "Momentum is easing, but inventory remains constrained. Here&rsquo;s what a &ldquo;slowing but tight&rdquo; market means for you."),
    ]
    cards = "".join("""
    <a class="post-card" href="/blog/%(slug)s">
      <div class="thumb" style="background-image:url('%(img)s')"></div>
      <div class="body">
        <div class="date">%(date)s</div>
        <h3>%(title)s</h3>
        <p class="excerpt">%(ex)s</p>
        <span class="view">Read More &rsaquo;</span>
      </div>
    </a>""" % {"slug": p[0], "img": p[3], "date": p[2], "title": p[1], "ex": p[4]} for p in posts)
    blog_body = head_block("Market Insights", "Local New Jersey housing-market reports and real estate insights from David Wainwright Jr.") + """
<section class="section"><div class="container"><div class="post-grid">%s</div></div></section>""" % cards
    page("blog", "Market Insights — Real Estate Blog | David Wainwright Jr, RE/MAX Select",
         "New Jersey county-by-county housing market reports and real estate insights from David Wainwright Jr.",
         blog_body, akey="blog")

    # Full article for the Somerset post; styled placeholders for the rest.
    somerset_article = """
<article class="article">
  <h1>Somerset County Market Update</h1>
  <div class="byline">by David Wainwright Jr &middot; July 23, 2026</div>
  <img src="%(img)s" alt="Somerset County Market Update" style="width:100%%;border-radius:6px;margin-bottom:26px">
  <h2>Somerset County Home Sales Picked Up in May, but the Market Is Shifting</h2>
  <p>Somerset County had a strong month. In May 2026, 357 homes went under contract across the county, up sharply from 250 in May 2025. That is a real increase in buyer activity, and it bucks the trend we are seeing in a lot of other New Jersey counties this spring.</p>
  <p>But there is a second part of this story that matters just as much. The number of homes for sale in Somerset County also grew, reaching 604 unsold listings in May, up from 555 a year earlier. More buyers showed up, and more sellers did too.</p>
  <h2>What This Means in Plain Terms</h2>
  <p>One of the numbers we track closely is called months supply. It sounds technical, but it answers a simple question: if no new homes came on the market starting today, how long would it take to sell everything that is currently listed?</p>
  <p>In Somerset County right now, that answer is about 1.7 months. Put another way, inventory is still tight and the market continues to favor sellers &mdash; but the extra listings are giving buyers a little more room to breathe than they had a year ago.</p>
  <p>If you are thinking about buying or selling in Somerset County, or anywhere across Morris, Sussex or Warren counties, reach out and let&rsquo;s talk through what these numbers mean for your specific situation.</p>
  <p><a class="btn btn-gold" href="/contact">Talk to Dave</a></p>
</article>""" % {"img": IMG["b_somerset"]}
    page("blog/somerset-county-market-update",
         "Somerset County Market Update | David Wainwright Jr, RE/MAX Select",
         "Somerset County NJ housing market update for May 2026 — contracts, inventory and months supply explained.",
         somerset_article, akey="blog")

    for p in posts[1:]:
        art = """
<article class="article">
  <h1>%(title)s</h1>
  <div class="byline">by David Wainwright Jr &middot; %(date)s</div>
  <img src="%(img)s" alt="%(title)s" style="width:100%%;border-radius:6px;margin-bottom:26px">
  <p>%(ex)s</p>
  <div class="placeholder-note"><strong>Article content placeholder.</strong> The full text of this market report will be migrated from the original site. The layout, image and metadata above match the live post.</div>
  <p style="margin-top:26px"><a class="btn btn-gold" href="/contact">Talk to Dave</a></p>
</article>""" % {"title": p[1], "date": p[2], "img": p[3], "ex": p[4]}
        page("blog/" + p[0], p[1] + " | David Wainwright Jr, RE/MAX Select",
             p[1] + " — New Jersey housing market insight from David Wainwright Jr.", art, akey="blog")

    # ---------------- CONTACT (Netlify Forms) ----------------
    contact_body = head_block("Contact Dave Wainwright", "Residential, Rural, Commercial &amp; REO expert serving NJ &amp; NY.") + """
<section class="section"><div class="container tight">
<div style="display:grid;grid-template-columns:1fr 1fr;gap:40px" class="contact-grid">
  <div class="prose">
    <h2>Let&rsquo;s talk</h2>
    <p>Whether you&rsquo;re buying, selling, or need REO and commercial expertise, reach out directly.</p>
    <p><strong>%(brand)s</strong><br>%(name)s</p>
    <p><a href="tel:%(phone_href)s">%(phone)s</a><br>
       <a href="mailto:%(email)s">%(email)s</a><br>
       License ID: %(license)s<br>%(address)s</p>
  </div>
  <form name="contact" method="POST" data-netlify="true" netlify-honeypot="bot-field" class="calc-mock" style="margin:0">
    <input type="hidden" name="form-name" value="contact">
    <p style="display:none"><label>Don&rsquo;t fill this out: <input name="bot-field"></label></p>
    <div class="row" style="display:block"><label>Name</label><input style="width:100%%" type="text" name="name" required></div>
    <div class="row" style="display:block"><label>Email</label><input style="width:100%%" type="email" name="email" required></div>
    <div class="row" style="display:block"><label>Phone</label><input style="width:100%%" type="tel" name="phone"></div>
    <div class="row" style="display:block"><label>How can we help?</label><textarea style="width:100%%;min-height:120px;padding:11px 12px;border:1px solid #dcdcdc;border-radius:3px;font-family:inherit" name="message"></textarea></div>
    <button class="btn btn-gold btn-lg" type="submit" style="width:100%%">Send Message</button>
  </form>
</div>
</div></section>""" % dict(AGENT)
    page("contact", "Contact David Wainwright Jr | RE/MAX Select",
         "Contact David Wainwright Jr, RE/MAX Select — residential, rural, commercial and REO real estate expert in NJ & NY.",
         contact_body, akey="")

    # ---------------- 404 ----------------
    nf = """
<section class="page-head"><div class="container"><h1>Page Not Found</h1><p>The page you&rsquo;re looking for doesn&rsquo;t exist or has moved.</p></div></section>
<section class="section"><div class="container center"><a class="btn btn-gold btn-lg" href="/">Back to Home</a></div></section>"""
    # write 404 at site root as 404.html (Netlify serves it automatically)
    import os as _os
    doc404 = g["page"]  # reuse builder by writing manually
    # Build 404 into site/404.html directly
    tmp = "404-tmp"
    page(tmp, "Page Not Found | David Wainwright Jr, RE/MAX Select", "Page not found.", nf, akey="")
    src = _os.path.join(g["ROOT"], tmp, "index.html")
    dst = _os.path.join(g["ROOT"], "404.html")
    _os.replace(src, dst)
    try:
        _os.rmdir(_os.path.join(g["ROOT"], tmp))
    except OSError:
        pass
    print("wrote 404.html")
