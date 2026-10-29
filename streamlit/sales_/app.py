import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Supermarket Sales Dashboard",
    page_icon="🛒",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for a premium look
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
    .stMetric {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    h1 {
        color: #1f77b4;
        font-family: 'Inter', sans-serif;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🛒 Supermarket Sales Analysis Hub")

st.markdown("""
Welcome to the elite **Sales Insights Portal**. This dashboard provides a 360-degree view of supermarket performance using advanced data visualization.

---
""")

@st.cache_data
def load_data():
    df = pd.read_csv("supermarket_sales_dataset.csv")
    df['Date'] = pd.to_datetime(df['Date'])
    return df

try:
    df = load_data()
    
    # Hero Metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Revenue", f"${df['Total'].sum():,.2f}", delta="Overall")
    with col2:
        st.metric("Total Transactions", f"{len(df):,}", delta="3 Months")
    with col3:
        st.metric("Customer Satisfaction", f"{df['Rating'].mean():.2f} / 10", delta="Avg")
    with col4:
        st.metric("Active Branches", f"{df['Branch'].nunique()}", delta="Cities: " + ", ".join(df['City'].unique()))

    st.markdown("---")

    col_info, col_img = st.columns([2, 1])
    
    with col_info:
        st.subheader("Explore the Data")
        st.write("""
        Use the sidebar on the left to navigate through specialized analysis modules:
        
        *   **1_Overview**: Big picture KPIs and trends.
        *   **2_Sales_Analysis**: Deep dive into revenue and timing.
        *   **3_Customer_Insights**: Who are our buyers?
        *   **4_Product_Performance**: What are the bestsellers?
        *   **5_Payment_Analysis**: How do people pay?
        *   **6_Ratings_Analysis**: What is the feedback?
        """)
        st.info("💡 **Pro-Tip**: You can interact with all charts by hovering, zooming, or filtering data in the specific analysis pages.")

    with col_img:
        st.image("https://images.unsplash.com/photo-1542838132-92c53300491e?auto=format&fit=crop&w=800&q=80", caption="Data-Driven Retail")

except Exception as e:
    st.error(f"Error loading system: {e}")
    st.warning("Please verify that 'supermarket_sales_dataset.csv' exists in the root directory.")