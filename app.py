import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="Marketing Campaign Dashboard", layout="wide")

@st.cache_data
def load_data():
    return pd.read_csv("data/marketing_data_final.csv")

df = load_data()

st.title("📊 Marketing Campaign Analysis Dashboard")
st.markdown("Customer segmentation, spending behavior & campaign response insights")

st.subheader("Customer Segment Distribution")
fig, ax = plt.subplots()
sns.countplot(x="Customer_Segment", data=df, ax=ax)
st.pyplot(fig)
st.subheader("Campaign Response Rate by Segment")

response_rate = (
    df.groupby("Customer_Segment")["Response"]
    .mean()
    .reset_index()
)

fig, ax = plt.subplots()
sns.barplot(
    x="Customer_Segment",
    y="Response",
    data=response_rate,
    ax=ax
)
ax.set_ylabel("Response Rate")
st.pyplot(fig)

st.subheader("Income vs Total Spending")

fig, ax = plt.subplots()
sns.scatterplot(
    x="Income",
    y="Total_Spending",
    hue="Customer_Segment",
    data=df,
    alpha=0.6,
    ax=ax
)
st.pyplot(fig)

