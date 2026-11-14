# ADR-0001: Build the analysis on synthetic data first

## Context
Real order, stock and substitution data from a delivery platform is private. Public datasets (Olist, Instacart)
need a Kaggle login and have no stock levels or substitution outcomes. The analysis still needs a dataset with
order lines, stock method, customer preference, substitute fit, refunds, ratings and repeat orders.

## Decision
Generate a synthetic dataset with `data/generate_data.py`, using simple rules written at the top of the script,
a fixed random seed, and every rule labelled as an assumption. Build and test the metrics on it.

## Consequences
- The method can be built, tested and shown now.
- The findings partly reflect the rules that made the data; every number is marked "assumed" in the ledger and
  the README. They are not real company figures.
- When real data is available, a new ADR replaces this one; the metric functions and tests stay the same.
