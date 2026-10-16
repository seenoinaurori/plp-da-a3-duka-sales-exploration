# Duka Electronics Sales Exploration

## Project summary

This project explores 1,000 synthetic Duka Electronics orders from January through June 2026. It ranks branches and products, compares weekend with weekday sales, identifies the strongest and weakest months, and filters premium online orders from Nairobi and Mombasa. The analysis is in `duka_sales_exploration.ipynb`; `generate_data.py` writes a reproducible `duka_sales.csv` using seed 2026.

## Questions answered

1. What do the dataset's shape, types, completeness, date range, and key categories look like?
2. Which branches rank highest by revenue and by order count, and do those rankings agree?
3. Which products lead by revenue and by units sold, and why can the lists differ?
4. How do weekend orders compare with weekday orders in count, revenue, and average order revenue?
5. Which month was best and worst for revenue, and how large is the difference?
6. How many Premium Online orders came from Nairobi and Mombasa, and what revenue did they produce?
7. Do the spreadsheet SUMIFS branch ranking and revenue-by-branch/channel PivotTable match pandas?

## Regenerate and run

From this directory, install dependencies with `python -m pip install -r requirements.txt`, regenerate the source data with `python generate_data.py`, then open `duka_sales_exploration.ipynb` and run all cells from top to bottom. The CSV has 1,000 order-level records dated in the first half of 2026. `outputs/premium_online_coast_capital.csv` and `excel/duka_branch_summary.xlsx` are produced by the analysis notebook. Creating and recalculating the native Excel PivotTable requires Windows with desktop Excel installed.

> **Generator provenance:** The original Practical generator was not included in the supplied workspace, so `generate_data.py` is reproducible with seed 2026 but cannot be verified as an unchanged copy. Replace it with the original Practical source if exact source identity is required.

## Executive Summary

- The dataset contains **1,000 orders** from **January 1 through June 30, 2026**, with **0 missing values**.

- **Mombasa** led revenue with **KES 8,180,000**, while **Eldoret** led order count with **137 orders**; the rankings differed.

- **Laptop Pro 14** led revenue at **KES 16,840,500**, while **Bluetooth Speaker** led units sold with **162 units**; the top-three lists did not overlap.

- **698 weekday orders** generated **KES 37,119,000** and averaged **KES 53,179.08**, versus **302 weekend orders** averaging **KES 50,811.59**.

- **June** led at **KES 11,002,100**, **64.1%** above **February** at **KES 6,703,000**; the Premium Online Nairobi/Mombasa filter found **47 orders** worth **KES 4,891,100**.
