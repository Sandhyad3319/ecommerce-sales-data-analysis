-- SQL script for product analysis
-- This script analyzes product data, including top products by revenue and quantity, and average selling price.

-- 1. Top products by revenue
SELECT 
    StockCode,
    Description,
    SUM(Revenue) AS TotalRevenue
FROM 
    sales
GROUP BY 
    StockCode, Description
ORDER BY 
    TotalRevenue DESC
LIMIT 10;

-- 2. Top products by quantity sold
SELECT 
    StockCode,
    Description,
    SUM(Quantity) AS TotalQuantity
FROM 
    sales
GROUP BY 
    StockCode, Description
ORDER BY 
    TotalQuantity DESC
LIMIT 10;

-- 3. Average selling price per product
SELECT 
    StockCode,
    Description,
    AVG(UnitPrice) AS AverageSellingPrice
FROM 
    sales
GROUP BY 
    StockCode, Description; 

-- 4. Revenue by stock code
SELECT 
    StockCode,
    SUM(Revenue) AS TotalRevenue
FROM 
    sales
GROUP BY 
    StockCode
ORDER BY 
    TotalRevenue DESC;

-- 5. Revenue by product description
SELECT 
    Description,
    SUM(Revenue) AS TotalRevenue
FROM 
    sales
GROUP BY 
    Description
ORDER BY 
    TotalRevenue DESC;