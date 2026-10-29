import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("supermarket_sales_dataset.csv")

st.title("Customer Insights")

gender_sales = df.groupby("Gender")["Total"].sum().reset_index()

fig = px.pie(
    gender_sales,
    names="Gender",
    values="Total",
    title="Sales by Gender"
)

st.plotly_chart(fig)


customer_type = df.groupby("Customer type")["Total"].sum().reset_index()

fig2 = px.bar(
    customer_type,
    x="Customer type",
    y="Total",
    color="Customer type",
    title="Sales by Customer Type"
)

st.plotly_chart(fig2)