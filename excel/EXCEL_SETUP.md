# EXCEL_SETUP.md

# Excel Analysis Setup Instructions

This document outlines the steps to create an Excel analysis using the cleaned dataset from the project.

## Steps to Create Excel Analysis

1. **Open Excel**: Launch Microsoft Excel on your computer.

2. **Import Cleaned Data**:
   - Go to the `Data` tab.
   - Click on `Get Data` > `From File` > `From Workbook`.
   - Navigate to the `data/cleaned/` directory and select `online_retail_cleaned.csv`.
   - Click `Import` and follow the prompts to load the data into Excel.

3. **Create Recommended Sheets**:
   - Create the following sheets in your Excel workbook:
     - **Cleaned_Data**: This sheet will contain the raw data imported from the cleaned CSV.
     - **KPI_Summary**: This sheet will summarize key performance indicators (KPIs).
     - **Monthly_Sales**: This sheet will analyze sales on a monthly basis.
     - **Country_Analysis**: This sheet will provide insights based on sales by country.
     - **Product_Analysis**: This sheet will analyze product performance.
     - **Customer_Analysis**: This sheet will focus on customer-related insights.

4. **Formulas and PivotTables**:
   - In the **KPI_Summary** sheet, use the following formulas to calculate KPIs:
     - Total Revenue: `=SUM(Cleaned_Data!E:E)` (assuming Revenue is in column E)
     - Total Orders: `=COUNTA(Cleaned_Data!A:A)` (assuming InvoiceNo is in column A)
     - Total Customers: `=COUNTA(UNIQUE(Cleaned_Data!G:G))` (assuming CustomerID is in column G)
     - Total Products: `=COUNTA(UNIQUE(Cleaned_Data!B:B))` (assuming StockCode is in column B)
     - Average Order Value: `=Total Revenue / Total Orders`
     - Total Quantity: `=SUM(Cleaned_Data!D:D)` (assuming Quantity is in column D)

   - Create PivotTables in the **Monthly_Sales**, **Country_Analysis**, **Product_Analysis**, and **Customer_Analysis** sheets to visualize the data:
     - For **Monthly_Sales**, summarize total revenue and quantity sold by month.
     - For **Country_Analysis**, summarize total revenue and orders by country.
     - For **Product_Analysis**, summarize total revenue and quantity sold by product.
     - For **Customer_Analysis**, summarize total revenue and orders by customer.

5. **Charts**:
   - Create charts to visualize the data in each analysis sheet:
     - Use bar charts for country and product analysis.
     - Use line charts for monthly sales trends.
     - Use pie charts for customer distribution.

6. **Save Your Workbook**: After completing your analysis, save your Excel workbook as `ecommerce_sales_analysis.xlsx` in the `excel/` directory.

By following these steps, you will create a comprehensive Excel analysis that complements the insights derived from the cleaned dataset.