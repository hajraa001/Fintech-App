import streamlit as st
import pandas as pd


# -----------------------------
# Configuration
# -----------------------------

st.set_page_config(
    page_title="Financial Analyst Pro",
    page_icon="📊",
    layout="wide"
)


# -----------------------------
# Styling
# -----------------------------

st.markdown(
"""
<style>

.metric-card {
    background-color: #f8f9fa;
    padding:20px;
    border-radius:15px;
    border:1px solid #e5e7eb;
}

</style>
""",
unsafe_allow_html=True
)


# -----------------------------
# Header
# -----------------------------

st.title("📊 Financial Analyst Pro")

st.caption(
    "AI-powered financial statement analysis platform"
)


# -----------------------------
# Upload Section
# -----------------------------

st.subheader("📂 Upload Financial Statements")


col1, col2, col3 = st.columns(3)


with col1:
    balance_file = st.file_uploader(
        "Balance Sheet",
        type=["xlsx"]
    )


with col2:
    income_file = st.file_uploader(
        "Income Statement",
        type=["xlsx"]
    )


with col3:
    cashflow_file = st.file_uploader(
        "Cash Flow Statement",
        type=["xlsx"]
    )


files_ready = (
    balance_file
    and income_file
    and cashflow_file
)


if files_ready:


    st.success(
        "All financial statements loaded successfully"
    )


    # -----------------------------
    # Load Data
    # -----------------------------

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



    # Clean

    balance_df.dropna(
        how="all",
        inplace=True
    )

    income_df.dropna(
        how="all",
        inplace=True
    )

    cashflow_df.dropna(
        how="all",
        inplace=True
    )



    # -----------------------------
    # Dashboard
    # -----------------------------

    st.divider()

    st.header(
        "📈 Executive Dashboard"
    )


    c1,c2,c3,c4 = st.columns(4)


    with c1:
        st.metric(
            "Financial Health",
            "Analyzing..."
        )


    with c2:
        st.metric(
            "Liquidity",
            "Pending"
        )


    with c3:
        st.metric(
            "Profitability",
            "Pending"
        )


    with c4:
        st.metric(
            "Risk Level",
            "Pending"
        )



    # -----------------------------
    # Statements
    # -----------------------------

    st.divider()

    st.header(
        "📑 Financial Statements"
    )


    tab1,tab2,tab3 = st.tabs(
        [
            "Balance Sheet",
            "Income Statement",
            "Cash Flow"
        ]
    )


    with tab1:

        st.dataframe(
            balance_df,
            use_container_width=True,
            height=500
        )


    with tab2:

        st.dataframe(
            income_df,
            use_container_width=True,
            height=500
        )


    with tab3:

        st.dataframe(
            cashflow_df,
            use_container_width=True,
            height=500
        )



    # -----------------------------
    # Next Engine
    # -----------------------------

    st.divider()

    st.header(
        "🤖 Analyst Insights"
    )


    st.info(
        """
        Financial intelligence engine is ready.

        Next update:
        • Automatic row recognition
        • Ratio calculations
        • Trend analysis
        • AI financial commentary
        """
    )


else:

    st.info(
        "Upload all three statements to activate the dashboard."
    )
