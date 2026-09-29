# DATA_MODEL.md

# Power BI Data Model

## Overview
The data model for the E-Commerce Sales & Customer Insights Dashboard is designed to facilitate efficient analysis and reporting. It consists of a fact table and several dimension tables that provide context to the sales data.

## Fact Table
- **Sales Table**: This is the primary fact table that contains transactional data. It includes metrics such as revenue, quantity sold, and order details.

## Dimension Tables
- **Date Dimension**: A dedicated date table that allows for time-based analysis. It includes fields such as:
  - Date
  - Year
  - Month Number
  - Month Name
  - Year Month
  - Quarter

- **Product Dimension**: Contains details about products, including:
  - StockCode
  - Description
  - UnitPrice

- **Customer Dimension**: Provides information about customers, including:
  - CustomerID
  - Country

## Relationships
- The **Sales Table** is linked to the **Date Dimension** through the InvoiceDate field, allowing for time-based analysis of sales.
- The **Sales Table** is linked to the **Product Dimension** through the StockCode field, enabling product-level insights.
- The **Sales Table** is linked to the **Customer Dimension** through the CustomerID field, facilitating customer analysis.

## Filter Direction
- Relationships are set to filter in both directions where applicable, allowing for comprehensive analysis across dimensions.

## Importance of the Date Table
A dedicated Date table is crucial for time-based analysis as it allows for:
- Easy filtering and grouping of data by various time periods (days, months, quarters, years).
- The ability to create time intelligence calculations, such as year-over-year growth and month-over-month comparisons.

This data model is structured to provide a clear and efficient way to analyze sales performance, customer behavior, and product trends, ultimately supporting data-driven decision-making.