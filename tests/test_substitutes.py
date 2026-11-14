"""Acceptance tests for spec 001, scenario 1 and its edge cases (FR-001).
Written before the code: run `python -m pytest -q` and see them fail first."""
from shelfsync.substitutes import rank_substitutes

SHELF = [
    {"name": "Oat drink 1 L", "group": "milk", "tags": ["vegan"], "price": 1.95, "stock": 0},
    {"name": "Whole milk 1 L", "group": "milk", "tags": ["gf"], "price": 1.15, "stock": 12},
    {"name": "Almond drink 1 L", "group": "milk", "tags": ["vegan", "gf"], "price": 2.10, "stock": 4},
    {"name": "Hummus 200 g", "group": "dip", "tags": ["vegan", "gf"], "price": 1.90, "stock": 7},
]


def test_vegan_customer_gets_vegan_substitute_first():
    # Given a vegan customer whose oat drink is out of stock
    # When the store opens the substitute list
    names = [item["name"] for item in rank_substitutes("Oat drink 1 L", SHELF, "vegan")]
    # Then almond drink (vegan) is listed before whole milk (not vegan)
    assert names.index("Almond drink 1 L") < names.index("Whole milk 1 L")


def test_only_items_from_the_same_group_are_suggested():
    names = [item["name"] for item in rank_substitutes("Oat drink 1 L", SHELF, "vegan")]
    assert "Hummus 200 g" not in names


def test_out_of_stock_items_are_never_suggested():
    shelf = [dict(item) for item in SHELF]
    shelf[2]["stock"] = 0  # almond drink sold out too
    names = [item["name"] for item in rank_substitutes("Oat drink 1 L", shelf, "vegan")]
    assert names == ["Whole milk 1 L"]


def test_no_substitute_when_nothing_in_the_group_is_in_stock():
    assert rank_substitutes("Hummus 200 g", SHELF, "vegan") == []


def test_customer_without_preference_gets_closest_price_first():
    # Oat drink costs 1.95: almond (2.10) is closer than whole milk (1.15)
    names = [item["name"] for item in rank_substitutes("Oat drink 1 L", SHELF, "none")]
    assert names == ["Almond drink 1 L", "Whole milk 1 L"]
