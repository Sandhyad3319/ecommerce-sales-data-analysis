-- SQL script for customer analysis

-- 1. Top customers by revenue
SELECT 
    CustomerID, 
    SUM(Revenue) AS TotalRevenue
FROM 
    sales
GROUP BY 
    CustomerID
ORDER BY 
    TotalRevenue DESC
LIMIT 10;

-- 2. Orders per customer
SELECT 
    CustomerID, 
    COUNT(DISTINCT InvoiceNo) AS TotalOrders
FROM 
    sales
GROUP BY 
    CustomerID;

-- 3. Revenue per customer
SELECT 
    CustomerID, 
    SUM(Revenue) AS RevenuePerCustomer
FROM 
    sales
GROUP BY 
    CustomerID;

-- 4. Quantity purchased per customer
SELECT 
    CustomerID, 
    SUM(Quantity) AS TotalQuantityPurchased
FROM 
    sales
GROUP BY 
    CustomerID;

-- 5. Customer ranking based on revenue
SELECT 
    CustomerID, 
    RANK() OVER (ORDER BY SUM(Revenue) DESC) AS CustomerRank
FROM 
    sales
GROUP BY 
    CustomerID;

-- 6. Country-wise customer count
SELECT 
    Country, 
    COUNT(DISTINCT CustomerID) AS CustomerCount
FROM 
    sales
GROUP BY 
    Country;