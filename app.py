import streamlit as st
import pandas as pd

st.title("Financial Analyst App")

balance_file = st.file_uploader(
    "Upload Balance Sheet",
    type=["xlsx"]
)

income_file = st.file_uploader(
    "Upload Income Statement",
    type=["xlsx"]
)

cashflow_file = st.file_uploader(
    "Upload Cash Flow Statement",
    type=["xlsx"]
)

if balance_file and income_file and cashflow_file:

    st.success("All 3 statements uploaded!")

    balance_df = pd.read_excel(balance_file, skiprows=3)
    income_df = pd.read_excel(income_file, skiprows=3)
    cashflow_df = pd.read_excel(cashflow_file, skiprows=3)

    st.subheader("Balance Sheet")
    st.dataframe(balance_df.head(20))

    st.subheader("Income Statement")
    st.dataframe(income_df.head(20))

    st.subheader("Cash Flow Statement")
    st.dataframe(cashflow_df.head(20))
