#!/usr/bin/env python3
"""Generate subpages with shared header/footer for Jerson's Concrete site."""

DOMAIN = "https://www.concretehouston.org"

NAV_ITEMS = [
    ("/", "Home"),
    ("/parking-lot-repair.html", "Parking Lot Repair"),
    ("/commercial-concrete.html", "Commercial"),
    ("/industrial-concrete.html", "Industrial"),
    ("/civil-concrete.html", "Civil"),
    ("/residential-concrete.html", "Residential"),
    ("/ready-mix-delivery.html", "Ready Mix"),
    ("/service-areas.html", "Service Areas"),
    ("/about.html", "About"),
    ("/contact.html", "Free Estimate"),
]

FOOTER = """<footer class="site-footer">
  <div class="wrap footer-grid">
    <div>
      <h2>Jerson's Concrete Houston Parking Lot Repair</h2>
      <p>Family-owned Houston concrete contractors. Lot repair and construction, commercial and industrial concrete, civil infrastructure, home foundations, and driveways.</p>
      <p><a href="tel:281-671-4809">281-671-4809</a><br>
      <a href="https://maps.app.goo.gl/TdP5XurEcnBgiJF19" rel="noopener">Find us on Google Maps</a></p>
    </div>
    <div>
      <h2>Services</h2>
      <ul>
        <li><a href="/parking-lot-repair.html">Parking Lot Repair Houston</a></li>
        <li><a href="/commercial-concrete.html">Commercial Concrete</a></li>
        <li><a href="/industrial-concrete.html">Industrial Concrete</a></li>
        <li><a href="/civil-concrete.html">Civil Concrete Construction</a></li>
        <li><a href="/residential-concrete.html">Foundations &amp; Driveways</a></li>
        <li><a href="/ready-mix-delivery.html">Ready Mix Concrete Delivery</a></li>
        <li><a href="/service-areas.html">Service Areas</a></li>
        <li><a href="/about.html">About Us</a></li>
        <li><a href="/contact.html">Request an Estimate</a></li>
      </ul>
    </div>
    <div class="footer-map">
      <h2>Our Location</h2>
      <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d221667.17747729734!2d-95.51743001362001!3d29.761744277271248!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x864099e6f4100001%3A0xb792829c2418bfb7!2sJerson%E2%80%99s%20Concrete%20Houston%20Parking%20Lot%20Repair!5e0!3m2!1sen!2sus!4v1784423699468!5m2!1sen!2sus" title="Map of Jerson's Concrete Houston Parking Lot Repair" style="border:0;" allowfullscreen loading="lazy" referrerpolicy="strict-origin-when-cross-origin"></iframe>
    </div>
  </div>
  <div class="wrap fineprint">
    <p>&copy; 2026 Jerson's Concrete Houston Parking Lot Repair. All rights reserved. &middot; <a href="/sitemap.xml">Sitemap</a></p>
  </div>
</footer>

<div class="call-bar">
  <a class="call" href="tel:281-671-4809">Call Now</a>
  <a class="estimate" href="/contact.html">Free Estimate</a>
</div>

<script src="/js/site.js"></script>
</body>
</html>
"""


def nav(current):
    items = []
    for href, label in NAV_ITEMS:
        cur = ' aria-current="page"' if href == current else ""
        items.append(f'      <li><a href="{href}"{cur}>{label}</a></li>')
    return "\n".join(items)


def page(path, title, desc, og_image, extra_head, body, breadcrumb_name):
    breadcrumb = f"""<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {{"@type": "ListItem", "position": 1, "name": "Home", "item": "{DOMAIN}/"}},
    {{"@type": "ListItem", "position": 2, "name": "{breadcrumb_name}", "item": "{DOMAIN}{path}"}}
  ]
}}
</script>"""
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{DOMAIN}{path}">
<meta property="og:type" content="website">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{DOMAIN}{path}">
<meta property="og:image" content="{DOMAIN}{og_image}">
<meta property="og:site_name" content="Jerson's Concrete Houston Parking Lot Repair">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Anton&family=Barlow:wght@400;600;700&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/css/style.css">
{breadcrumb}
{extra_head}
</head>
<body>
<a class="skip-link" href="#main">Skip to content</a>

<header class="site-header">
  <div class="header-bar">
    <a class="brand" href="/">Jerson's Concrete<small>Houston Parking Lot Repair</small></a>
    <a class="header-call" href="tel:281-671-4809">CALL 281-671-4809</a>
    <button class="nav-toggle" aria-expanded="false" aria-controls="site-nav">Menu</button>
  </div>
  <nav class="site-nav" id="site-nav" aria-label="Main">
    <ul>
{nav(path)}
    </ul>
  </nav>
</header>

<main id="main">
{body}
</main>

{FOOTER}"""


def service_schema(name, desc, path):
    return f"""<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "Service",
  "serviceType": "{name}",
  "provider": {{"@id": "{DOMAIN}/#business"}},
  "areaServed": "Greater Houston, TX",
  "url": "{DOMAIN}{path}",
  "description": "{desc}"
}}
</script>"""


ESTIMATE_BAND = """<section class="cta-band">
  <div class="wrap">
    <h2>Ready for a Price? Request a Free Estimate</h2>
    <p>Call us or send the form. Site visit, written scope, clear price &mdash; the same four-step process for every project, residential to civil.</p>
    <div class="cta-row">
      <a class="btn btn-solid" href="tel:281-671-4809">Call 281-671-4809</a>
      <a class="btn btn-ghost" href="/contact.html">Send the Estimate Form</a>
    </div>
  </div>
