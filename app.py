import streamlit as st
import pandas as pd


# -----------------------------
# Page Configuration
# -----------------------------

st.set_page_config(
    page_title="Financial Analyst App",
    page_icon="📊",
    layout="wide"
)


st.title("📊 Financial Analyst App")
st.write(
    "Upload the 3 financial statements to begin analysis."
)


# -----------------------------
# File Upload
# -----------------------------

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



# -----------------------------
# Cleaning Function
# -----------------------------

def clean_dataframe(df):

    # Remove completely empty rows
    df = df.dropna(
        how="all"
    )

    # Remove completely empty columns
    df = df.dropna(
        axis=1,
        how="all"
    )


    # Clean text formatting
    df = df.map(
        lambda x: x.strip()
        if isinstance(x, str)
        else x
    )

    return df



# -----------------------------
# Detect Rows
# -----------------------------

def display_rows(df, title):

    st.subheader(title)

    for index, row in df.iterrows():

        values = row.dropna().tolist()

        if values:

            st.write(
                values
            )



# -----------------------------
# Main Application
# -----------------------------

if balance_file and income_file and cashflow_file:


    st.success(
        "✅ All 3 statements uploaded successfully!"
    )


    # Read Excel without assuming structure

    balance_df = pd.read_excel(
        balance_file,
        header=None
    )


    income_df = pd.read_excel(
        income_file,
        header=None
    )


    cashflow_df = pd.read_excel(
        cashflow_file,
        header=None
    )



    # Clean data

    balance_df = clean_dataframe(
        balance_df
    )

    income_df = clean_dataframe(
        income_df
    )

    cashflow_df = clean_dataframe(
        cashflow_df
    )



    # -----------------------------
    # Display Raw Statements
    # -----------------------------

    st.divider()

    st.header(
        "📋 Financial Statements"
    )


    with st.expander(
        "Balance Sheet (SOFP)"
    ):

        st.dataframe(
            balance_df,
            use_container_width=True
        )


    with st.expander(
        "Income Statement (SOPL)"
    ):

        st.dataframe(
            income_df,
            use_container_width=True
        )


    with st.expander(
        "Cash Flow Statement (SOCF)"
    ):

        st.dataframe(
            cashflow_df,
            use_container_width=True
        )



    # -----------------------------
    # Row Detection
    # -----------------------------

    st.divider()

    st.header(
        "🔍 Balance Sheet Row Names"
    )


    display_rows(
        balance_df,
        "Detected Balance Sheet Rows"
    )



    st.divider()


    st.header(
        "📈 Financial Ratio Dashboard"
    )


    st.info(
        """
        Data extraction completed.

        Next version will automatically calculate:

        ✅ Current Ratio
        ✅ Quick Ratio
        ✅ Debt-to-Equity
        ✅ Working Capital
        ✅ Profit Margins
        ✅ Cash Flow Metrics
        """
    )


else:

    st.warning(
        "Please upload all 3 financial statements to start analysis."
    )
