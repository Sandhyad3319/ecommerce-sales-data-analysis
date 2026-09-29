from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
CLEANED_DATA_PATH = PROJECT_ROOT / "data" / "cleaned" / "online_retail_cleaned.csv"
CHARTS_DIR = PROJECT_ROOT / "outputs" / "charts"


def load_data():
    if not CLEANED_DATA_PATH.exists():
        raise FileNotFoundError(
            f"Cleaned data not found: {CLEANED_DATA_PATH}\n"
            "Run data_cleaning.py first."
        )

    return pd.read_csv(CLEANED_DATA_PATH)


def total_revenue(df):
    return df["revenue"].sum()


def total_orders(df):
    return df["invoice_no"].nunique()


def total_customers(df):
    return df.loc[df["customer_id"] != -1, "customer_id"].nunique()


def total_products(df):
    return df["stock_code"].nunique()


def total_quantity_sold(df):
    return df["quantity"].sum()


def average_order_value(df):
    return total_revenue(df) / total_orders(df)


def monthly_revenue(df):
    df["invoice_date"] = pd.to_datetime(df["invoice_date"])
    return df.groupby(df["invoice_date"].dt.to_period("M"))["revenue"].sum()


def revenue_by_country(df):
    return df.groupby("country")["revenue"].sum().sort_values(ascending=False)


def top_products_by_revenue(df, n=10):
    return df.groupby("description")["revenue"].sum().nlargest(n)


def top_products_by_quantity(df, n=10):
    return df.groupby("description")["quantity"].sum().nlargest(n)


def top_customers_by_revenue(df, n=10):
    valid_customers = df[df["customer_id"] != -1]
    return valid_customers.groupby("customer_id")["revenue"].sum().nlargest(n)


def orders_by_month(df):
    df["invoice_date"] = pd.to_datetime(df["invoice_date"])
    return df.groupby(df["invoice_date"].dt.to_period("M"))["invoice_no"].nunique()


def save_series_chart(series, filename, title, xlabel, ylabel, kind="bar"):
    ax = series.plot(kind=kind, figsize=(12, 6), title=title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    plt.tight_layout()
    plt.savefig(CHARTS_DIR / filename, dpi=150)
    plt.close()


def main():
    CHARTS_DIR.mkdir(parents=True, exist_ok=True)
    df = load_data()

    print(f"Total Revenue: £{total_revenue(df):,.2f}")
    print(f"Total Orders: {total_orders(df):,}")
    print(f"Total Customers: {total_customers(df):,}")
    print(f"Total Products: {total_products(df):,}")
    print(f"Total Quantity Sold: {total_quantity_sold(df):,.0f}")
    print(f"Average Order Value: £{average_order_value(df):,.2f}")

    save_series_chart(
        monthly_revenue(df),
        "monthly_revenue.png",
        "Monthly Revenue",
        "Month",
        "Revenue",
        kind="line",
    )

    save_series_chart(
        revenue_by_country(df).head(15),
        "country_revenue.png",
        "Top 15 Countries by Revenue",
        "Country",
        "Revenue",
    )

    save_series_chart(
        top_products_by_revenue(df),
        "top_products.png",
        "Top 10 Products by Revenue",
        "Product",
        "Revenue",
    )

    save_series_chart(
        top_products_by_quantity(df),
        "top_products_by_quantity.png",
        "Top 10 Products by Quantity",
        "Product",
        "Quantity",
    )

    save_series_chart(
        top_customers_by_revenue(df),
        "top_customers.png",
        "Top 10 Customers by Revenue",
        "Customer ID",
        "Revenue",
    )

    save_series_chart(
        orders_by_month(df),
        "orders_by_month.png",
        "Orders by Month",
        "Month",
        "Orders",
        kind="line",
    )

    print(f"\nCharts saved to: {CHARTS_DIR}")


if __name__ == "__main__":
    main()