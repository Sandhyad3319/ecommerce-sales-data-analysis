from pathlib import Path
import sqlite3

import pandas as pd
from ucimlrepo import fetch_ucirepo


PROJECT_ROOT = Path(__file__).resolve().parents[1]
RAW_FILE = PROJECT_ROOT / "data" / "raw" / "Online_Retail.xlsx"
CLEANED_DIR = PROJECT_ROOT / "data" / "cleaned"
CLEANED_FILE = CLEANED_DIR / "online_retail_cleaned.csv"
DATABASE_FILE = CLEANED_DIR / "online_retail.db"


def create_directories():
    CLEANED_DIR.mkdir(parents=True, exist_ok=True)


def download_dataset():
    """Load the official UCI Online Retail dataset."""
    print("Downloading dataset from UCI...")

    dataset = fetch_ucirepo(id=352)

    features = dataset.data.features.copy()
    identifiers = dataset.data.ids.copy()

    # UCI stores InvoiceNo and StockCode as identifier columns.
    if identifiers is not None and not identifiers.empty:
        df = pd.concat(
            [identifiers.reset_index(drop=True), features.reset_index(drop=True)],
            axis=1,
        )
    else:
        df = features

    print(f"Downloaded {len(df):,} rows.")
    print(f"Available columns: {list(df.columns)}")
    return df


def load_dataset():
    """Use a manually supplied file when available; otherwise use UCI."""
    if RAW_FILE.exists():
        print(f"Loading local file: {RAW_FILE}")
        return pd.read_excel(RAW_FILE)

    return download_dataset()


def clean_data(df):
    """Clean transactions and create analysis columns."""

    # Normalize source column names: spaces, underscores, and capitalization.
    df = df.copy()
    df.columns = (
        df.columns.astype(str)
        .str.strip()
        .str.replace(r"[^A-Za-z0-9]", "", regex=True)
        .str.lower()
    )

    column_aliases = {
        "invoiceno": "invoice_no",
        "invoice": "invoice_no",
        "stockcode": "stock_code",
        "stock": "stock_code",
        "description": "description",
        "quantity": "quantity",
        "invoicedate": "invoice_date",
        "unitprice": "unit_price",
        "customerid": "customer_id",
        "country": "country",
    }

    df = df.rename(columns=column_aliases)

    required_columns = {
        "invoice_no",
        "stock_code",
        "description",
        "quantity",
        "invoice_date",
        "unit_price",
        "customer_id",
        "country",
    }

    missing_columns = required_columns - set(df.columns)
    if missing_columns:
        raise ValueError(
            f"Missing required columns: {sorted(missing_columns)}\n"
            f"Available columns: {list(df.columns)}"
        )

    # Convert fields to appropriate types.
    df["invoice_no"] = df["invoice_no"].astype("string").str.strip()
    df["stock_code"] = df["stock_code"].astype("string").str.strip()
    df["description"] = df["description"].fillna("No Description").astype("string")
    df["quantity"] = pd.to_numeric(df["quantity"], errors="coerce")
    df["invoice_date"] = pd.to_datetime(df["invoice_date"], errors="coerce")
    df["unit_price"] = pd.to_numeric(df["unit_price"], errors="coerce")
    df["customer_id"] = pd.to_numeric(df["customer_id"], errors="coerce")
    df["country"] = df["country"].fillna("Unknown").astype("string").str.strip()

    # Identify cancellations before filtering them out.
    df["is_cancellation"] = df["invoice_no"].str.upper().str.startswith(
        "C", na=False
    )

    # Remove cancellations and invalid sales records.
    df = df[~df["is_cancellation"]]
    df = df[df["quantity"] > 0]
    df = df[df["unit_price"] > 0]
    df = df.dropna(
        subset=[
            "invoice_no",
            "stock_code",
            "invoice_date",
            "quantity",
            "unit_price",
        ]
    )

    # Preserve valid transactions with unknown customers.
    df["customer_id"] = df["customer_id"].fillna(-1).astype("Int64")

    df = df.drop_duplicates().copy()

    # Create analysis columns.
    df["revenue"] = df["quantity"] * df["unit_price"]
    df["year"] = df["invoice_date"].dt.year
    df["month"] = df["invoice_date"].dt.month
    df["month_name"] = df["invoice_date"].dt.month_name()
    df["year_month"] = df["invoice_date"].dt.to_period("M").astype(str)

    return df


def save_cleaned_data(df):
    """Save the cleaned CSV and SQLite database."""
    df.to_csv(CLEANED_FILE, index=False)

    with sqlite3.connect(DATABASE_FILE) as connection:
        df.to_sql("sales", connection, if_exists="replace", index=False)

    print(f"Saved CSV: {CLEANED_FILE}")
    print(f"Saved database: {DATABASE_FILE}")


def print_summary(original_count, df):
    print("\nCleaning Summary")
    print("----------------")
    print(f"Original row count: {original_count:,}")
    print(f"Final row count: {len(df):,}")
    print(f"Missing customer IDs retained: {(df['customer_id'] == -1).sum():,}")
    print(f"Total revenue: £{df['revenue'].sum():,.2f}")


def main():
    create_directories()
    raw_data = load_dataset()
    cleaned_data = clean_data(raw_data)
    save_cleaned_data(cleaned_data)
    print_summary(len(raw_data), cleaned_data)


if __name__ == "__main__":
    main()