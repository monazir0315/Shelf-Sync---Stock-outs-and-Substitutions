# Simulated users (DS403 method)

Same loop as in the HR Analysis project: simulated users critique the product in **waves**, and a fixed
**directive** decides which of their requests get built.

```text
directive (fixed) → personas → critique (each persona, twice) → triage (≤ 5 changes) → build → walk again → 3–5 real people
```

| File | What it is |
|---|---|
| [`directive.md`](directive.md) | What Shelf Sync is for, and invariants I1–I5 that no wave may break. **Draft: the product owner edits and commits it** |
| [`personas.yaml`](personas.yaml) | Four fictional personas who disagree: a store picker at the counter, a store owner who distrusts auto-accept, a vegan customer on her phone, a city operations analyst |
| [`simulate_wave.py`](simulate_wave.py) · [`ux_critic.md`](ux_critic.md) · [`wave_triage.md`](wave_triage.md) | The course script and its two prompts |

## Next: wave 1

Show the personas screenshots of the store app prototype (orders board, out-of-stock sheet, stock screen),
collect two critiques per persona, and triage them into at most five changes.

```bash
python simulate_wave.py --directive directive.md --personas personas.yaml --text wave1/structure.md --runs 2 --out wave1
```
