# Feature 001: Fewer stock-out failures without unwanted substitutes

<!-- Spec-driven development (DS403 session 6, 10): what and why, never how. Written before any code. -->

## Why
On a delivery app, some orders contain an item the store no longer has. In the synthetic baseline, 18.0% of
orders hit at least one out-of-stock item (25.2% at stores that update stock by hand, 11.1% at stores with
synced stock), and a substitute that does not fit the shopper's preference is accepted only 17.3% of the time
(84.6% when it fits). Refunds go with lower ratings and fewer repeat orders. *(Kind: assumed — synthetic data,
see `research/ledger.csv`.)*

## Who
Partner stores (grocery and convenience) that sell through a delivery platform, and their customers,
especially customers with a stated preference (vegan, gluten-free).

## What
- An item reported out of stock comes off the menu automatically, until tomorrow or until staff turn it back on.
- Staff are alerted when an item is down to its last 2 units.
- When an item is missing, the substitutes offered first are those that fit the customer's preference.
- The customer accepts or declines a substitute in one step; a decline or no answer refunds the item.

## User scenarios (Given / When / Then)
1. **Preference-matched substitute (P1).** Given a vegan customer whose oat drink is out of stock, and almond
   drink (vegan) and whole milk (not vegan) on the shelf, when the store opens the substitute list, then almond
   drink is listed before whole milk.
2. **Auto-removal (P1).** Given an item with 1 unit left, when an order takes the last unit, then the item is no
   longer orderable and staff see why and until when.
3. **Low-stock alert (P2).** Given an item with 3 units, when an order takes 1, then staff get one alert for that
   item; a second order that takes another unit does not send a second alert.
4. **Decline refunds (P1).** Given a substitute sent to the customer, when the customer declines or does not
   answer within 2 minutes, then the original item is refunded and the substitute goes back to the shelf.

## Edge cases
- No item in the same group is in stock → no substitute is offered; the item is refunded.
- Customer has no preference → every same-group item fits.
- Stock count says 1 but the shelf is empty → staff report it out of stock; the same rules apply.

## Functional requirements
- **FR-001** The system MUST list substitutes that fit the customer's preference before those that do not.
- **FR-002** The system MUST make an item unorderable when its stock reaches 0 or it is reported out of stock.
- **FR-003** The system MUST send one low-stock alert per item when stock first drops to 2 or fewer.
- **FR-004** The system MUST refund an item whose substitute is declined or unanswered after 2 minutes.
- **FR-005** The analysis MUST report the stock-out rate, acceptance by fit, and refunds per 1,000 orders from
  order-line data.

EARS: WHEN a store reports an item out of stock THE SYSTEM SHALL remove the item from the menu and list
same-group substitutes that fit the customer's preference first.

## Success criteria
- **SC-001** Orders hit by a stock-out fall from 18.0% toward the synced-store rate (11.1%) in a pilot.
- **SC-002** Substitute acceptance rises from 65% toward 85%.
- **Guardrail:** order rating and 14-day repeat rate do not fall.
- **Kill criterion:** if a 4-week pilot shows no drop in refunds per 1,000 orders, drop fix 3 and keep 1–2.

## Out of scope
Courier pay and labour policy; machine-learning models; a production dashboard; payment changes.

## Open questions
- [NEEDS CLARIFICATION: do partner stores update availability by hand today, or sync from their till?]
- [NEEDS CLARIFICATION: is substitute acceptance recorded per item?]
