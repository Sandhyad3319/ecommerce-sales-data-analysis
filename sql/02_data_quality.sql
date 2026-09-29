-- SQL script to check for data quality issues in the cleaned dataset

-- Check for missing customer IDs
SELECT COUNT(*) AS Missing_CustomerIDs
FROM sales
WHERE CustomerID IS NULL;

-- Check for null values in InvoiceNo
SELECT COUNT(*) AS Null_InvoiceNo
FROM sales
WHERE InvoiceNo IS NULL;

-- Check for null values in StockCode
SELECT COUNT(*) AS Null_StockCode
FROM sales
WHERE StockCode IS NULL;

-- Check for null values in InvoiceDate
SELECT COUNT(*) AS Null_InvoiceDate
FROM sales
WHERE InvoiceDate IS NULL;

-- Check for null values in Quantity
SELECT COUNT(*) AS Null_Quantity
FROM sales
WHERE Quantity IS NULL;

-- Check for null values in UnitPrice
SELECT COUNT(*) AS Null_UnitPrice
FROM sales
WHERE UnitPrice IS NULL;

-- Check for null values in Revenue (calculated as Quantity * UnitPrice)
SELECT COUNT(*) AS Null_Revenue
FROM sales
WHERE Revenue IS NULL;

-- Check for invalid quantities (less than or equal to 0)
SELECT COUNT(*) AS Invalid_Quantities
FROM sales
WHERE Quantity <= 0;

-- Check for invalid unit prices (less than or equal to 0)
SELECT COUNT(*) AS Invalid_UnitPrices
FROM sales
WHERE UnitPrice <= 0;

-- Check for duplicate records
SELECT COUNT(*) AS Duplicate_Records
FROM (
    SELECT InvoiceNo, StockCode, CustomerID, COUNT(*) AS RecordCount
    FROM sales
    GROUP BY InvoiceNo, StockCode, CustomerID
    HAVING COUNT(*) > 1
) AS duplicates;

-- Check for cancelled invoices (InvoiceNo starting with 'C')
SELECT COUNT(*) AS Cancelled_Invoices
FROM sales
WHERE InvoiceNo LIKE 'C%';

-- Check for negative revenue
SELECT COUNT(*) AS Negative_Revenue
FROM sales
WHERE Revenue < 0;