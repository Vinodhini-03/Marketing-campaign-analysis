CREATE TABLE marketing_campaign (
    ID INT PRIMARY KEY,
    Year_Birth INT,
    Education VARCHAR(50),
    Marital_Status VARCHAR(50),
    Income FLOAT,
    Kidhome INT,
    Teenhome INT,
    Dt_Customer DATE,
    Recency INT,

    MntWines FLOAT,
    MntFruits FLOAT,
    MntMeatProducts FLOAT,
    MntFishProducts FLOAT,
    MntSweetProducts FLOAT,
    MntGoldProds FLOAT,

    NumWebPurchases INT,
    NumCatalogPurchases INT,
    NumStorePurchases INT,
    NumWebVisitsMonth INT,

    Response INT,

    -- Engineered Features
    Age INT,
    Customer_Tenure_Days INT,
    Total_Spend FLOAT,
    Total_Purchases INT,
    Children INT,

    High_Income INT,
    Young_Customer INT,
    Family_Customer INT,
    Campaign_Responder INT,
    High_Web_Engagement INT,
    High_Spender INT,

    Age_Band VARCHAR(20),
    Income_Band VARCHAR(20)
);
