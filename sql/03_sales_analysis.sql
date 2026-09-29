-- SQL script for sales analysis

-- 1. Total Revenue
SELECT SUM(Revenue) AS Total_Revenue
FROM sales;

-- 2. Total Orders
SELECT COUNT(DISTINCT InvoiceNo) AS Total_Orders
FROM sales;

-- 3. Total Quantity
SELECT SUM(Quantity) AS Total_Quantity
FROM sales;

-- 4. Total Customers
SELECT COUNT(DISTINCT CustomerID) AS Total_Customers
FROM sales;

-- 5. Total Products
SELECT COUNT(DISTINCT StockCode) AS Total_Products
FROM sales;

-- 6. Average Order Value
SELECT AVG(Revenue) AS Average_Order_Value
FROM sales;

-- 7. Monthly Revenue
SELECT strftime('%Y-%m', InvoiceDate) AS Month, SUM(Revenue) AS Monthly_Revenue
FROM sales
GROUP BY Month
ORDER BY Month;

-- 8. Revenue by Country
SELECT Country, SUM(Revenue) AS Revenue_By_Country
FROM sales
GROUP BY Country
ORDER BY Revenue_By_Country DESC;

-- 9. Orders by Country
SELECT Country, COUNT(DISTINCT InvoiceNo) AS Orders_By_Country
FROM sales
GROUP BY Country
ORDER BY Orders_By_Country DESC;

-- 10. Top Products
SELECT StockCode, SUM(Revenue) AS Total_Revenue
FROM sales
GROUP BY StockCode
ORDER BY Total_Revenue DESC
LIMIT 10;

-- 11. Revenue Trend
SELECT strftime('%Y-%m', InvoiceDate) AS Month, SUM(Revenue) AS Revenue
FROM sales
GROUP BY Month
ORDER BY Month;

-- 12. Highest Revenue Month
SELECT strftime('%Y-%m', InvoiceDate) AS Month, SUM(Revenue) AS Total_Revenue
FROM sales
GROUP BY Month
ORDER BY Total_Revenue DESC
LIMIT 1;