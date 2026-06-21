import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Financial Analyst App",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Financial Analyst App")
st.write("Upload the 3 financial statements to begin analysis.")

# Upload files
balance_file = st.file_uploader(
    "Upload Balance Sheet (SOFP)",
    type=["xlsx"]
)

income_file = st.file_uploader(
    "Upload Income Statement (SOPL)",
    type=["xlsx"]
)

cashflow_file = st.file_uploader(
    "Upload Cash Flow Statement (SOCF)",
    type=["xlsx"]
)

# Process files when all are uploaded
if balance_file and income_file and cashflow_file:

    st.success("✅ All 3 statements uploaded successfully!")

    # Read Excel files
    balance_df = pd.read_excel(balance_file, skiprows=3)
    income_df = pd.read_excel(income_file, skiprows=3)
    cashflow_df = pd.read_excel(cashflow_file, skiprows=3)

    # Display data
    st.subheader("📋 Balance Sheet (SOFP)")
    st.dataframe(balance_df.head(20))

    st.subheader("📋 Income Statement (SOPL)")
    st.dataframe(income_df.head(20))

    st.subheader("📋 Cash Flow Statement (SOCF)")
    st.dataframe(cashflow_df.head(20))

    st.subheader("🔍 Balance Sheet Data Inspector")

st.write(
    "These are the detected row labels:"
)

rows = balance_df.iloc[:,0].dropna()

for row in rows:
    st.write("•", row)

    st.divider()

    st.subheader("📈 Financial Ratio Dashboard")

    st.info(
        "Next step: We will connect the actual Assets, Liabilities, Equity, Revenue, and Net Income values and calculate ratios automatically."
    )
