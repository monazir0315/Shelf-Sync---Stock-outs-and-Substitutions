"""
Make a SYNTHETIC (made-up) dataset of delivery orders for practice.

Why synthetic: real order data from a delivery company is private, and the public Kaggle datasets
need a login. This script creates realistic-looking data with simple, stated rules, so the analysis
in the notebook can be built and checked now and rerun on real data later.

Rules the data follows (all invented, for illustration only):
- 8 stores in Barcelona. 4 update their stock by hand ("manual"), 4 have stock synced from the till ("synced").
- Manual stores, evenings, weekends and some popular vegan items run out more often.
- When an item is missing, the store sends a substitute from the same group, picked without looking at the
  customer's preference. A substitute that fits the preference is accepted 85% of the time, one that does
  not fit only 15% of the time. Declined substitutes are refunded.
- Customers who get a refund order less often for the next 14 days.

Run:  python generate_data.py      ->  writes order_lines.csv next to this file
"""
import csv
import random
from datetime import date, timedelta

random.seed(2026)  # same "random" data every time

# ---------- Stores ----------
STORES = [
    ("S01", "Gràcia", "manual"), ("S02", "Eixample", "synced"), ("S03", "Sants", "manual"), ("S04", "Poblenou", "synced"),
    ("S05", "Sant Andreu", "manual"), ("S06", "Les Corts", "synced"), ("S07", "El Born", "manual"), ("S08", "Sarrià", "synced"),
]

# ---------- Products: name, category, group (for substitutes), price, tags, popularity, extra stock-out risk ----------
PRODUCTS = [
    ("Oat drink 1 L", "Dairy & alternatives", "milk", 1.95, "vegan", 9, 1.8),
    ("Whole milk 1 L", "Dairy & alternatives", "milk", 1.15, "gf", 12, 0.8),
    ("Almond drink 1 L", "Dairy & alternatives", "milk", 2.10, "vegan gf", 5, 1.2),
    ("Greek yogurt 500 g", "Dairy & alternatives", "yogurt", 2.30, "gf", 7, 1.0),
    ("Coconut yogurt 400 g", "Dairy & alternatives", "yogurt", 2.90, "vegan gf", 4, 1.5),
    ("Sourdough loaf", "Bakery", "bread", 2.80, "vegan", 8, 1.3),
    ("Gluten-free loaf", "Bakery", "bread", 3.40, "vegan gf", 3, 1.6),
    ("Butter croissant", "Bakery", "pastry", 1.40, "", 10, 1.4),
    ("Firm tofu 400 g", "Fridge", "protein", 2.40, "vegan gf", 5, 1.4),
    ("Chicken breast 500 g", "Fridge", "protein", 4.90, "gf", 9, 0.9),
    ("Hummus 200 g", "Fridge", "dip", 1.90, "vegan gf", 7, 1.0),
    ("Tzatziki 200 g", "Fridge", "dip", 2.10, "gf", 4, 1.0),
    ("Plant burgers x2", "Fridge", "burger", 3.80, "vegan", 5, 1.7),
    ("Beef burgers x2", "Fridge", "burger", 3.50, "", 7, 0.9),
    ("Falafel salad bowl", "Ready to eat", "meal", 6.50, "vegan", 6, 1.2),
    ("Chicken Caesar wrap", "Ready to eat", "meal", 5.20, "", 8, 1.0),
]

# ---------- Customers ----------
CUSTOMERS = []
for i in range(1, 1501):
    r = random.random()
    pref = "vegan" if r < 0.22 else ("gf" if r < 0.34 else "none")
    CUSTOMERS.append({"id": f"C{i:04d}", "pref": pref, "store": random.choice(STORES), "cooldown_until": None})


def fits(tags, pref):
    """True if a product with these tags suits a customer with this preference."""
    return pref == "none" or pref in tags.split()


def stockout_chance(store_method, hour, weekday, risk):
    chance = 0.03 * risk
    if store_method == "manual":
        chance = chance * 2.2
    if hour >= 19:
        chance = chance * 1.6
    if weekday >= 5:  # Saturday or Sunday
        chance = chance * 1.3
    return min(chance, 0.4)


