import streamlit as st
import pandas as pd


st.set_page_config(
    page_title="Financial Analyst App",
    page_icon="📊",
    layout="wide"
)


st.title("📊 Financial Analyst App")
st.write(
    "Upload financial statements to begin automated analysis."
)


# ----------------------------
# Upload Files
# ----------------------------

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



# ----------------------------
# Functions
# ----------------------------

def clean_dataframe(df):

    # Remove empty rows
    df = df.dropna(how="all")

    # Remove empty columns
    df = df.dropna(axis=1, how="all")

    # Clean text spaces
    df = df.map(
        lambda x: x.strip()
        if isinstance(x, str)
        else x
    )

    return df



def find_label_column(df):

    """
    Finds the column containing financial labels
    """

    scores = {}

    for col in df.columns:

        score = (
            df[col]
            .astype(str)
            .str.len()
            .mean()
        )

        scores[col] = score


    return max(
        scores,
        key=scores.get
    )



# ----------------------------
# Read Files
# ----------------------------

if balance_file and income_file and cashflow_file:


    st.success(
        "✅ All statements uploaded successfully!"
    )


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


    balance_df = clean_dataframe(balance_df)
    income_df = clean_dataframe(income_df)
    cashflow_df = clean_dataframe(cashflow_df)



    # ----------------------------
    # Display Statements
    # ----------------------------

    st.header("📋 Financial Statements")


    with st.expander(
        "Balance Sheet"
    ):

        st.dataframe(
            balance_df,
            use_container_width=True
        )


    with st.expander(
        "Income Statement"
    ):

        st.dataframe(
            income_df,
            use_container_width=True
        )


    with st.expander(
        "Cash Flow Statement"
    ):

        st.dataframe(
            cashflow_df,
            use_container_width=True
        )



    # ----------------------------
    # Row Detection
    # ----------------------------


    st.divider()

    st.header(
        "🔍 Balance Sheet Row Detection"
    )


    label_column = find_label_column(
        balance_df
    )


    st.write(
        "Detected label column:",
        label_column
    )


    rows = (
        balance_df[label_column]
        .dropna()
        .tolist()
    )


    for row in rows:

        st.write(
            "•",
            row
        )



    # ----------------------------
    # Next Development
    # ----------------------------

    st.divider()

    st.header(
        "📈 Financial Analysis"
    )


    st.info(
        """
        Data extraction complete.

        Next upgrade:
        ✅ Automatically detect Assets
        ✅ Detect Liabilities
        ✅ Detect Equity
        ✅ Calculate financial ratios
        """
    )
