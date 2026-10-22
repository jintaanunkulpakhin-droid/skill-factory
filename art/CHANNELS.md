# Where the art is sold

| Channel | How it gets there | Your part |
|---|---|---|
| Gumroad | Weekly run publishes it | Nothing |
| Printify (mugs, tote bags) | Weekly run creates the products by API in the Printify Pop-Up Store (and Etsy once connected in Printify) | Once: Printify account, `PRINTIFY_API_TOKEN` in the cloud environment, `api.printify.com` in Allowed domains |
| Pinterest | Weekly run schedules a pin per bundle through Metricool, linking to Gumroad | Once: connect Pinterest in Metricool and make a board named "Thai Clip Art" |
| Etsy | The PC builds a kit in Drive: `outputs/thai-art/<slug>/kits/etsy/` | About 3 minutes per bundle, below |
| Adobe Stock | The PC builds a kit in Drive: `outputs/thai-art/<slug>/kits/adobe/` | About 3 minutes per bundle, below |
| Dreamstime | The PC builds a kit in Drive: `outputs/thai-art/<slug>/kits/dreamstime/` | About 3 minutes per bundle, below |

## Etsy (until Etsy approves API access)
1. Shop Manager > Listings > Add a listing.
2. Photos: the cover and thumbnail PNGs. Type: Digital files.
3. Copy the title, tags, price and description from `ETSY.txt`. Tick the AI box and choose
   "Designed by".
4. Digital files: upload the zip. Publish.

## Adobe Stock
Adobe Stock only accepts AI images through its contributor portal, with the AI box ticked.
1. contributor.stock.adobe.com > Upload: drag in all the JPGs from the `adobe` folder.
2. Upload CSV: pick `adobe_stock.csv` (fills titles, keywords and category).
3. Select all > tick "Created using generative AI tools" > Submit.
Each image is sold on its own, so the same bundle keeps earning a little over time.

## Dreamstime
1. dreamstime.com > Upload: add all the JPGs from the `dreamstime` folder.
2. For each file use the title, description and keywords from `dreamstime.csv`, and choose
   the category "AI generated illustrations" (required for AI images). Submit.

## Not used
- Shutterstock, Getty Images, Canva: don't accept AI-made images from contributors.
- Wirestock: stopped sending new uploads to other stock sites in January 2026.
- LINE Creators Market: needs sticker sets made by hand; worth it once a style sells.
