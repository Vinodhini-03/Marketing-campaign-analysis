📊 Marketing Campaign Analysis
🔍 Project Overview

This project analyzes a customer marketing campaign dataset to understand customer behavior, segment audiences, and evaluate campaign performance.
It follows an end-to-end data analytics workflow, transforming raw marketing data into actionable business insights using Python, SQL, and an interactive dashboard.

🎯 Project Objectives

Clean and preprocess raw marketing data

Engineer meaningful features for customer behavior analysis

Segment customers based on demographics and spending patterns

Store and analyze data efficiently using SQL

Build an interactive dashboard for real-time insights

🗂️ Project Structure
Marketing_Campaign_Analysis/
│
├── data/
│   ├── marketing_data.csv
│   ├── marketing_data_dictionary.csv
│   └── marketing_data_final.csv
│
├── notebooks/
│   ├── 01_data_cleaning.ipynb
│   ├── 02_feature_engineering_segmentation.ipynb
│   └── 03_eda.ipynb
│
├── sql/
│   ├── create_tables.sql
│   ├── load_data.sql
│   ├── analytical_queries.sql
│   └── marketing_campaign.db
│
├── dashboard/
│   └── app.py
│
└── README.md

🛠️ Tools & Technologies

Python – Data processing & analysis

Pandas, NumPy – Data manipulation

Matplotlib, Seaborn, Plotly – Visualization

SQLite – Database storage & querying

Streamlit – Interactive dashboard

Jupyter Notebook – Exploratory analysis

📒 Notebooks Overview
📘 Notebook 1 – Data Cleaning

Handled missing values and invalid entries

Standardized categorical variables

Prepared raw data for analysis

📘 Notebook 2 – Feature Engineering & Segmentation

Created features such as:

Total spending

Campaign responder flag

High spender indicator

Prepared data for segmentation and SQL storage

📘 Notebook 3 – Exploratory Data Analysis (EDA)

Analyzed customer demographics

Visualized spending behavior

Evaluated campaign response patterns

🗄️ SQL Layer
Database

SQLite database: marketing_campaign.db

SQL Scripts

create_tables.sql → Defines database schema

load_data.sql → Loads cleaned data into tables

analytical_queries.sql → Business-focused SQL insights

Example Analyses

Campaign response rates

Spending patterns by customer segment

Identification of high-value customers

📊 Streamlit Dashboard

The Streamlit dashboard provides:

Interactive filters (Education, Marital Status)

Key performance indicators (KPIs)

Spending and income distribution visualizations

Campaign response insights

High-value customer table

▶️ Run the Dashboard

From the project root directory:

cd dashboard
streamlit run app.py

💡 Key Insights

Higher-income customers show stronger campaign engagement

Certain education and marital groups spend more consistently

A small percentage of customers contribute to a large share of revenue

🚀 Conclusion

This project demonstrates how structured data processing, SQL analysis, and interactive visualization can be combined to support data-driven marketing decisions.