"""Tests for the analysis metrics in spec 001 (FR-005). Small hand-made tables, so the right answer is known."""
import pandas as pd
import pytest

from shelfsync.metrics import acceptance_by_fit, refunds_per_1000_orders, stockout_rate, stockout_rate_by


def make_lines():
    # 4 orders. O1 has one missing item out of two; O3's only item is missing; O2 and O4 are fine.
    return pd.DataFrame([
        {"order_id": "O1", "stock_method": "manual", "out_of_stock": "yes", "substitute_fits_pref": "no", "outcome": "substitute_declined", "refund_eur": 2.0},
        {"order_id": "O1", "stock_method": "manual", "out_of_stock": "no", "substitute_fits_pref": None, "outcome": "packed", "refund_eur": 0.0},
        {"order_id": "O2", "stock_method": "manual", "out_of_stock": "no", "substitute_fits_pref": None, "outcome": "packed", "refund_eur": 0.0},
        {"order_id": "O3", "stock_method": "synced", "out_of_stock": "yes", "substitute_fits_pref": "yes", "outcome": "substitute_accepted", "refund_eur": 0.0},
        {"order_id": "O4", "stock_method": "synced", "out_of_stock": "no", "substitute_fits_pref": None, "outcome": "packed", "refund_eur": 0.0},
    ])


def test_stockout_rate_counts_orders_not_items():
    # 2 of 4 orders had at least one missing item
    assert stockout_rate(make_lines()) == pytest.approx(50.0)


def test_stockout_rate_by_stock_method():
    rates = stockout_rate_by(make_lines(), "stock_method")
    assert rates["manual"] == pytest.approx(50.0)   # O1 yes, O2 no
    assert rates["synced"] == pytest.approx(50.0)   # O3 yes, O4 no


def test_acceptance_by_fit_only_counts_substitutes():
    result = acceptance_by_fit(make_lines())
    assert result["yes"] == pytest.approx(100.0)
    assert result["no"] == pytest.approx(0.0)


def test_refunds_per_1000_orders():
    # 2.00 euros over 4 orders = 500 euros per 1,000 orders
    assert refunds_per_1000_orders(make_lines()) == pytest.approx(500.0)
