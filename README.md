# Ontario Sanitary Drainage Sizing Calculator

Counts drainage fixture units for common fixtures (OBC Table 7.4.9.3) and selects the minimum branch, stack and building drain sizes from Tables 7.4.10.6.-A, -B and -C of the 2024 Ontario Building Code, Part 7.

**Live web tool:** https://dust2engineering.github.io/ontario-sanitary-drainage-sizing-calculator/web/

## How it works

- Total the fixture units, then take the smallest pipe whose table capacity is not less than the load.
- Stacks also respect the per-storey cap in Table 7.4.10.6.-A; building drains depend on slope and are never smaller than NPS 4 to a public sewer.

## Data in this repository

- drainage-data.json — fixture-unit values and all three capacity tables, machine-readable.

## Command line

```bash
python3 sanitary_drainage.py --fu 54 --fu-one-storey 54 --slope 1:100
```

## Worked examples

- [restaurant-54-fu.md](examples/restaurant-54-fu.md)
- [plaza-unit-130-fu.md](examples/plaza-unit-130-fu.md)

## Scope and limits

Preliminary design aid only. It does not replace the current Ontario Building Code or the judgement of the designer of record. Verify all values against the Code in force for your project before submitting drawings for permit.

## About

Maintained by **Dust 2 Engineering Inc.** (Mississauga, Ontario) — building permit drawings
(architectural, HVAC, plumbing, sprinkler, electrical) for restaurants and small commercial
projects across the Greater Toronto Area, stamped by an Ontario P.Eng. Flat rate $3,500–$5,000.

Category: Plumbing. More free Ontario code tools: see the full index at
https://github.com/dust2engineering
