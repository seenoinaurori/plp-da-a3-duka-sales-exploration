"""Generate the reproducible Duka Electronics half-year sales dataset."""

from pathlib import Path

import numpy as np
import pandas as pd

SEED = 2026
ORDER_COUNT = 1_000
OUTPUT_PATH = Path(__file__).resolve().parent / "duka_sales.csv"

BRANCHES = {
    "Nairobi": "Capital",
    "Westlands": "Capital",
    "Mombasa": "Coast",
    "Kisumu": "Western",
    "Nakuru": "Rift Valley",
    "Eldoret": "Rift Valley",
    "Thika": "Central",
    "Nyeri": "Central",
}
PRODUCTS = {
    "Smartphone X": ("Mobile", 42_000),
    "Budget Smartphone": ("Mobile", 18_500),
    "Laptop Pro 14": ("Computing", 115_000),
    "Chromebook Air": ("Computing", 32_000),
    "Wireless Headphones": ("Audio", 8_500),
    "Bluetooth Speaker": ("Audio", 6_800),
    "4K Television 43in": ("Television", 54_000),
    "HD Television 32in": ("Television", 27_500),
    "Wi-Fi Router AX": ("Networking", 12_000),
    "Power Bank 20K": ("Accessories", 4_500),
    "Smart Watch": ("Wearables", 22_000),
    "Tablet 10in": ("Computing", 29_500),
}
CHANNELS = ("In-store", "Online")


def generate_sales(seed: int = SEED, order_count: int = ORDER_COUNT) -> pd.DataFrame:
    """Return deterministic order-level sales covering January through June 2026."""
    rng = np.random.default_rng(seed)
    product_names = np.array(list(PRODUCTS))
    selected_products = rng.choice(product_names, size=order_count)
    dates = pd.Timestamp("2026-01-01") + pd.to_timedelta(
        rng.integers(0, 181, size=order_count), unit="D"
    )

    rows = []
    for index, product in enumerate(selected_products):
        category, base_price = PRODUCTS[str(product)]
        unit_price = int(round(base_price * rng.uniform(0.92, 1.08) / 100) * 100)
        rows.append(
            {
                "order_id": f"DUKA-{index + 1:04d}",
                "order_date": dates[index],
                "branch": str(rng.choice(list(BRANCHES))),
                "region": "",
                "product": str(product),
                "category": category,
                "channel": str(rng.choice(CHANNELS, p=[0.64, 0.36])),
                "units_sold": int(rng.choice([1, 2, 3, 4, 5], p=[0.58, 0.24, 0.11, 0.05, 0.02])),
                "unit_price": unit_price,
            }
        )

    data = pd.DataFrame(rows)
    data["region"] = data["branch"].map(BRANCHES)
    return data


def main() -> None:
    data = generate_sales()
    data.to_csv(OUTPUT_PATH, index=False, date_format="%Y-%m-%d")
    print(f"Wrote {len(data):,} orders to {OUTPUT_PATH}")
    print(f"Date range: {data['order_date'].min():%Y-%m-%d} to {data['order_date'].max():%Y-%m-%d}")


if __name__ == "__main__":
    main()
