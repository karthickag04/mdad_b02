import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("supermarket_sales_dataset.csv")

st.title("Product Performance")

product_sales = df.groupby("Product line")["Total"].sum().reset_index()

fig = px.bar(
    product_sales,
    x="Product line",
    y="Total",
    color="Product line",
    title="Sales by Product Line"
)

st.plotly_chart(fig, use_container_width=True)


qty_sold = df.groupby("Product line")["Quantity"].sum().reset_index()

fig2 = px.bar(
    qty_sold,
    x="Product line",
    y="Quantity",
    color="Product line",
    title="Quantity Sold per Product Line"
)

st.plotly_chart(fig2, use_container_width=True)