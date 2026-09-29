# POWERBI_SETUP.md

# Power BI Dashboard Setup Instructions

This document provides step-by-step instructions for setting up the E-Commerce Sales & Customer Insights Dashboard in Power BI.

## Step 1: Open Power BI Desktop
Launch Power BI Desktop on your computer.

## Step 2: Import Data
1. Click on the "Home" tab.
2. Select "Get Data" and choose "Text/CSV".
3. Navigate to the `data/cleaned/` directory.
4. Select the `online_retail_cleaned.csv` file and click "Open".

## Step 3: Check Data Types
1. After importing, review the data types of each column in the "Data" view.
2. Ensure that the data types are correctly assigned (e.g., Date for InvoiceDate, Decimal for Revenue).

## Step 4: Create Relationships (if required)
1. Go to the "Model" view.
2. Check if there are any relationships that need to be created between tables.
3. Drag and drop fields to create relationships as necessary.

## Step 5: Create a Date Table
1. In the "Model" view, create a new table for dates.
2. Use the following DAX formula to create a Date table:
   ```DAX
   DateTable = CALENDAR(MIN(Sales[InvoiceDate]), MAX(Sales[InvoiceDate]))
   ```
3. Add additional columns for Year, Month Number, Month Name, and Quarter.

## Step 6: Create Calculated Columns (only when necessary)
1. If needed, create calculated columns in the "Data" view for any additional metrics.

## Step 7: Create DAX Measures
1. Create necessary DAX measures for KPIs such as Total Revenue, Total Orders, and Average Order Value.
2. Use the DAX measures provided in the `DAX_MEASURES.md` file.

## Step 8: Build Dashboard Pages
1. Create three pages in your Power BI report:
   - **Page 1: Executive Sales Overview**
   - **Page 2: Product Performance**
   - **Page 3: Customer & Market Analysis**
2. Add visuals such as charts, tables, and KPI cards to each page based on the analysis requirements.

## Final Notes
- Ensure to save your Power BI report frequently.
- Review the dashboard for any adjustments or additional insights that may be required.

By following these steps, you will successfully set up the Power BI dashboard for the E-Commerce Sales & Customer Insights project.