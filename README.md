# Living Tamil California — Website package

Owner account: livingtamilcalifornia@gmail.com
This Google Drive folder ("Website") is the **single source** for the live website.
Nobody edits the live site directly. Changes are made here, versioned, then published.

## Roles

| Person | Role on the website |
|---|---|
| **Balajee Gurumoorthy — Secretary** | Reviews all content before it goes live, edits content when needed, and publishes the site (hosting and domain) |
| Padmanaba PS Pillai — Treasurer | Prepares changes and releases; owns Donate page, Zeffy and donation tracking |
| Board | Approves policy pages (Privacy, Donation Policy) and mission text |

## What is in this folder

| Item | What it is |
|---|---|
| `README` (this file) | Deployment and update instructions |
| `CHANGELOG` | What changed in each version |
| `Current/` | The zip of the version that should be live right now (only one file here) |
| `Releases/` | Every version ever published, never deleted: `livingtamil-website-vX.Y.Z-DATE.zip` |
| `Proposed changes/` | Drop requests here (a Google Doc, photos, new text) for the next version |

Inside each zip:

| Folder | What it is |
|---|---|
| `site/` | **The website itself. This is the folder you publish.** Plain HTML/CSS/JS — no build step |
| `tools/` | Python scripts used to regenerate parts of the site (Reading Archive, writers ribbon) |
| `README.md`, `CHANGELOG.md`, `VERSION` | Same as above, frozen for that version |

## First-time deployment (for Balajee)

Before publishing, **review the content** (Step 0): unzip, open `site/index.html` in a browser
and read every page. If something needs changing, see "If Balajee edits the content" below.

Recommended host: **Cloudflare Pages** or **Netlify** (both free, HTTPS included).
Sign up with livingtamilcalifornia@gmail.com so the org owns the hosting account.

### Netlify (simplest)
1. Download the zip from `Current/` and unzip it.
2. Go to app.netlify.com → sign up with the org Gmail → **Add new site → Deploy manually**.
3. Drag the **`site`** folder (not the whole zip folder) onto the page. Done — it gives a test URL.
4. Open the test URL and check: Home, Reading Archive, Join form, Donate form.
5. **Domain settings → Add custom domain** → enter the domain (e.g. livingtamilcalifornia.org)
   and follow the DNS instructions at the registrar. HTTPS is issued automatically.

### Cloudflare Pages (alternative)
1. dash.cloudflare.com → Workers & Pages → Create → Pages → **Upload assets**.
2. Project name `livingtamil` → upload the **`site`** folder → Deploy.
3. Custom domains → add the domain.

Both hosts read the `_headers` file in `site/` automatically (security headers). Keep it.

## Things that already work and need no setup
These run in the org Google account and are not part of the hosting:

| Feature | Where it lives (org account) |
|---|---|
| Join / WhatsApp forms | Apps Script web app bound to *Membership → Living Tamil – Website Sign-ups* sheet |
| Reading Archive "Newly added" | Apps Script project *Living Tamil YouTube Feed* (reads the YouTube channel) |
| Donations | Zeffy form embedded on Donate page; *Zeffy Donation Logger* script in the *Donations & Zeffy Payouts* sheet logs each donation hourly and saves receipts to *Finance/Donation Receipts* |

The web-app URLs are already inside the HTML. If a script is ever redeployed, use
**Manage deployments → Edit → New version** so the URL stays the same.
Never "New deployment" (it creates a new URL and the forms break).

## How updates work from now on (version control)

1. **Request** — anyone puts the requested change in `Proposed changes/` (or emails the Board).
2. **Make the change** — the editor (Padmanaba, or Claude working for him) edits the
   working copy on the Mac (`~/workspace/livingtamil-website`) and tests it.
3. **Version it** — bump `VERSION`, add an entry at the top of `CHANGELOG.md`
   (date, who, what changed).
4. **Release** — zip as `livingtamil-website-vX.Y.Z-YYYY-MM-DD.zip`, put it in `Releases/`,
   and replace the file in `Current/` with it. Update the CHANGELOG doc in this folder.
5. **Notify** — email Balajee: "Version X.Y.Z is ready in Website/Current".
6. **Review** — Balajee (Secretary) reviews the content. He either approves it, or edits it
   himself (see below), or sends it back with comments.
7. **Publish** — Balajee downloads `Current/`, unzips, and in Netlify uses
   **Deploys → drag the `site` folder** (Cloudflare: **Create new deployment**).
8. **Confirm** — check the live site, then reply "X.Y.Z live on <date>".

### If Balajee edits the content
Edits are welcome — they just need to go through the same versioning so nothing is lost:
1. Unzip the version from `Current/`, edit the files in `site/` (any text editor; pages are
   plain HTML — change only the text between the tags).
2. Open the page in a browser to check it.
3. Raise the version (e.g. 1.0.0 → 1.0.1), add a line at the top of `CHANGELOG.md`:
   date, "Balajee", what changed.
4. Zip the folder as `livingtamil-website-v1.0.1-YYYY-MM-DD.zip`, put it in `Releases/`,
   and replace the file in `Current/`. Update the CHANGELOG in this folder too.
5. Publish it, and let Padmanaba know so his working copy on the Mac is updated from
   `Current/` before the next change.

Always start from the newest zip in `Current/`, never from an older copy.

Rules:
- The live site must always equal the zip in `Current/`.
- Never delete an old release. To **roll back**, re-deploy the previous zip from `Releases/`
  (Netlify also keeps old deploys: Deploys → pick one → *Publish deploy*).
- One version at a time; do not edit files directly on the host.

## Regular automatic tasks
- 20th of each month: a scheduled check of the YouTube channel for new recordings to
  add to the Reading Archive. New videos also appear automatically in "Newly added".
- Hourly: Zeffy donation emails → Donations tracker.

## Contacts
- Preparing changes and releases: Padmanaba PS Pillai, Treasurer
- Content review, edits and publishing (hosting and domain): Balajee Gurumoorthy, Secretary
- Org email: livingtamilcalifornia@gmail.com
