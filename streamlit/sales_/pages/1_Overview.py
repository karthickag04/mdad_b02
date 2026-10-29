import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("supermarket_sales_dataset.csv")

st.title("Overview Dashboard")

total_sales = df["Total"].sum()
total_qty = df["Quantity"].sum()
avg_rating = df["Rating"].mean()

col1, col2, col3 = st.columns(3)

col1.metric("Total Sales", f"{total_sales:,.2f}")
col2.metric("Total Quantity Sold", total_qty)
col3.metric("Average Rating", round(avg_rating, 2))

fig = px.bar(
    df.groupby("City")["Total"].sum().reset_index(),
    x="City",
    y="Total",
    color="City",
    title="Sales by City"
)

st.plotly_chart(fig, use_container_width=True)