</section>"""

PAGES = {}

# ---------------- PARKING LOT REPAIR ----------------
PAGES["/parking-lot-repair.html"] = dict(
    title="Parking Lot Repair & Construction Houston TX | Jerson's Concrete",
    desc="Concrete parking lot repair in Houston: pothole repair, panel replacement, new parking lot construction, and ADA work. Phased so your business stays open. Free estimates.",
    og_image="/images/parking-lot-repair.svg",
    breadcrumb="Parking Lot Repair",
    extra_head=service_schema(
        "Parking Lot Repair and Construction",
        "Concrete parking lot repair, pothole repair, panel replacement, and new parking lot construction across the greater Houston area.",
        "/parking-lot-repair.html",
    ),
    body="""<section class="hero">
  <div class="wrap">
    <span class="eyebrow">Our #1 Service</span>
    <h1>Parking Lot Repair &amp; Construction in Houston</h1>
    <p class="lede">Potholes, cracked panels, sunken sections, drainage problems &mdash; we repair them all, and we build new concrete parking lots from the dirt up. Phased work keeps your business open while we pour.</p>
    <div class="cta-row">
      <a class="btn btn-solid" href="tel:281-671-4809">Call 281-671-4809</a>
      <a class="btn btn-ghost" href="/contact.html">Request a Free Estimate</a>
    </div>
    <ul class="badge-row">
      <li class="badge">Bonded &amp; Insured</li>
      <li class="badge">Retail &middot; Office &middot; Church &middot; HOA</li>
      <li class="badge">Phased Work, Lot Stays Open</li>
      <li class="badge">Free Written Estimates</li>
    </ul>
  </div>
</section>

<hr class="joint">

<section class="section">
  <div class="wrap two-col">
    <div>
      <span class="eyebrow">The problem we fix</span>
      <h2>Concrete Parking Lot Repair</h2>
      <p>A property manager in Clear Lake called us about one pothole near her building entrance. By the time we walked the lot, that one pothole had three cousins forming around it. That is how parking lot damage works in Houston: rain gets under the slab, the clay soil moves, and small cracks grow into trip hazards and tire-eaters.</p>
      <p>Our parking lot repair process fixes the cause, not just the hole. We saw-cut the failed section to clean edges, dig out and re-compact the subgrade, then pour a high-strength mix matched to your traffic load. The patch bonds tight and sits flush &mdash; no hump, no bathtub ring.</p>
      <h3>Repair Work We Handle</h3>
      <ul class="check-list">
        <li>Pothole repair and full-depth panel replacement</li>
        <li>Crack repair and joint sealing to keep water out</li>
        <li>Lifting or replacing sunken, uneven sections</li>
        <li>Drainage corrections so water leaves the lot</li>
        <li>ADA ramps, accessible stalls, and wheel stops</li>
        <li>Curb repair and re-striping after the pour</li>
      </ul>
    </div>
    <div class="col-media">
      <img src="/images/parking-lot-repair.svg" alt="Concrete crew saw-cutting and patching a damaged parking lot panel in Houston" width="1200" height="675" loading="eager">
    </div>
  </div>
</section>

<hr class="joint">

<section class="section section-alt">
  <div class="wrap">
    <span class="eyebrow">New lots</span>
    <h2>Parking Lot Construction</h2>
    <p>Building a new lot? Concrete costs more than asphalt on day one and less every year after. Houston sun softens asphalt; it does not soften a properly built concrete lot. We handle parking lot construction start to finish: grading, stabilized subgrade, reinforcement, jointing plan, pour, cure, and striping.</p>
    <p>We size the slab for your real traffic. A church lot that fills up twice a week needs a different design than a strip center with daily delivery trucks. Tell us how the lot gets used, and we design the mix and thickness to match. New lot for a new building? We often pour the <a href="/commercial-concrete.html">building pad and sidewalks</a> on the same mobilization, which saves you money.</p>
    <h3>Who We Build and Repair Lots For</h3>
    <ul class="check-list">
      <li>Retail centers and restaurants &mdash; phased overnight or off-peak work</li>
      <li>Offices, medical buildings, and schools</li>
      <li>Churches and non-profits across <a href="/service-areas.html">greater Houston</a></li>
      <li>HOAs, apartment and condo communities</li>
      <li>Warehouses that need <a href="/industrial-concrete.html">heavy-duty industrial paving</a></li>
    </ul>
  </div>
</section>

<hr class="joint">

<section class="section">
  <div class="wrap">
    <span class="eyebrow">Straight answers</span>
    <h2>Parking Lot Repair Questions</h2>
    <div class="faq">
      <details>
        <summary>Should I repair sections or replace the whole lot?</summary>
        <div class="faq-body"><p>If less than about a third of the panels have failed and the base is sound, section repair usually makes sense. If damage is spread across most of the lot or the subgrade has failed, replacement costs less over ten years. We give you both numbers so you can decide.</p></div>
      </details>
      <details>
        <summary>How soon can cars park on the new concrete?</summary>
        <div class="faq-body"><p>Light vehicle traffic is normally fine after about 7 days, and heavy trucks after the mix reaches design strength. We post each phase and tell you exact dates for your pour.</p></div>
      </details>
      <details>
        <summary>Do you work nights or weekends?</summary>
        <div class="faq-body"><p>Yes. For busy retail lots we can saw-cut and pour during off-peak hours so customers always have a place to park.</p></div>
      </details>
    </div>
  </div>
</section>
"""
    + ESTIMATE_BAND,
)

# ---------------- COMMERCIAL ----------------
PAGES["/commercial-concrete.html"] = dict(
    title="Commercial Concrete Contractors Houston TX | Jerson's Concrete",
    desc="Commercial concrete contractors in Houston: building pads, sidewalks, curbs, dumpster pads, and flatwork for retail, restaurants, and offices. Free written estimates.",
    og_image="/images/commercial-concrete.svg",
    breadcrumb="Commercial Concrete",
    extra_head=service_schema(
        "Commercial Concrete Construction",
        "Commercial concrete work in Houston including building pads, sidewalks, curbs, dumpster pads, and flatwork for retail and office properties.",
        "/commercial-concrete.html",
    ),
    body="""<section class="hero">
  <div class="wrap">
    <span class="eyebrow">Business Properties</span>
    <h1>Commercial Concrete Contractors in Houston</h1>
    <p class="lede">Building pads, sidewalks, curbs, ramps, dumpster pads, and full site flatwork. We work with owners, property managers, and general contractors, and we hit the schedule we agree to.</p>
    <div class="cta-row">
      <a class="btn btn-solid" href="tel:281-671-4809">Call 281-671-4809</a>
      <a class="btn btn-ghost" href="/contact.html">Request a Bid</a>
    </div>
    <ul class="badge-row">
      <li class="badge">Bonded &amp; Insured</li>
      <li class="badge">Plan &amp; Spec Bids Welcome</li>
      <li class="badge">GC Subcontract Ready</li>
      <li class="badge">15+ Years in Houston</li>
    </ul>
  </div>
