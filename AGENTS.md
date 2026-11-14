# AGENTS.md

## Product directive (owned by the human; agents never edit this section)
Shelf Sync helps partner stores keep what customers can order in line with what is on the shelf: sold-out
items come off the menu, staff are warned before items run out, and missing items get substitutes that fit
what the customer asked for. Full text and invariants I1–I5: `simulation/directive.md`.

## Always on
1. Spec before code: `specs/001-stockout-substitutes/spec.md` (D1).
2. Tests before code; run `python -m pytest -q` before saying "done" and paste the last line (D7, D8).
3. Never edit, delete, skip or weaken anything under `tests/`; if a test looks wrong, stop and say why.
4. Every number carries its source, date and kind (observed, reported, estimated, assumed): `research/ledger.csv` (A3).
5. Keep raw inputs untouched; every derived number comes from code (A12). The data is synthetic: say so.
6. Unsure? Write the question with its default, apply the default, keep working (D10).
7. One branch per task; Conventional commits (`feat:`, `test:`, `docs:`); a human merges.
8. No personal data, no keys, no real people as personas (A13).

## How to run
- `pip install -r requirements.txt`
- `python data/generate_data.py` (from `data/`) → `data/order_lines.csv`
- `python -m pytest -q`
- Notebook: `notebooks/01_stockout_analysis.ipynb`
