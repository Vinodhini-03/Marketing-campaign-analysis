import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Page configuration
st.set_page_config(
    page_title="Marketing Campaign Dashboard", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for dark theme
st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
    }
    .stMetric {
        background-color: #1e2130;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
    }
    h1, h2, h3 {
        color: #ffffff;
    }
    </style>
    """, unsafe_allow_html=True)

# Title
st.title("📊 Marketing Campaign Analysis Dashboard")

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv("data/marketing_data_final.csv")
    return df

df = load_data()

# Sidebar filters
st.sidebar.header("🔍 Filters")
education_filter = st.sidebar.multiselect(
    "Education Level",
    options=df["Education"].unique(),
    default=df["Education"].unique()
)

marital_filter = st.sidebar.multiselect(
    "Marital Status",
    options=df["Marital_Status"].unique(),
    default=df["Marital_Status"].unique()
)

# Apply filters
df_filtered = df[
    (df["Education"].isin(education_filter)) & 
    (df["Marital_Status"].isin(marital_filter))
]

# Key Metrics Row
st.subheader("📈 Key Performance Indicators")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Total Customers", 
        f"{len(df_filtered):,}",
        delta=f"{len(df_filtered) - len(df)}" if len(df_filtered) != len(df) else None
    )

with col2:
    avg_income = df_filtered["Income"].mean()
    st.metric("Avg Income", f"${avg_income:,.2f}")

with col3:
    response_rate = df_filtered["Campaign_Responder"].mean() * 100
    st.metric("Campaign Response Rate", f"{response_rate:.2f}%")

with col4:
    high_spender_pct = (df_filtered["High_Spender"].sum() / len(df_filtered)) * 100
    st.metric("High Spenders", f"{high_spender_pct:.2f}%")

st.markdown("---")

# Row 1: Two charts
col1, col2 = st.columns(2)

with col1:
    st.subheader("💰 Total Spending by Education Level")
    
    # Calculate total spending by education
    spending_cols = ['MntWines', 'MntFruits', 'MntMeatProducts', 
                     'MntFishProducts', 'MntSweetProducts', 'MntGoldProds']
    df_filtered['Total_Spending'] = df_filtered[spending_cols].sum(axis=1)
    
    edu_spending = df_filtered.groupby('Education')['Total_Spending'].mean().reset_index()
    
    fig1 = px.bar(
        edu_spending, 
        x='Education', 
        y='Total_Spending',
        title="Average Spending by Education",
        template="plotly_dark",
        color='Total_Spending',
        color_continuous_scale='Blues'
    )
    fig1.update_layout(height=400)
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    st.subheader("🎯 Campaign Response Distribution")
    
    response_counts = df_filtered['Campaign_Responder'].value_counts()
    
    fig2 = go.Figure(data=[go.Pie(
        labels=['Non-Responders', 'Responders'],
        values=response_counts.values,
        hole=0.4,
        marker=dict(colors=['#FF6B6B', '#4ECDC4'])
    )])
    fig2.update_layout(
        template="plotly_dark",
        height=400,
        showlegend=True
    )
    st.plotly_chart(fig2, use_container_width=True)

st.markdown("---")

# Row 2: Two more charts
col3, col4 = st.columns(2)

with col3:
    st.subheader("👥 Customer Distribution by Marital Status")
    
    marital_counts = df_filtered['Marital_Status'].value_counts().reset_index()
    marital_counts.columns = ['Marital_Status', 'Count']
    
    fig3 = px.bar(
        marital_counts,
        x='Marital_Status',
        y='Count',
        template="plotly_dark",
        color='Count',
        color_continuous_scale='Viridis'
    )
    fig3.update_layout(height=400)
    st.plotly_chart(fig3, use_container_width=True)

with col4:
    st.subheader("💸 Income Distribution")
    
    fig4 = px.histogram(
        df_filtered,
        x='Income',
        nbins=30,
        template="plotly_dark",
        color_discrete_sequence=['#FFA07A']
    )
    fig4.update_layout(height=400)
    st.plotly_chart(fig4, use_container_width=True)

st.markdown("---")

# Row 3: Product spending breakdown
st.subheader("🛒 Product Category Spending")

product_totals = df_filtered[spending_cols].sum()
product_data = pd.DataFrame({
    'Category': ['Wines', 'Fruits', 'Meat', 'Fish', 'Sweets', 'Gold'],
    'Total_Spending': product_totals.values
})

fig5 = px.bar(
    product_data,
    x='Category',
    y='Total_Spending',
    template="plotly_dark",
    color='Total_Spending',
    color_continuous_scale='Sunset'
)
fig5.update_layout(height=400)
st.plotly_chart(fig5, use_container_width=True)

st.markdown("---")

# Row 4: High Spenders Table
st.subheader("⭐ Top High Spenders")
high_spenders = df_filtered[df_filtered["High_Spender"] == 1].sort_values(
    by='Total_Spending', ascending=False
).head(10)

display_cols = ['Education', 'Marital_Status', 'Income', 'Total_Spending', 
                'Campaign_Responder', 'Country']
st.dataframe(
    high_spenders[display_cols],
    use_container_width=True,
    hide_index=True
)

# Footer
st.markdown("---")
st.caption("Dashboard created with Streamlit & Plotly | Marketing Campaign Analysis")