</section>

<hr class="joint">

<section class="section">
  <div class="wrap two-col">
    <div>
      <span class="eyebrow">What we pour</span>
      <h2>Commercial Concrete Work</h2>
      <p>A restaurant owner near Sugar Land once told us his last concrete sub disappeared for three weeks mid-project, with the health inspector waiting on a finished dumpster pad. We poured it that Friday. Stories like that are why most of our commercial work comes from referrals: general contractors and owners want a crew that answers the phone and shows up.</p>
      <p>Our commercial concrete crews handle the full site package or a single scope item. We coordinate with your other trades, keep the site clean, and protect finished work while the rest of the job moves. Need concrete only? We offer <a href="/ready-mix-delivery.html">ready mix delivery</a> to GCs running their own placement crews.</p>
      <h3>Commercial Services</h3>
      <ul class="check-list">
        <li>Building pads and slab-on-grade for retail and office</li>
        <li>Sidewalks, entry aprons, and accessible ramps</li>
        <li>Curb and gutter, bollards, and dumpster pads</li>
        <li>Drive lanes and <a href="/parking-lot-repair.html">parking lot construction and repair</a></li>
        <li>Tear-out and replacement of failed flatwork</li>
      </ul>
      <p>Need heavier slabs for trucks and machines? That is our <a href="/industrial-concrete.html">industrial concrete</a> page. Public right-of-way work lives on the <a href="/civil-concrete.html">civil construction</a> page.</p>
    </div>
    <div class="col-media">
      <img src="/images/commercial-concrete.svg" alt="Commercial retail building in Houston with new concrete sidewalks and parking flatwork" width="1200" height="675" loading="eager">
    </div>
  </div>
</section>

<hr class="joint">

<section class="section section-alt">
  <div class="wrap">
    <span class="eyebrow">Why owners call us</span>
    <h2>Built for Houston Business Conditions</h2>
    <p>Gulf Coast weather is hard on commercial concrete. Summer slabs can hit 140&deg;F, then a cold snap drops them 60 degrees overnight. Add clay soil movement and daily delivery trucks, and cheap flatwork fails fast. We control curing, joint spacing, and mix design so your concrete handles all of it.</p>
    <p>Every commercial job follows the same <a href="/#estimate-process">four-step estimate process</a>: site visit or plan review, written scope, agreed schedule, pour. You always know the price before we mobilize.</p>
  </div>
</section>
"""
    + ESTIMATE_BAND,
)

# ---------------- INDUSTRIAL ----------------
PAGES["/industrial-concrete.html"] = dict(
    title="Industrial Concrete Contractors Houston TX | Jerson's Concrete",
    desc="Industrial concrete in Houston: heavy-duty slabs, warehouse floors, loading docks, truck aprons, and equipment pads built for forklift and 18-wheeler traffic.",
    og_image="/images/industrial-concrete.svg",
    breadcrumb="Industrial Concrete",
    extra_head=service_schema(
        "Industrial Concrete Construction",
        "Industrial concrete work in Houston including warehouse floors, heavy-duty slabs, loading docks, truck aprons, and equipment pads.",
        "/industrial-concrete.html",
    ),
    body="""<section class="hero">
  <div class="wrap">
    <span class="eyebrow">Heavy Duty</span>
    <h1>Industrial Concrete Contractors in Houston</h1>
    <p class="lede">Warehouse floors, loading docks, truck aprons, and equipment pads. When forklifts run all day and 18-wheelers back in every hour, the slab has to be designed for it &mdash; and that is the work we do.</p>
    <div class="cta-row">
      <a class="btn btn-solid" href="tel:281-671-4809">Call 281-671-4809</a>
      <a class="btn btn-ghost" href="/contact.html">Request a Bid</a>
    </div>
    <ul class="badge-row">
      <li class="badge">Bonded &amp; Insured</li>
      <li class="badge">Engineered Mix Designs</li>
      <li class="badge">Warehouse &middot; Plant &middot; Yard</li>
      <li class="badge">Free Written Estimates</li>
    </ul>
  </div>
</section>

<hr class="joint">

<section class="section">
  <div class="wrap two-col">
    <div>
      <span class="eyebrow">Built for load</span>
      <h2>Industrial Concrete Services</h2>
      <p>A warehouse manager off the Gulf Freeway showed us a dock apron that was only four years old and already rubble. The original contractor had poured a standard commercial mix under trucks that gross 80,000 pounds. Wrong slab for the job. We replaced it with a thicker, reinforced apron on a stabilized base, and it has taken daily truck traffic since.</p>
      <p>Industrial concrete is a load math problem. Point loads from rack legs, wheel loads from forklifts, impact at dock doors &mdash; each one drives thickness, reinforcement, and joint layout. We build to those numbers.</p>
      <h3>Industrial Work We Handle</h3>
      <ul class="check-list">
        <li>Warehouse and distribution center floor slabs</li>
        <li>Loading docks, dock aprons, and truck courts</li>
        <li>Equipment and machine foundations</li>
        <li>Container yards and laydown areas</li>
        <li>Trench drains and washdown areas</li>
        <li>Heavy-duty <a href="/parking-lot-repair.html">truck parking and paving repair</a></li>
      </ul>
      <p>Lighter-duty site work like sidewalks and building pads is on our <a href="/commercial-concrete.html">commercial concrete</a> page.</p>
    </div>
    <div class="col-media">
      <img src="/images/industrial-concrete.svg" alt="Industrial warehouse in Houston with a heavy-duty concrete slab and loading dock" width="1200" height="675" loading="eager">
    </div>
  </div>
