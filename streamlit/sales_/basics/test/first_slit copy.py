import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Sales Dashboard",
    layout="wide"
)

st.title("Sales Dashboard")

# Read CSV
df = pd.read_csv("sales.csv")

# Dataset preview
st.subheader("Dataset")

st.dataframe(df)

# Basic statistics
st.subheader("Statistics")

st.write(df.describe())

# Total sales
total_sales = df["Sales"].sum()

st.metric(
    "Total Sales",
    f"₹{total_sales:,.0f}"
)

# Sales by category
category_sales = (
    df.groupby("Category")["Sales"]
      .sum()
      .reset_index()
)

st.subheader("Sales by Category")

# Create Matplotlib chart
fig, ax = plt.subplots()

ax.bar(
    category_sales["Category"],
    category_sales["Sales"]
)

ax.set_title("Sales by Category")
ax.set_xlabel("Category")
ax.set_ylabel("Sales")

plt.xticks(rotation=45)

# Display Matplotlib chart in Streamlit
st.pyplot(fig)