"""Analysis metrics for spec 001 (FR-005). Each takes the order-lines table (one row per item ordered)."""


def _orders_with_stockout(lines):
    """One row per order: True if any item in the order was out of stock."""
    is_missing = lines["out_of_stock"] == "yes"
    return is_missing.groupby(lines["order_id"]).any()


def stockout_rate(lines):
    """Percentage of orders with at least one out-of-stock item."""
    return _orders_with_stockout(lines).mean() * 100


def stockout_rate_by(lines, column):
    """Stock-out rate (%) for each value of a column, such as stock_method."""
    per_order = lines.groupby("order_id").agg(group=(column, "first"))
    per_order["hit"] = _orders_with_stockout(lines)
    return per_order.groupby("group")["hit"].mean() * 100


def acceptance_by_fit(lines):
    """Acceptance rate (%) of substitutes that fit the preference ("yes") and that do not ("no")."""
    subs = lines[lines["substitute_fits_pref"].isin(["yes", "no"])]
    accepted = subs["outcome"] == "substitute_accepted"
    return (accepted.groupby(subs["substitute_fits_pref"]).mean() * 100).to_dict()


def refunds_per_1000_orders(lines):
    """Total refunds in euros for every 1,000 orders."""
    n_orders = lines["order_id"].nunique()
    return lines["refund_eur"].sum() / n_orders * 1000
