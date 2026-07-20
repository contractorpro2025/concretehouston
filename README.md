# Jerson's Concrete Houston Parking Lot Repair — Website

Static site (plain HTML/CSS, no build step) for concretehouston.org.
Hosted free on **GitHub Pages** with DNS on **Cloudflare**.

## What's in here

| File / folder | Purpose |
|---|---|
| `index.html` | Homepage — targets "parking lot repair Houston" |
| `parking-lot-repair.html` | Primary service page |
| `commercial-concrete.html`, `industrial-concrete.html`, `civil-concrete.html`, `residential-concrete.html`, `ready-mix-delivery.html` | Service pages |
|  Supporting pages | Supporting pages |
| `css/style.css` | All styles, mobile-first |
| `js/site.js` | Mobile menu toggle (only JS on the site) |
| `images/*.svg` | One illustration per page — replace with real photos when ready |
| `sitemap.xml`, `robots.txt`, `llms.txt` | SEO + AI crawler files |
| `CNAME` | Tells GitHub Pages your custom domain |
| `404.html` | Not-found page |
| `build_pages.py` | Optional generator for the subpages (edit once, rebuild all). You can also edit the HTML files directly. |

## Step 1 — Put it on GitHub

1. Create a free account at github.com if you don't have one.
2. Click **New repository**. Name it anything (e.g. `concretehouston`). Keep it **Public**.
3. On the empty repo page, click **uploading an existing file** and drag ALL the
   files and folders from this project in. Commit.
4. Go to **Settings → Pages**. Under "Build and deployment," set Source to
   **Deploy from a branch**, branch **main**, folder **/ (root)**. Save.
5. Within a minute or two your site is live at `https://YOURUSERNAME.github.io/concretehouston/`.

## Step 2 — Connect the domain through Cloudflare

1. Add `concretehouston.org` as a site in your Cloudflare account (free plan is fine)
   and point your domain registrar's nameservers at Cloudflare if you haven't already.
2. In Cloudflare **DNS**, add these records:
   - `CNAME` | Name: `www` | Target: `YOURUSERNAME.github.io` | Proxy: **DNS only** (gray cloud) at first
   - `A` records for the apex `concretehouston.org` pointing to GitHub Pages IPs:
     `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`
3. Back in GitHub **Settings → Pages**, enter `www.concretehouston.org` in the
   Custom domain box (the `CNAME` file in this repo keeps it set). Check
   **Enforce HTTPS** once the certificate appears (can take up to an hour).
4. In Cloudflare **SSL/TLS**, set mode to **Full**. Add a redirect rule so
   `concretehouston.org` → `https://www.concretehouston.org` (Rules → Redirect Rules).
5. Optional: after HTTPS works, you can flip the `www` record to Proxied (orange cloud).

## Step 3 — Make the contact form work

The form on `contact.html` needs a form service (GitHub Pages can't process forms):
1. Sign up free at **formspree.io**, create a form, copy your form ID.
2. In `contact.html`, replace `YOUR_FORM_ID` in the form's `action` attribute.
3. Submissions will arrive in your email.

## Step 4 — After launch

- Add the site to **Google Search Console** and submit `sitemap.xml`.
- Set the Website field on your Google Business Profile to `https://www.concretehouston.org`.
- Replace the SVG illustrations in `/images` with real jobsite photos (keep the
  same filenames and the descriptive `alt` text pattern — real photos convert
  better and rank better in image search).
- To edit subpages: either edit the `.html` files directly, or edit
  `build_pages.py` and run `python3 build_pages.py` to regenerate them all
  with a consistent header/footer.
