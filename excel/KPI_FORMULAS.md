# KPI_FORMULAS.md

# Key Performance Indicators (KPIs) and Formulas

This document outlines the key performance indicators (KPIs) used in the Excel analysis along with their corresponding formulas.

## KPIs

1. **Total Revenue**
   - Formula: `=SUM(Cleaned_Data!E:E)`
   - Description: Total revenue generated from all sales.

2. **Total Orders**
   - Formula: `=COUNTA(Cleaned_Data!A:A) - COUNTIF(Cleaned_Data!A:A, "C*")`
   - Description: Total number of unique orders, excluding cancellations.

3. **Total Customers**
   - Formula: `=COUNTA(UNIQUE(Cleaned_Data!G:G))`
   - Description: Total number of unique customers.

4. **Total Products**
   - Formula: `=COUNTA(UNIQUE(Cleaned_Data!B:B))`
   - Description: Total number of unique products sold.

5. **Average Order Value**
   - Formula: `=Total Revenue / Total Orders`
   - Description: Average revenue generated per order.

6. **Total Quantity Sold**
   - Formula: `=SUM(Cleaned_Data!D:D)`
   - Description: Total quantity of products sold.

## Additional Notes

- Ensure that the data in the "Cleaned_Data" sheet is up-to-date before using these formulas.
- Adjust the cell references in the formulas as necessary based on your Excel sheet layout.