</section>

<hr class="joint">

<section class="section section-alt">
  <div class="wrap">
    <span class="eyebrow">Keep operating</span>
    <h2>Repairs Without Shutting Down Your Facility</h2>
    <p>Downtime costs more than concrete. For working facilities we phase repairs bay by bay, pour on weekends, and use high-early-strength mixes that take traffic in days instead of weeks. Tell us your operating hours and we build the schedule around them. It starts with the same <a href="/#estimate-process">four-step estimate process</a> we use on every project.</p>
  </div>
</section>
"""
    + ESTIMATE_BAND,
)

# ---------------- CIVIL ----------------
PAGES["/civil-concrete.html"] = dict(
    title="Civil Concrete Construction Houston TX | Jerson's Concrete",
    desc="Civil concrete construction in Houston: roadway panels, curb and gutter, culverts, spillways, and public infrastructure built to city and TxDOT specifications.",
    og_image="/images/civil-concrete.svg",
    breadcrumb="Civil Concrete Construction",
    extra_head=service_schema(
        "Civil Concrete Construction",
        "Civil concrete construction in Houston including roadway panels, curb and gutter, culverts, spillways, and public infrastructure.",
        "/civil-concrete.html",
    ),
    body="""<section class="hero">
  <div class="wrap">
    <span class="eyebrow">Public Infrastructure</span>
    <h1>Civil Concrete Construction in Houston</h1>
    <p class="lede">Roadway panels, curb and gutter, box culverts, spillways, and drainage structures. We build public infrastructure to plan, to spec, and to inspection &mdash; for cities, municipalities, and prime contractors.</p>
    <div class="cta-row">
      <a class="btn btn-solid" href="tel:281-671-4809">Call 281-671-4809</a>
      <a class="btn btn-ghost" href="/contact.html">Request Bid Documents Review</a>
    </div>
    <ul class="badge-row">
      <li class="badge">Bonded &amp; Insured</li>
      <li class="badge">City &amp; TxDOT Spec Experience</li>
      <li class="badge">Prime &amp; Sub Roles</li>
      <li class="badge">15+ Years in Houston</li>
    </ul>
  </div>
</section>

<hr class="joint">

<section class="section">
  <div class="wrap two-col">
    <div>
      <span class="eyebrow">Built to spec</span>
      <h2>Civil Concrete Work We Perform</h2>
      <p>Public work is a different trade. Every pour has a spec section, a testing lab on site, and an inspector who signs off before the next step. We like it that way. Our crews have placed roadway panels, drainage structures, and flatwork on city-contracted projects around Houston, and passing inspection the first time is how we keep that work coming.</p>
      <h3>Civil Scope Items</h3>
      <ul class="check-list">
        <li>Concrete roadway panels and street repair</li>
        <li>Curb and gutter, medians, and driveways in right-of-way</li>
        <li>Box culverts, headwalls, and wingwalls</li>
        <li>Spillways and drainage channel lining</li>
        <li>Structures for water and wastewater facilities</li>
        <li>ADA sidewalks and ramp retrofits in public right-of-way</li>
      </ul>
      <p>Houston drainage is serious business &mdash; this region moves storm water by the acre-foot, and the concrete that carries it has to be right. Subgrade prep, steel placement, and cure control get checked at every step on our jobs.</p>
    </div>
    <div class="col-media">
      <img src="/images/civil-concrete.svg" alt="Civil concrete infrastructure in Houston including roadway, curb and gutter, and box culvert" width="1200" height="675" loading="eager">
    </div>
  </div>
</section>

<hr class="joint">

<section class="section section-alt">
  <div class="wrap">
    <span class="eyebrow">For estimators &amp; PMs</span>
    <h2>Bidding Civil Work With Us</h2>
    <p>Send plans and spec sections through our <a href="/contact.html">contact page</a> and mark the project "civil." We return unit pricing or lump sum, with exclusions listed plainly so there are no surprises at buyout. We take prime roles on smaller packages and sub roles under larger primes. Private-side site work belongs on our <a href="/commercial-concrete.html">commercial</a> and <a href="/industrial-concrete.html">industrial</a> pages.</p>
  </div>
</section>
"""
    + ESTIMATE_BAND,
)

# ---------------- RESIDENTIAL ----------------
PAGES["/residential-concrete.html"] = dict(
    title="Concrete Foundations & Driveways Houston TX | Jerson's Concrete",
    desc="Residential concrete in Houston: slab-on-grade home foundations, multi-family foundation packages, driveway replacement, and new driveway installation. Free estimates.",
    og_image="/images/residential-concrete.svg",
    breadcrumb="Residential Concrete",
    extra_head=service_schema(
        "Residential Concrete Foundations and Driveways",
        "Residential concrete in Houston including slab-on-grade home foundations, multi-family foundation packages, driveway replacement, and new driveway installation.",
        "/residential-concrete.html",
    ),
    body="""<section class="hero">
  <div class="wrap">
    <span class="eyebrow">Homes &amp; Multi-Family</span>
    <h1>Home Foundations &amp; Driveways in Houston</h1>
    <p class="lede">We pour slab-on-grade foundations for new homes, full foundation packages for apartments and townhome developments, and we replace or install concrete driveways across the Houston area.</p>
    <div class="cta-row">
      <a class="btn btn-solid" href="tel:281-671-4809">Call 281-671-4809</a>
      <a class="btn btn-ghost" href="/contact.html">Request a Free Estimate</a>
    </div>
    <ul class="badge-row">
      <li class="badge">Bonded &amp; Insured</li>
      <li class="badge">Builder &amp; Homeowner Friendly</li>
      <li class="badge">Engineered Foundations</li>
      <li class="badge">Free Written Estimates</li>
    </ul>
  </div>
