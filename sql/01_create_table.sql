CREATE TABLE sales (
    InvoiceNo TEXT PRIMARY KEY,
    StockCode TEXT NOT NULL,
    Description TEXT,
    Quantity INTEGER NOT NULL CHECK (Quantity > 0),
    InvoiceDate DATETIME NOT NULL,
    UnitPrice REAL NOT NULL CHECK (UnitPrice > 0),
    CustomerID INTEGER,
    Country TEXT,
    Revenue REAL GENERATED ALWAYS AS (Quantity * UnitPrice) STORED,
    Year INTEGER,
    Month INTEGER,
    MonthName TEXT,
    YearMonth TEXT,
    IsCancellation BOOLEAN DEFAULT 0
);