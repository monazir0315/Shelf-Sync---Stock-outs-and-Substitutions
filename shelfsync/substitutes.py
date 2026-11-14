"""Rank substitutes for a missing item (spec 001, FR-001)."""


def fits(item, preference):
    """True if the item suits the customer's preference ("none" means anything fits)."""
    return preference == "none" or preference in item["tags"]


def rank_substitutes(missing_name, shelf, preference):
    """Return in-stock items from the same group as the missing item.

    Items that fit the customer's preference come first; within each half,
    the item with the closest price comes first.
    """
    missing = None
    for item in shelf:
        if item["name"] == missing_name:
            missing = item
    if missing is None:
        return []

    candidates = []
    for item in shelf:
        same_group = item["group"] == missing["group"]
        is_other_item = item["name"] != missing_name
        in_stock = item["stock"] > 0
        if same_group and is_other_item and in_stock:
            candidates.append(item)

    def sort_key(item):
        not_fitting = 0 if fits(item, preference) else 1  # fitting items first
        price_gap = abs(item["price"] - missing["price"])
        return (not_fitting, price_gap)

    return sorted(candidates, key=sort_key)