</section>

<hr class="joint">

<section class="section">
  <div class="wrap two-col">
    <div>
      <span class="eyebrow">Under your home</span>
      <h2>Concrete Foundations for Homes</h2>
      <p>Ask anyone in Pearland or Friendswood what Houston clay does to a bad foundation. Doors stick, floors slope, cracks climb the drywall. The fix costs ten times what doing it right the first time costs. So we do it right the first time.</p>
      <p>We form and pour engineered slab-on-grade foundations for custom homes and production builders. Your engineer's plan drives everything: beam depth and layout, steel or post-tension cable placement, and mix design. We hold tight tolerances on the pad so framing starts square.</p>
      <h3>Foundation Work</h3>
      <ul class="check-list">
        <li>Slab-on-grade foundations for new single-family homes</li>
        <li>Multi-family foundation packages &mdash; apartments, condos, townhomes, and build-to-rent communities</li>
        <li>Garage, shop, and home-addition slabs</li>
        <li>Patio and outdoor living slabs poured with the foundation or after</li>
      </ul>
      <p>Building several units? We sequence pours across the site so your framing crews never wait on concrete.</p>
    </div>
    <div class="col-media">
      <img src="/images/residential-concrete.svg" alt="Houston home with a new slab-on-grade concrete foundation and concrete driveway" width="1200" height="675" loading="eager">
    </div>
  </div>
</section>

<hr class="joint">

<section class="section section-alt">
  <div class="wrap">
    <span class="eyebrow">Curb appeal that lasts</span>
    <h2>Driveway Replacement &amp; New Driveway Installation</h2>
    <p>A cracked, sunken driveway drags down the whole front of a house. Our driveway replacement crew tears out the old slab, fixes the base underneath &mdash; usually the real reason it failed &mdash; and pours a new reinforced driveway with clean joints and a uniform broom finish. Most tear-out-and-replace jobs take one to two days of work, plus cure time before you park on it.</p>
    <p>Building new? We install new driveways, approaches, and walkways for custom homes and additions, matched to your home's layout and drainage. Where the driveway meets the street, that approach section is public right-of-way in many areas &mdash; we handle the permits and pour it to <a href="/civil-concrete.html">city spec</a>.</p>
    <div class="faq">
      <details>
        <summary>When can I park on my new driveway?</summary>
        <div class="faq-body"><p>Cars after about 7 days for a standard mix. Full design strength takes about 28 days, so keep heavy trucks off until then. We put the exact dates for your pour in writing.</p></div>
      </details>
      <details>
        <summary>Do you repair driveways or only replace them?</summary>
        <div class="faq-body"><p>If damage is limited to a section, we can replace just those panels. If cracks run through most of the slab or the base has failed, full replacement lasts longer and often costs less than repeated repairs. We give you an honest read on the site visit.</p></div>
      </details>
    </div>
  </div>
</section>
"""
    + ESTIMATE_BAND,
)

# ---------------- READY MIX DELIVERY ----------------
PAGES["/ready-mix-delivery.html"] = dict(
    title="Ready Mix Concrete Delivery Houston TX | Jerson's Concrete",
    desc="Ready mix concrete delivery in Houston: 3000-4000 PSI mixes, fiber-reinforced and admixture blends, small loads welcome, same-day delivery available. Call 281-671-4809.",
    og_image="/images/ready-mix-delivery.svg",
    breadcrumb="Ready Mix Concrete Delivery",
    extra_head=service_schema(
        "Ready Mix Concrete Delivery",
        "Ready mix concrete delivered across the greater Houston area, including 3000 to 4000 PSI mixes, fiber-reinforced concrete, and admixture blends for residential, commercial, industrial, and civil projects.",
        "/ready-mix-delivery.html",
    ),
    body="""<section class="hero">
  <div class="wrap">
    <span class="eyebrow">Fresh Concrete, On Schedule</span>
    <h1>Ready Mix Concrete Delivery in Houston</h1>
    <p class="lede">Fresh concrete hauled from the nearest batch plant straight to your job site. Standard and high-strength mixes, small loads welcome, and same-day delivery when you're in a bind.</p>
    <div class="cta-row">
      <a class="btn btn-solid" href="tel:281-671-4809">Call 281-671-4809</a>
      <a class="btn btn-ghost" href="/contact.html">Schedule a Delivery</a>
    </div>
    <ul class="badge-row">
      <li class="badge">Same-Day Delivery Available</li>
      <li class="badge">2 Yards to 20+</li>
      <li class="badge">3000&ndash;4000 PSI Mixes</li>
      <li class="badge">Free Quotes</li>
    </ul>
  </div>
</section>

<hr class="joint">

<section class="section">
  <div class="wrap two-col">
    <div>
      <span class="eyebrow">Why fresh matters</span>
      <h2>Ready Mix Concrete Delivery</h2>
      <p>A builder in Pearland called us after losing half a Saturday: his crew stood around for three hours waiting on a truck from across town, and when the mix finally showed up, it was stiff and hard to work. Concrete has a clock on it. Once the drum loads, every mile and every minute costs you workability.</p>
      <p>That is why our ready mix concrete delivery runs from the batch plant closest to your site. Shorter haul, less drum time, better slump when the chute drops. You get concrete that places and finishes the way it should.</p>
      <p>We deliver to every kind of project: <a href="/residential-concrete.html">home foundations and driveways</a>, <a href="/commercial-concrete.html">commercial slabs and flatwork</a>, <a href="/industrial-concrete.html">industrial floors</a>, <a href="/parking-lot-repair.html">parking lot pours</a>, and <a href="/civil-concrete.html">civil work</a>. Contractor or homeowner, two yards or twenty &mdash; tell us the location, the spec, the yardage, and the pour time, and a truck starts rolling.</p>
    </div>
    <div class="col-media">
      <img src="/images/ready-mix-delivery.svg" alt="Ready mix concrete truck delivering fresh concrete to a Houston job site" width="1200" height="675" loading="eager">
    </div>
  </div>
