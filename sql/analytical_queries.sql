-- 1. Age distribution
SELECT
    Age,
    COUNT(*) AS customer_count
FROM customers
GROUP BY Age
ORDER BY Age;


-- 2. Income vs Total Spend
SELECT
    Income,
    Total_Spend
FROM customers
WHERE Income IS NOT NULL;


-- 3. Average spend by education
SELECT
    Education,
    ROUND(AVG(Total_Spend), 2) AS avg_spend
FROM customers
GROUP BY Education
ORDER BY avg_spend DESC;


-- 4. Average spend by marital status
SELECT
    Marital_Status,
    ROUND(AVG(Total_Spend), 2) AS avg_spend
FROM customers
GROUP BY Marital_Status
ORDER BY avg_spend DESC;


-- 5. Channel usage comparison
SELECT
    ROUND(AVG(NumWebPurchases), 2) AS avg_web,
    ROUND(AVG(NumCatalogPurchases), 2) AS avg_catalog,
    ROUND(AVG(NumStorePurchases), 2) AS avg_store
FROM customers;


-- 6. Campaign response rate
SELECT
    Campaign_Responder,
    COUNT(*) AS customer_count
FROM customers
GROUP BY Campaign_Responder;


-- 7. High spender profile
SELECT
    Age_Band,
    Income_Band,
    COUNT(*) AS high_spender_count
FROM customers
WHERE High_Spender = 1
GROUP BY Age_Band, Income_Band
ORDER BY high_spender_count DESC;
