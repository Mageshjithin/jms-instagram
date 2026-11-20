# JMS Textiles – Instagram posts

Public photo hosting for @jms.textiles. Instagram needs public image links.

- `queue/<YYYY-MM-DD-name>/` — ready to post: `1.jpg`…`10.jpg` (already branded, 1080x1350) + `caption.txt`.
- `posted/<folder>/` — moved here after posting; `posted.txt` records the Instagram media id.
- `tools/brand.py` — adds the JMS Textiles banner + order number (78459 99726).

The daily scheduled task posts the **oldest** folder in `queue/` (one post per day) as a carousel
(or single image if only one photo), then moves it to `posted/`. Empty queue → nothing is posted.
