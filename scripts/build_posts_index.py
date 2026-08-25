"""
build_posts_index.py
Reads every .md file in site/blog/posts/, extracts frontmatter,
and writes site/blog/posts/posts.json for the blog listing page.

Run automatically by Netlify on every deploy.
"""

import os
import json
import re

POSTS_DIR = os.path.join("site", "blog", "posts")
OUTPUT    = os.path.join(POSTS_DIR, "posts.json")


def parse_frontmatter(content):
    """Return (meta_dict, body_str) from a Markdown file with YAML frontmatter."""
    if not content.startswith("---"):
        return {}, content
    parts = content.split("---", 2)
    if len(parts) < 3:
        return {}, content
    meta = {}
    for line in parts[1].strip().splitlines():
        idx = line.find(":")
        if idx > 0:
            key = line[:idx].strip()
            val = line[idx + 1:].strip().strip('"').strip("'")
            meta[key] = val
    return meta, parts[2].strip()


def build_index():
    posts = []
    if not os.path.isdir(POSTS_DIR):
        print(f"Posts directory not found: {POSTS_DIR}")
        return

    for filename in os.listdir(POSTS_DIR):
        if not filename.endswith(".md"):
            continue
        slug = filename[:-3]            # strip .md
        filepath = os.path.join(POSTS_DIR, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            raw = f.read()
        meta, _ = parse_frontmatter(raw)

        posts.append({
            "slug":     slug,
            "title":    meta.get("title",    slug.replace("-", " ").title()),
            "date":     meta.get("date",     ""),
            "category": meta.get("category", "Market Update"),
            "summary":  meta.get("summary",  ""),
            "image":    meta.get("image",    ""),
            "author":   meta.get("author",   "David Wainwright Jr."),
            "featured": meta.get("featured", "false").lower() == "true",
        })

    # Sort newest-first
    posts.sort(key=lambda p: p["date"], reverse=True)

    with open(OUTPUT, "w", encoding="utf-8") as f:
        json.dump(posts, f, indent=2, ensure_ascii=False)

    print(f"✓ posts.json — {len(posts)} post{'s' if len(posts) != 1 else ''} indexed")


if __name__ == "__main__":
    build_index()
