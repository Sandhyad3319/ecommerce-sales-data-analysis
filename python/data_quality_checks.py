from pathlib import Path
import sqlite3

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATABASE_PATH = PROJECT_ROOT / "data" / "cleaned" / "online_retail.db"
CLEANED_CSV = PROJECT_ROOT / "data" / "cleaned" / "online_retail_cleaned.csv"


def data_quality_checks():
    if not DATABASE_PATH.exists():
        raise FileNotFoundError(
            f"Database not found: {DATABASE_PATH}\n"
            "Run data_cleaning.py first."
        )

    if not CLEANED_CSV.exists():
        raise FileNotFoundError(f"Cleaned CSV not found: {CLEANED_CSV}")

    with sqlite3.connect(DATABASE_PATH) as connection:
        cursor = connection.cursor()

        total_rows = cursor.execute(
            "SELECT COUNT(*) FROM sales"
        ).fetchone()[0]

        checks = {
            "Null invoice numbers": "invoice_no IS NULL",
            "Null stock codes": "stock_code IS NULL",
            "Null invoice dates": "invoice_date IS NULL",
            "Null quantities": "quantity IS NULL",
            "Null unit prices": "unit_price IS NULL",
            "Missing customer IDs": "customer_id IS NULL OR customer_id = -1",
            "Non-positive quantities": "quantity <= 0",
            "Non-positive prices": "unit_price <= 0",
            "Negative revenue": "revenue < 0",
            "Cancelled invoices": "UPPER(invoice_no) LIKE 'C%'",
            "Extremely high quantities": "quantity > 10000",
            "Extremely high unit prices": "unit_price > 10000",
        }

        print("\nDATA QUALITY REPORT")
        print("=" * 50)
        print(f"Total rows: {total_rows:,}\n")

        for label, condition in checks.items():
            count = cursor.execute(
                f"SELECT COUNT(*) FROM sales WHERE {condition}"
            ).fetchone()[0]

            percentage = count / total_rows * 100 if total_rows else 0
            print(f"{label}: {count:,} ({percentage:.2f}%)")

        # Read only the columns needed for duplicate checking.
        duplicate_columns = [
            "invoice_no",
            "stock_code",
            "invoice_date",
            "quantity",
            "unit_price",
        ]

        cleaned_df = pd.read_csv(
            CLEANED_CSV,
            usecols=duplicate_columns,
        )

        duplicate_mask = cleaned_df.duplicated(
            subset=duplicate_columns,
            keep=False,
        )

        duplicate_groups = (
            cleaned_df.loc[duplicate_mask, duplicate_columns]
            .drop_duplicates()
            .shape[0]
        )

        duplicate_rows = int(
            cleaned_df.duplicated(
                subset=duplicate_columns,
                keep="first",
            ).sum()
        )

        print(f"\nDuplicate groups: {duplicate_groups:,}")
        print(f"Duplicate extra rows: {duplicate_rows:,}")

        invalid_condition = """
            invoice_no IS NULL
            OR stock_code IS NULL
            OR invoice_date IS NULL
            OR quantity IS NULL
            OR unit_price IS NULL
            OR quantity <= 0
            OR unit_price <= 0
            OR revenue < 0
            OR UPPER(invoice_no) LIKE 'C%'
        """

        invalid_count = cursor.execute(
            f"SELECT COUNT(*) FROM sales WHERE {invalid_condition}"
        ).fetchone()[0]

        valid_count = total_rows - invalid_count
        validity_rate = valid_count / total_rows * 100 if total_rows else 0

        print("\nSUMMARY")
        print("=" * 50)
        print(f"Valid rows: {valid_count:,}")
        print(f"Invalid rows: {invalid_count:,}")
        print(f"Validity rate: {validity_rate:.2f}%")


if __name__ == "__main__":
    data_quality_checks()