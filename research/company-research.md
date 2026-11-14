# Glovo: company research (13 Nov 2026)

Use this for the Glovo project, interviews and messages to Paula Fernández / Laura Torrents.

## Snapshot
- Barcelona-born multi-category delivery app, founded 2015 (celebrated 10 years in 2025). Co-founder/CEO Òscar Pierre.
- Owned by Delivery Hero (majority since 2022). Uber announced a takeover offer for Delivery Hero on 16 Jul 2026
  (EUR 41.50/share); the companies run independently until closing.
- ~23 countries: Southern & Eastern Europe, Central Asia, Africa.
- Categories: restaurants, groceries/quick commerce (own dark stores + supermarkets), retail, pharmacy, courier.
  Revenue also from a subscription (Prime) and ads for partners.

## Context in 2025–2026 (talking points)
- Group: quick commerce is ~18% of Delivery Hero GMV, growing ~30% (Q1 2026). DH passed 1bn orders in a quarter (Q3 2026).
- Spain labour model: Glovo moved riders from self-employed to employees (announced Dec 2024, ~14,000 hired by mid-2025).
  Costs: ~EUR 100M hit to 2025 earnings, a EUR 450M Social Security claim (Jul 2025), a ~EUR 79M fine (Feb 2026).
- Mar 2026: redundancy plan for up to 750 riders across 60 Spanish cities, with service reduced in some provinces
  (incl. Barcelona area); riders struck in Apr 2026.
- So what: with salaried riders, **efficiency per rider hour** (orders/hour, idle time, demand forecasting by zone and
  hour) is now a direct cost lever, not just a nice-to-have.

## How Glovo uses data (from their own blog/stories)
- **Dispatch & ETA ("Jarvis")**: assigns orders to couriers in real time; ML + operations research predict prep time,
  travel time and demand.
- **Forecasting**: Bayesian models that share learning across cities, so new cities get good forecasts quickly
  (links delivery time, cancellations and efficiency).
- **Grocery order weight**: deep learning estimates basket weight to plan couriers and handling time.
- **Restaurant tools**: an assistant for partners; restaurants using it grew orders ~15%.
- Typical analyst work around these: cancellations/failed orders, late deliveries, partner performance, Prime
  retention, ads performance, quick-commerce availability & substitutions, rider utilisation.
- Team tools (Paula's profile): SQL, Python, Git, Looker, Power BI.

## Your angle
Greggs delivery story (unfulfilled orders 4% → 0.9%, ~£4M/yr) maps straight onto Glovo's core problems:
failed/late orders and the cost of each delivery.

Project idea candidates (public data only, framed as hypotheses):
1. What drives late or failed deliveries, and which 2 fixes recover the most revenue?
2. Rider utilisation: when and where does supply outrun demand (idle hours), and what's the saving from better shift planning?
3. Quick-commerce: which product categories cause most substitutions/stock-outs, and their effect on repeat orders?

## Sources
- Glovo 10 years: https://about.glovoapp.com/press/glovo-celebrates-10-years
- Delivery Hero Q1 2026 call: https://www.marketbeat.com/instant-alerts/delivery-hero-q1-earnings-call-highlights-2026-04-30/
- DH Q3 2026 (1bn orders): https://retail-news.de/delivery-hero-q3-2026-milliarde-bestellungen-umsatz/
- Glovo Jarvis: https://about.glovoapp.com/stories/hi-this-is-jarvis
- Cross-city Bayesian forecasting: https://medium.com/glovo-engineering/bayesian-modelling-for-cross-city-learning-at-glovo-730924f45308
- Grocery weight model: https://medium.com/data-centric-engineering-blog/automating-supply-chains-how-heavy-is-my-shopping-7070dafa33dd
- Riders become employees: https://abcnews.go.com/Business/wireStory/drivers-spanish-food-delivery-app-glovo-become-full-116377082
- EUR 450M Social Security claim: https://apps.eurofound.europa.eu/platformeconomydb/glovo-faces-450m-spanish-social-security-bill-for-misclassifying-riders-110271
- 750 layoffs: https://en.ara.cat/economy/glovo-plans-to-lay-off-750-workers-in-spain_1_5675089.amp.html
- Note: some Q2/Q3 2026 figures come from trade press; check ir.deliveryhero.com before quoting numbers.
