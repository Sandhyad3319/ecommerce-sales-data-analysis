from pathlib import Path

import pandas as pd
from openpyxl import Workbook
from openpyxl.styles import Font


ROOT = Path(__file__).resolve().parents[1]
CSV_PATH = ROOT / "data" / "cleaned" / "online_retail_cleaned.csv"
OUTPUT_PATH = ROOT / "excel" / "ecommerce_sales_analysis.xlsx"


def main():
    if not CSV_PATH.exists():
        raise FileNotFoundError(
            f"Cleaned CSV not found: {CSV_PATH}. Run data_cleaning.py first."
        )

    df = pd.read_csv(CSV_PATH)
    df["invoice_date"] = pd.to_datetime(df["invoice_date"])

    customers = df[df["customer_id"] != -1]

    kpis = pd.DataFrame({
        "KPI": [
            "Total Revenue",
            "Total Orders",
            "Total Customers",
            "Total Products",
            "Total Quantity",
            "Average Order Value",
        ],
        "Value": [
            df["revenue"].sum(),
            df["invoice_no"].nunique(),
            customers["customer_id"].nunique(),
            df["stock_code"].nunique(),
            df["quantity"].sum(),
            df["revenue"].sum() / df["invoice_no"].nunique(),
        ],
    })

    monthly = (
        df.groupby("year_month", as_index=False)
        .agg(
            Revenue=("revenue", "sum"),
            Orders=("invoice_no", "nunique"),
            Quantity=("quantity", "sum"),
        )
    )

    country = (
        df.groupby("country", as_index=False)
        .agg(
            Revenue=("revenue", "sum"),
            Orders=("invoice_no", "nunique"),
            Customers=("customer_id", "nunique"),
        )
        .sort_values("Revenue", ascending=False)
    )

    products = (
        df.groupby(["stock_code", "description"], as_index=False)
        .agg(
            Revenue=("revenue", "sum"),
            Quantity=("quantity", "sum"),
            Orders=("invoice_no", "nunique"),
        )
        .sort_values("Revenue", ascending=False)
    )

    customer_analysis = (
        customers.groupby("customer_id", as_index=False)
        .agg(
            Revenue=("revenue", "sum"),
            Orders=("invoice_no", "nunique"),
            Quantity=("quantity", "sum"),
        )
        .sort_values("Revenue", ascending=False)
    )

    workbook = Workbook()
    workbook.remove(workbook.active)

    sheets = {
        "Cleaned_Data": df,
        "KPI_Summary": kpis,
        "Monthly_Sales": monthly,
        "Country_Analysis": country,
        "Product_Analysis": products,
        "Customer_Analysis": customer_analysis,
    }

    for sheet_name, data in sheets.items():
        worksheet = workbook.create_sheet(sheet_name)

        for column_number, column_name in enumerate(data.columns, start=1):
            cell = worksheet.cell(row=1, column=column_number, value=column_name)
            cell.font = Font(bold=True)

        for row in data.itertuples(index=False, name=None):
            worksheet.append(row)

        worksheet.freeze_panes = "A2"
        worksheet.auto_filter.ref = worksheet.dimensions

        for column in worksheet.columns:
            worksheet.column_dimensions[column[0].column_letter].width = min(
                max(len(str(cell.value or "")) for cell in column) + 2,
                30,
            )

    workbook.save(OUTPUT_PATH)
    print(f"Workbook created: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()