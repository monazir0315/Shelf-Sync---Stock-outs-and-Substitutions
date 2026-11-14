# Directive: Shelf Sync (store app for stock-outs and substitutions)

<!--
DRAFT proposed by Claude on 2026-11-14 from the PRD and the two prototypes (U2, D10).
The directive belongs to the product owner: edit it, then commit it yourself as its own commit,
outside any wave. Once the first wave has run, do not change it until the loop ends (U1).
-->

## Directive

Shelf Sync helps partner stores on a delivery platform keep what customers can order in line with what is on
the shelf. Orders are accepted automatically and get a fixed prep time; the store is warned before an item runs
out; sold-out items come off the menu on their own; and when an item is missing, the customer is offered a
substitute that fits what they asked for. Store staff decide every substitute they send and every item they take
off the menu; the customer decides whether to accept a substitute; operations teams see totals per store, never
individual customers.

## Invariants (what no wave may break)

- **I1 · The customer decides on substitutes.** No substitute is packed until the customer accepts it; a decline
  or no answer always refunds that item, and the screen says so.
- **I2 · Staff stay in control of the menu.** Every automatic change to the menu says what changed, why and for
  how long, and staff can undo it in one tap.
- **I3 · No order is rejected by the store.** Every order line ends as packed, substituted with the customer's
  consent, or refunded; there is no reject button.
- **I4 · Time is visible.** Every order shows its prep timer and when the courier will be requested; nothing
  requests a courier without the store being told.
- **I5 · Contact without exposing people.** Customers, couriers, stores and support reach each other only through
  masked calls or in-app chat; no screen shows a phone number or address it does not need.
