# Store app prototype: research and spec (14 Nov 2026)

## What exists today (from public sources)

| Feature | Glovo partner app (Orders app / GoDroid / Manager Portal) | Others |
|---|---|---|
| Accepting orders | Store accepts in the Orders app. Auto-accept found only via POS integrations (e.g. Last.app), not confirmed as a native setting | Uber Eats: green flashing screen + sound for new orders |
| Prep time | Estimated from past orders; store can raise it **before accepting**, not after. Raising it delays the courier. Busy Mode adds time to all new orders | Uber Eats: predicted prep time, editable; busy mode adds 10–20 min |
| Order ready | **Mark as ready** button sends the courier sooner | — |
| Courier wait | Countdown after acceptance; "avoidable courier wait time" = courier waiting after prep time ends | — |
| Courier ETA / map | Customer app has live map + countdown. No public evidence of a map on the partner side | Uber Eats: store sees courier photo and ETA once assigned |
| Contacts | Not documented publicly | Uber Eats: contact customer from the order |
| Out of stock | Deactivate products in Menu Manager (mobile/desktop); grocery partners can sync stock via integrations/API | Just Eat: Item availability toggle, "back tomorrow" or "off the menu indefinitely" |
| Substitutions | Not documented publicly for partners | Just Eat Orderpad: search and pick a substitute, customer accepts. Deliveroo: mark item out of stock from "Manage order" after acceptance; customer chooses replacement; a decline does not count as a store cancellation |

Sources:
- Glovo prep time, Mark as ready, avoidable wait: https://sell.glovoapp.com/ng/en/?p=703
- Glovo Orders app / GoDroid: https://sell.glovoapp.com/ke/en/resource/tutorials-and-tips/category/orders-app , https://sell.glovoapp.com/ug/en/resource/tutorials-and-tips/category/godroid
- Glovo Manager Portal / Menu Manager: https://sell.glovoapp.com/ke/en/resource/tutorials-and-tips/category/manager-portal
- Glovo grocery stock integrations: https://qcommerce-integrations.glovoapp.com
- Auto-accept via POS (third party): https://help.last.app/portal/en/kb/articles/integrations-glovo
- Just Eat item availability: https://www.just-eat.ie/partner-blog/?p=573
- Just Eat substitution feature: https://extrahelpings.just-eat.ie/new-substitution-feature-reduces-need-refunds
- Deliveroo restaurant substitutions: https://help.deliveroo.com/en/articles/10156329-item-substitutions-restaurant-only
- Uber Eats Orders app: https://merchants.ubereats.com/gb/en/resources/learning-center/uber-eats-orders-app/

## Proposed store app (prototype spec)

Device: store tablet, landscape. Look: Glovo-style yellow and green, rounded cards. No Glovo logo; labelled "Concept".

Layout: left nav (Orders, Stock, Insights, Help) · top bar (store name, Open/Paused, Busy mode) · main area.

1. **Live orders board.** Columns: Preparing · Ready, courier coming · Picked up. A new order slides in with a sound and a banner: "New order #A7F2 · auto-accepted". No accept/reject buttons.
2. **Order card / detail.**
   - Items as a pick list with tick boxes, diet tags (Vegan, GF), notes.
   - **8:00 prep timer** ring counting down. Big **Mark as ready** button. Line under it: "Courier is sent automatically at 0:00."
   - **+5 min** button, only in the first 60 seconds (Glovo today only allows changes before accepting; auto-accept needs this window).
   - After ready: "Courier wait" countdown, so the store sees avoidable wait.
3. **Contacts panel** (in the order detail):
   - Customer: first name, masked call + chat.
   - Courier: appears once a courier accepts: name, vehicle, masked call + chat.
   - Glovo support: chat + phone, with order number pre-filled.
4. **Courier tracking card:** small map with the store pin and courier pin, ETA "arrives in 4 min", steps: Finding courier → Assigned → On the way → At store → Picked up.
5. **Substitution flow:** tap an item → "Out of stock" → 2–3 suggested substitutes (same category, fits the customer's preference, similar price) → "Send to customer" → status "Waiting for customer (2:00)" → toast "Customer accepted Almond drink" or "Customer declined: item refunded". Marking it out of stock also updates the catalogue (step 6).
6. **Stock alerts and auto-removal:**
   - Toast: "Oat drink: 2 left" → Restock / Mark out of stock.
   - When an item is reported out of stock (or hits 0 in synced stock), it is removed from the menu automatically, with "Back tomorrow" or "Until I turn it on" (Just Eat style).
   - Stock screen: search, category filter, on-shelf count, Low/Out badges, availability toggle.
7. **Everything else:** Busy mode (+10 / +20 min), Pause store, notification centre (new order, courier assigned, courier 2 min away, courier waiting, substitute accepted/declined, low stock, item hidden, support reply), order history and missing-item claims, daily summary (orders, avg prep time, avoidable wait, substitutions accepted, refunds), sound and printer settings.

## Open questions to confirm with Glovo
- Is auto-accept available natively, or only through POS integrations?
- With auto-accept, how should the store extend prep time if it is busy?
- Does the partner app show the courier on a map, or only an ETA?
- How do stores contact customers and couriers (masked calls, chat)?
- Is there a store-side substitution flow today for restaurants and groceries?
