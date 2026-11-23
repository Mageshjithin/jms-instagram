# JMS Textiles – Instagram posts

Public photo hosting for @jms.textiles. Instagram needs public image links.

- `queue/<YYYY-MM-DD-name>/` — ready to post: `1.jpg`…`10.jpg` (or `.mp4` videos, also 1080x1350) (already branded, 1080x1350) + `caption.txt`.
- `posted/<folder>/` — moved here after posting; `posted.txt` records the Instagram media id.
- `tools/brand.py` — adds the JMS Textiles banner + order number (78459 99726).

The daily scheduled task posts the **oldest** folder in `queue/` (one post per day) as a carousel
(or single image if only one photo), then moves it to `posted/`. Empty queue → nothing is posted.

- `tags.txt` — Instagram usernames (one per line, no @) tagged on every new post (max 20).

- Reels style: **full-screen template** (owner chose option 1 on 2026-11-23) — see `tools/templates/reel_templates.py` (overlay A).