</section>

<hr class="joint">

<section class="section section-alt">
  <div class="wrap">
    <span class="eyebrow">The right mix for the job</span>
    <h2>Concrete Mix Designs We Deliver</h2>
    <p>Not every slab needs the same concrete. A backyard patio and a truck-loading apron carry very different loads, and the mix should match. Here is what we haul:</p>
    <ul class="check-list">
      <li><strong>3000 PSI</strong> &mdash; the workhorse for sidewalks, patios, and most residential flatwork</li>
      <li><strong>3500 PSI</strong> &mdash; driveways, garage slabs, and foundations on engineer's spec</li>
      <li><strong>4000 PSI</strong> &mdash; commercial slabs, parking areas, and pours that see real traffic</li>
      <li><strong>Fiber-reinforced concrete</strong> &mdash; added crack resistance for slabs and toppings</li>
      <li><strong>Admixture blends</strong> &mdash; accelerators, retarders, and other adjustments for hot Houston pour days or fast turnaround</li>
      <li><strong>Specialty mix designs</strong> &mdash; send us the spec sheet and we match it</li>
    </ul>
    <p>Not sure which mix your project calls for? Say what you're building and we'll point you to the right one &mdash; no upsell, just the mix the job needs.</p>
  </div>
</section>

<hr class="joint">

<section class="section">
  <div class="wrap">
    <span class="eyebrow">When the clock is tight</span>
    <h2>Same-Day Concrete Delivery in Houston</h2>
    <p>Crews get rained out, trucks break down, suppliers no-show. When that happens on your job, call us early in the day and we can often have concrete rolling to your site the same day, dispatched from a Houston-area plant instead of a hauler two counties away. Being based in southeast Houston puts us minutes from Pasadena, Clear Lake, Pearland, and the Beltway &mdash; and within reach of the whole <a href="/service-areas.html">metro area</a>.</p>
    <h3>How to Be Ready When the Truck Arrives</h3>
    <ul class="check-list">
      <li>Have forms set, steel placed, and the crew on site before the scheduled window</li>
      <li>Clear a path for the truck &mdash; a loaded mixer is heavy and needs firm ground</li>
      <li>Plan a washout spot for the chute before the pour, not after</li>
      <li>Order 5&ndash;10% more than your math says; short-loading a pour costs more than the extra half yard</li>
    </ul>
  </div>
</section>

<hr class="joint">

<section class="section section-alt">
  <div class="wrap">
    <span class="eyebrow">Straight answers</span>
    <h2>Ready Mix Delivery Questions</h2>
    <div class="faq">
      <details>
        <summary>How many yards of concrete do I need?</summary>
        <div class="faq-body"><p>Multiply length by width by depth in feet, then divide by 27. A 20 by 20 foot slab at 4 inches (0.33 ft) comes to about 5 yards. Add 5&ndash;10% for waste and uneven grade. Call us with your dimensions and we'll check your math for free.</p></div>
      </details>
      <details>
        <summary>Do you deliver small loads?</summary>
        <div class="faq-body"><p>Yes. Plenty of suppliers turn down anything under a full truck. We take small orders &mdash; a couple of yards for a patio, a shed slab, or a repair section is a normal delivery for us.</p></div>
      </details>
      <details>
        <summary>How long can concrete stay in the truck?</summary>
        <div class="faq-body"><p>The general rule is about 90 minutes from batching, less on a hot Houston afternoon. That is exactly why we dispatch from the plant nearest your site &mdash; the mix spends its clock on your pour, not on the freeway.</p></div>
      </details>
      <details>
        <summary>Can you pour it too, or delivery only?</summary>
        <div class="faq-body"><p>Both. Delivery-only for contractors and capable DIYers, or our own crew can form, pour, and finish the whole job &mdash; see our <a href="/residential-concrete.html">residential</a> and <a href="/commercial-concrete.html">commercial</a> pages, or just ask when you call.</p></div>
      </details>
    </div>
  </div>
</section>
"""
    + ESTIMATE_BAND,
)

# ---------------- SERVICE AREAS ----------------
PAGES["/service-areas.html"] = dict(
    title="Concrete Contractor Service Areas | Houston & Surrounding Cities",
    desc="Jerson's Concrete serves Houston and surrounding cities: Pearland, Pasadena, Clear Lake, Friendswood, League City, Sugar Land, Katy, Baytown, Spring, Humble, and more.",
    og_image="/images/service-areas.svg",
    breadcrumb="Service Areas",
    extra_head="",
    body="""<section class="hero">
  <div class="wrap">
    <span class="eyebrow">Where we work</span>
    <h1>Houston Concrete Service Areas</h1>
    <p class="lede">Based on Fuqua Street in southeast Houston, working across the whole metro. If your project is within about an hour of the Beltway, we can be there.</p>
    <div class="cta-row">
      <a class="btn btn-solid" href="tel:281-671-4809">Call 281-671-4809</a>
      <a class="btn btn-ghost" href="/contact.html">Request a Free Estimate</a>
    </div>
  </div>
</section>

<hr class="joint">

