import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("supermarket_sales_dataset.csv")

st.title("Payment Analysis")

payment_dist = df.groupby("Payment")["Total"].sum().reset_index()

fig = px.pie(
    payment_dist,
    names="Payment",
    values="Total",
    title="Payment Method Distribution"
)

st.plotly_chart(fig)


city_payment = px.bar(
    df,
    x="City",
    y="Total",
    color="Payment",
    title="City vs Payment Method"
)

st.plotly_chart(city_payment)