start = date(2026, 10, 1)
days = 28
rows = []
order_no = 0

for d in range(days):
    day = start + timedelta(days=d)
    weekday = day.weekday()  # Monday = 0
    for cust in CUSTOMERS:
        # Base chance of ordering today, lower for 14 days after a refund
        p = 0.15 if weekday >= 4 else 0.12
        if cust["cooldown_until"] and day <= cust["cooldown_until"]:
            p = p * 0.6
        if random.random() > p:
            continue

        order_no += 1
        order_id = f"O{order_no:05d}"
        hour = random.choices(range(9, 23), weights=[2, 3, 4, 8, 9, 6, 4, 3, 4, 7, 9, 9, 6, 3])[0]
        store_id, area, method = cust["store"]

        # The customer picks 1-4 products that fit their preference
        choices = [p_ for p_ in PRODUCTS if fits(p_[4], cust["pref"])]
        weights = [p_[5] for p_ in choices]
        n_items = random.choice([1, 2, 2, 3, 3, 4])
        basket = []
        while len(basket) < min(n_items, len(choices)):
            item = random.choices(choices, weights=weights)[0]
            if item not in basket:
                basket.append(item)

        order_lines = []
        bad_experience = False
        any_substitute = False
        for name, cat, grp, price, tags, pop, risk in basket:
            qty = 2 if random.random() < 0.15 else 1
            line = {
                "order_id": order_id, "date": day.isoformat(), "weekday": day.strftime("%A"), "hour": hour,
                "store_id": store_id, "area": area, "stock_method": method,
                "customer_id": cust["id"], "customer_pref": cust["pref"],
                "product": name, "category": cat, "price": price, "qty": qty,
                "out_of_stock": "no", "substitute": "", "substitute_fits_pref": "",
                "outcome": "packed", "refund_eur": 0.0,
            }
            if random.random() < stockout_chance(method, hour, weekday, risk):
                line["out_of_stock"] = "yes"
                options = [p_ for p_ in PRODUCTS if p_[2] == grp and p_[0] != name]
                if not options:
                    line["outcome"] = "refunded_no_substitute"
                    line["refund_eur"] = round(price * qty, 2)
                    bad_experience = True
                else:
                    sub = random.choice(options)  # today: store picks any item from the same group
                    ok = fits(sub[4], cust["pref"])
                    line["substitute"] = sub[0]
                    line["substitute_fits_pref"] = "yes" if ok else "no"
                    accept_chance = 0.85 if ok else 0.15
                    if random.random() < accept_chance:
                        line["outcome"] = "substitute_accepted"
                        any_substitute = True
                    else:
                        line["outcome"] = "substitute_declined"
                        line["refund_eur"] = round(price * qty, 2)
                        bad_experience = True
            order_lines.append(line)

        # Order rating: 70% of customers leave one
        rating = ""
        if random.random() < 0.7:
            score = 4.6 + random.gauss(0, 0.5)
            if any_substitute:
                score = score - 0.3
            if bad_experience:
                score = score - 1.3
            rating = max(1, min(5, round(score)))
        for line in order_lines:
            line["order_rating"] = rating
            rows.append(line)

        if bad_experience:
            cust["cooldown_until"] = day + timedelta(days=14)

# ---------- Did the customer order again within 14 days? ----------
orders_by_customer = {}
for line in rows:
    orders_by_customer.setdefault(line["customer_id"], set()).add((line["date"], line["order_id"]))
last_day = start + timedelta(days=days - 1)
for line in rows:
    this_day = date.fromisoformat(line["date"])
    if this_day > last_day - timedelta(days=14):
        line["ordered_again_within_14d"] = ""  # not enough days left to know
        continue
    later = [d_ for d_, o in orders_by_customer[line["customer_id"]]
             if this_day < date.fromisoformat(d_) <= this_day + timedelta(days=14)]
    line["ordered_again_within_14d"] = "yes" if later else "no"

with open("order_lines.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
    writer.writeheader()
    writer.writerows(rows)

print(f"Wrote {len(rows)} order lines from {order_no} orders to order_lines.csv")