<section class="section">
  <div class="wrap two-col">
    <div>
      <span class="eyebrow">Local means faster</span>
      <h2>Cities We Serve for Parking Lot Repair &amp; Concrete Work</h2>
      <p>Concrete is a local trade. Fresh mix has a clock on it from the minute the truck loads, so a nearby crew means better concrete on your site. Our shop in southeast Houston puts us minutes from the South Belt, Hobby Airport, Pearland, and Clear Lake, and an easy run to the rest of the metro.</p>
      <ul class="area-grid">
        <li>Houston</li>
        <li>Pearland</li>
        <li>Pasadena</li>
        <li>Clear Lake</li>
        <li>Friendswood</li>
        <li>League City</li>
        <li>Webster</li>
        <li>South Houston</li>
        <li>Deer Park</li>
        <li>La Porte</li>
        <li>Baytown</li>
        <li>Channelview</li>
        <li>Sugar Land</li>
        <li>Missouri City</li>
        <li>Stafford</li>
        <li>Katy</li>
        <li>Cypress</li>
        <li>Spring</li>
        <li>Humble</li>
        <li>The Woodlands</li>
        <li>Alvin</li>
      </ul>
      <p class="note">Don't see your city? Call anyway &mdash; we take projects across the greater Houston region.</p>
    </div>
    <div class="col-media">
      <img src="/images/service-areas.svg" alt="Map of greater Houston showing cities served by Jerson's Concrete" width="1200" height="675" loading="eager">
    </div>
  </div>
</section>

<hr class="joint">

<section class="section section-alt">
  <div class="wrap">
    <span class="eyebrow">Every service, every city</span>
    <h2>What We Do Across These Areas</h2>
    <p>Every city on this list gets our full service line: <a href="/parking-lot-repair.html">parking lot repair and construction</a> for businesses, <a href="/commercial-concrete.html">commercial</a> and <a href="/industrial-concrete.html">industrial concrete</a> for owners and GCs, <a href="/civil-concrete.html">civil infrastructure</a> for public agencies, and <a href="/residential-concrete.html">home foundations and driveways</a> for builders and homeowners &mdash; plus <a href="/ready-mix-delivery.html">ready mix concrete delivery</a> when you just need the truck.</p>
    <p>Neighborhood conditions matter, and we plan for them. Coastal-side cities like League City and Baytown deal with higher water tables. Fast-growing areas like Katy and Cypress sit on freshly graded clay that moves as it settles. Older in-town lots often hide failed base under decades of patches. We have poured in all of it.</p>
  </div>
</section>
"""
    + ESTIMATE_BAND,
)

# ---------------- ABOUT ----------------
PAGES["/about.html"] = dict(
    title="About Jerson's Concrete Houston Parking Lot Repair | Family-Owned",
    desc="Family-owned Houston concrete contractor with 15+ years of pours behind us. Meet the crew behind Jerson's Concrete Houston Parking Lot Repair and how we work.",
    og_image="/images/about-crew.svg",
    breadcrumb="About Us",
    extra_head="",
    body="""<section class="hero">
  <div class="wrap">
    <span class="eyebrow">Who we are</span>
    <h1>The Crew Behind the Concrete</h1>
    <p class="lede">Jerson's Concrete Houston Parking Lot Repair is a family-owned concrete company. We have been pouring in Houston for more than 15 years, and our name is on every slab we leave behind.</p>
    <div class="cta-row">
      <a class="btn btn-solid" href="tel:281-671-4809">Call 281-671-4809</a>
      <a class="btn btn-ghost" href="/contact.html">Request a Free Estimate</a>
    </div>
    <ul class="badge-row">
      <li class="badge">Family-Owned &amp; Operated</li>
      <li class="badge">Bonded &amp; Insured</li>
      <li class="badge">Houston Hispanic Chamber Member</li>
      <li class="badge">Se Habla Espa&ntilde;ol</li>
    </ul>
  </div>
</section>

<hr class="joint">

<section class="section">
  <div class="wrap two-col">
    <div>
      <span class="eyebrow">Our story</span>
      <h2>15+ Years of Houston Pours</h2>
      <p>This company started the way most good concrete companies do: one crew, one truck, and a reputation to build one job at a time. Years later, the trucks have multiplied, but the rule has not changed &mdash; do the job like your name is on it, because ours is.</p>
      <p>We grew up on <a href="/parking-lot-repair.html">parking lot repair</a>, and it is still the heart of the business. Along the way, builders asked us to pour <a href="/residential-concrete.html">foundations</a>, GCs brought us onto <a href="/commercial-concrete.html">commercial</a> and <a href="/industrial-concrete.html">industrial</a> sites, and the city work followed as our <a href="/civil-concrete.html">civil experience</a> grew. Today one company covers all of it.</p>
      <h3>How We Work</h3>
      <ul class="check-list">
        <li>Every estimate is written, itemized, and free</li>
        <li>The person who bids your job answers your calls during it</li>
        <li>We fix the subgrade before we pour &mdash; no shortcuts under the slab</li>
        <li>We phase work so homes and businesses stay usable</li>
        <li>We are a proud member of the Houston Hispanic Chamber of Commerce</li>
      </ul>
    </div>
    <div class="col-media">
      <img src="/images/about-crew.svg" alt="Jerson's Concrete crew and ready mix truck on a Houston jobsite" width="1200" height="675" loading="eager">
    </div>
  </div>
</section>

<hr class="joint">

<section class="section section-alt">
  <div class="wrap">
    <span class="eyebrow">Why Houston trusts us</span>
    <h2>Local Knowledge You Can't Fake</h2>
    <p>Concrete in Houston is a fight against clay soil, 100-degree pour days, tropical rain, and the occasional hard freeze. Fifteen-plus years of pouring here taught us when to pour, when to wait, how to cure in August, and how deep the base has to go on ground that moves. That knowledge is baked into every estimate we write &mdash; it is why our repairs stay fixed.</p>
    <p>Want to see where we are based? <a href="https://maps.app.goo.gl/TdP5XurEcnBgiJF19" rel="noopener">Find us on Google Maps</a>, or head to the <a href="/contact.html">contact page</a> to start your estimate.</p>
  </div>
