# Wainwright Realty CMS — Setup Guide
## One-Time Setup (~15 minutes)

---

## STEP 1: Create a GitHub Account (if you don't have one)

1. Go to **github.com**
2. Click **Sign up** (top right)
3. Use davewjr7@gmail.com as your email
4. Pick a username — something like **dwainwrightrealty** or **davewjr7**
5. Verify your email

> If you already have a GitHub account, skip to Step 2.

---

## STEP 2: Create a New Repository

1. Once logged in to GitHub, click the **+** icon (top right) → **New repository**
2. Name it: `dwainwright-realty-nj`
3. Set it to **Private** (your site files stay yours)
4. Click **Create repository**

---

## STEP 3: Upload Your Site Files to GitHub

1. On the new repo page, click **uploading an existing file** (or drag files in)
2. Upload EVERYTHING from your site package zip — the whole folder structure:
   - `admin/`
   - `site/`
   - `scripts/`
   - `netlify.toml`
   - `build.py` (your existing file)
   - `build_pages.py` (your existing file)
   - Any other files at the root
3. Scroll down and click **Commit changes**

---

## STEP 4: Connect Netlify to GitHub

1. Go to **netlify.com** and log in (Google → davewjr7@gmail.com)
2. Open your **dwainwright-realty-nj** site
3. Go to **Site settings** → **Build & deploy** → **Continuous deployment**
4. Click **Link site to Git**
5. Choose **GitHub** → authorize it → select the `dwainwright-realty-nj` repo
6. Set:
   - **Branch**: `main`
   - **Build command**: `python scripts/build_posts_index.py`
   - **Publish directory**: `site`
7. Click **Save**

> From now on, every time content is saved through the CMS, Netlify automatically rebuilds and redeploys the site. No more zip uploads needed.

---

## STEP 5: Enable Netlify Identity

1. Still in Netlify, go to **Integrations** → search **Identity** → click **Enable**
   (or go to your site → **Identity** tab → **Enable Identity**)
2. Under **Registration preferences** → change to **Invite only**
   (so only people you invite can create accounts)
3. Scroll down to **Services** → **Git Gateway** → click **Enable Git Gateway**

---

## STEP 6: Invite Users

1. Still on the Identity tab, click **Invite users**
2. Enter: `dave@dwainwrightrealty.com` → **Send invite**
3. Enter your assistant's email address → **Send invite**
4. Both of you will get an email — click the link in the email to set your password

---

## STEP 7: Log in to the Admin Panel

1. Go to **dwainwrightrealty.com/admin/**
2. Click **Login with Netlify Identity**
3. Enter your email and the password you just created
4. You're in!

---

## HOW TO WRITE A BLOG POST (for your assistant)

1. Go to `dwainwrightrealty.com/admin/`
2. Log in
3. Click **Market Insights / Blog** in the left sidebar
4. Click **New Post** (top right)
5. Fill in:
   - **Title** — clear and specific
   - **Publish Date** — today's date
   - **Category** — pick from the dropdown
   - **Featured Image** — upload a photo (recommended: 1200×630px)
   - **Summary** — 2-3 sentences for the listing page preview
   - **Body** — write the full post using the rich text editor
6. When done, click **Save** (drafts) or **Publish** → then **Publish now**
7. Netlify auto-deploys in about 60 seconds. The post is live.

---

## NEED HELP?

For layout changes, new page sections, graphics, or anything structural —
that still comes to Claude (Dave's AI assistant in claude.ai).

For content updates (blog posts, text changes, photo swaps) —
use this admin panel.
