import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("supermarket_sales_dataset.csv")
df["Date"] = pd.to_datetime(df["Date"])

st.title("Sales Analysis")

sales_trend = df.groupby("Date")["Total"].sum().reset_index()

fig = px.line(
    sales_trend,
    x="Date",
    y="Total",
    title="Daily Sales Trend"
)

st.plotly_chart(fig, use_container_width=True)


branch_sales = df.groupby("Branch")["Total"].sum().reset_index()

fig2 = px.bar(
    branch_sales,
    x="Branch",
    y="Total",
    color="Branch",
    title="Branch-wise Sales"
)

st.plotly_chart(fig2, use_container_width=True)