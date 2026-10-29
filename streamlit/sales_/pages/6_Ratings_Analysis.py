import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("supermarket_sales_dataset.csv")

st.title("Ratings Analysis")

rating_product = df.groupby("Product line")["Rating"].mean().reset_index()

fig = px.bar(
    rating_product,
    x="Product line",
    y="Rating",
    color="Product line",
    title="Average Rating per Product Line"
)

st.plotly_chart(fig)


rating_city = px.box(
    df,
    x="City",
    y="Rating",
    color="City",
    title="Rating Distribution by City"
)

st.plotly_chart(rating_city)