</section>
"""
    + ESTIMATE_BAND,
)

# ---------------- CONTACT ----------------
PAGES["/contact.html"] = dict(
    title="Request a Free Concrete Estimate | Jerson's Concrete Houston",
    desc="Request a free estimate from Jerson's Concrete Houston Parking Lot Repair. Call 281-671-4809 or send the form. 11200 Fuqua St, Houston, TX 77089.",
    og_image="/images/contact-estimate.svg",
    breadcrumb="Contact Us",
    extra_head="""<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "ContactPage",
  "url": "https://www.concretehouston.org/contact.html",
  "mainEntity": {"@id": "https://www.concretehouston.org/#business"}
}
</script>""",
    body="""<section class="hero">
  <div class="wrap">
    <span class="eyebrow">Free estimates</span>
    <h1>Request Your Free Estimate</h1>
    <p class="lede">Call, or fill out the form below. Tell us the project type &mdash; residential, commercial, industrial, or civil &mdash; and we take it from there: site visit, written scope, clear price.</p>
    <div class="cta-row">
      <a class="btn btn-solid" href="tel:281-671-4809">Call 281-671-4809</a>
    </div>
  </div>
</section>

<hr class="joint">

<section class="section">
  <div class="wrap two-col">
    <div>
      <span class="eyebrow">Tell us about the project</span>
      <h2>Estimate Request Form</h2>
      <!-- SETUP REQUIRED: replace YOUR_FORM_ID with your Formspree form ID (free at formspree.io)
           or swap the action for any static-site form service (Web3Forms, Basin, etc.). -->
      <form action="https://formspree.io/f/YOUR_FORM_ID" method="POST" class="form-grid">
        <div>
          <label for="name">Your Name *</label>
          <input type="text" id="name" name="name" autocomplete="name" required>
        </div>
        <div>
          <label for="phone">Phone *</label>
          <input type="tel" id="phone" name="phone" autocomplete="tel" required>
        </div>
        <div>
          <label for="email">Email *</label>
          <input type="email" id="email" name="email" autocomplete="email" required>
        </div>
        <div>
          <label for="city">Project City *</label>
          <input type="text" id="city" name="city" placeholder="Houston, Pearland, Katy..." required>
        </div>
        <div>
          <label for="type">Project Type *</label>
          <select id="type" name="project_type" required>
            <option value="">Select one</option>
            <option>Parking lot repair</option>
            <option>Parking lot construction</option>
            <option>Commercial concrete</option>
            <option>Industrial concrete</option>
            <option>Civil / public infrastructure</option>
            <option>Ready mix concrete delivery</option>
            <option>Home foundation</option>
            <option>Multi-family foundation package</option>
            <option>Driveway replacement</option>
            <option>New driveway installation</option>
            <option>Other concrete work</option>
          </select>
        </div>
        <div>
          <label for="timeline">When Do You Need It?</label>
          <select id="timeline" name="timeline">
            <option>As soon as possible</option>
            <option>Within 1 month</option>
            <option>1&ndash;3 months</option>
            <option>Just planning / budgeting</option>
          </select>
        </div>
        <div class="full">
          <label for="details">Project Details *</label>
          <textarea id="details" name="details" placeholder="Example: retail parking lot on FM 518, about 6 cracked panels and 2 potholes, business must stay open during repairs." required></textarea>
        </div>
        <div class="full">
          <button type="submit" class="btn">Send Estimate Request</button>
          <p class="note">We reply within one business day. Nothing is scheduled and nothing is charged until you approve a written estimate.</p>
        </div>
      </form>
    </div>
    <div>
      <div class="col-media">
        <img src="/images/contact-estimate.svg" alt="Free written concrete estimate on a clipboard with a hard hat" width="1200" height="675" loading="eager">
      </div>
      <h2 style="margin-top:1.5rem;">Visit or Call</h2>
      <p><strong>Jerson's Concrete Houston Parking Lot Repair</strong><br>
      11200 Fuqua St<br>
      Houston, TX 77089<br>
      <a href="tel:281-671-4809">281-671-4809</a></p>
      <p><a href="https://maps.app.goo.gl/TdP5XurEcnBgiJF19" rel="noopener">Open in Google Maps</a></p>
      <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d221667.17747729734!2d-95.51743001362001!3d29.761744277271248!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x864099e6f4100001%3A0xb792829c2418bfb7!2sJerson%E2%80%99s%20Concrete%20Houston%20Parking%20Lot%20Repair!5e0!3m2!1sen!2sus!4v1784423699468!5m2!1sen!2sus" width="400" height="300" style="border:0; width:100%;" allowfullscreen loading="lazy" referrerpolicy="strict-origin-when-cross-origin" title="Map to Jerson's Concrete at 11200 Fuqua St, Houston TX 77089"></iframe>
    </div>
  </div>
</section>

<hr class="joint">

<section class="section section-alt">
  <div class="wrap">
    <span class="eyebrow">What happens next</span>
    <h2>After You Hit Send</h2>
    <ol class="process">
      <li><h3>We Call You Back</h3><p>Within one business day, usually sooner. We confirm the scope and set a site visit time that works for you.</p></li>
      <li><h3>Site Visit</h3><p>We walk the property, measure, and check subgrade and drainage. Plan-and-spec projects can skip straight to a document review.</p></li>
      <li><h3>Written Estimate</h3><p>A clear, itemized price. Free, no obligation, good for 30 days.</p></li>
      <li><h3>You Decide</h3><p>Approve it and we schedule the pour. Not ready? Keep the estimate for budgeting &mdash; no follow-up pressure.</p></li>
    </ol>
  </div>
</section>
""",
)


def main():
    import os

    out_dir = os.path.dirname(os.path.abspath(__file__))
    for path, cfg in PAGES.items():
        html = page(
            path=path,
            title=cfg["title"],
            desc=cfg["desc"],
            og_image=cfg["og_image"],
            extra_head=cfg["extra_head"],
            body=cfg["body"],
            breadcrumb_name=cfg["breadcrumb"],
        )
        fname = os.path.join(out_dir, path.lstrip("/"))
        with open(fname, "w") as f:
            f.write(html)
        print("wrote", fname)


if __name__ == "__main__":
    main()
