# DAX Measures for Power BI Dashboard

This document outlines the DAX measures used in the Power BI dashboard for the E-Commerce Sales & Customer Insights project. These measures are essential for calculating key performance indicators (KPIs) and providing insights into the sales data.

## DAX Measures

1. **Total Revenue**
   ```DAX
   Total Revenue = SUM(Sales[Revenue])
   ```

2. **Total Orders**
   ```DAX
   Total Orders = DISTINCTCOUNT(Sales[InvoiceNo])
   ```

3. **Total Customers**
   ```DAX
   Total Customers = DISTINCTCOUNT(Sales[CustomerID])
   ```

4. **Total Products**
   ```DAX
   Total Products = DISTINCTCOUNT(Sales[StockCode])
   ```

5. **Total Quantity**
   ```DAX
   Total Quantity = SUM(Sales[Quantity])
   ```

6. **Average Order Value**
   ```DAX
   Average Order Value = DIVIDE([Total Revenue], [Total Orders])
   ```

7. **Revenue per Customer**
   ```DAX
   Revenue per Customer = DIVIDE([Total Revenue], [Total Customers])
   ```

8. **Previous Month Revenue**
   ```DAX
   Previous Month Revenue = CALCULATE([Total Revenue], PREVIOUSMONTH('Date'[Date]))
   ```

9. **Revenue Growth %**
   ```DAX
   Revenue Growth % = DIVIDE([Total Revenue] - [Previous Month Revenue], [Previous Month Revenue], 0)
   ```

10. **Average Quantity per Order**
    ```DAX
    Average Quantity per Order = DIVIDE([Total Quantity], [Total Orders])
    ```

11. **Revenue Contribution %**
    ```DAX
    Revenue Contribution % = DIVIDE(Sales[Revenue], CALCULATE(SUM(Sales[Revenue]), ALL(Sales)), 0)
    ```

These measures will be utilized in the Power BI dashboard to provide a comprehensive view of the e-commerce sales performance, enabling stakeholders to make informed business decisions.