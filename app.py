import streamlit as st
import pandas as pd
import plotly.express as px


# =====================================
# CONFIGURATION
# =====================================

st.set_page_config(
    page_title="Financial Analyst Pro",
    page_icon="📊",
    layout="wide"
)


# =====================================
# STYLE
# =====================================

st.markdown(
"""
<style>

.main-header {
    font-size: 40px;
    font-weight: 700;
}

.card {
    padding: 20px;
    border-radius: 15px;
    background-color: #f8f9fa;
    border: 1px solid #e5e7eb;
}

</style>
""",
unsafe_allow_html=True
)



# =====================================
# TITLE
# =====================================

st.markdown(
"""
<div class="main-header">
📊 Financial Analyst Pro
</div>
""",
unsafe_allow_html=True
)

st.caption(
"Automated financial intelligence platform | Rieter Holding Ltd. 2025"
)



# =====================================
# SIDEBAR
# =====================================

st.sidebar.title(
"Navigation"
)


page = st.sidebar.radio(
    "Go to",
    [
        "🏠 Dashboard",
        "📄 Statements",
        "📈 Ratios",
        "⚠️ Risk Analysis"
    ]
)



# =====================================
# UPLOAD AREA
# =====================================

st.sidebar.divider()

st.sidebar.subheader(
"Upload Reports"
)


balance_file = st.sidebar.file_uploader(
"SOFP - Balance Sheet",
type=["xlsx"]
)


income_file = st.sidebar.file_uploader(
"SOFL - Income Statement",
type=["xlsx"]
)


cashflow_file = st.sidebar.file_uploader(
"SOCF - Cash Flow",
type=["xlsx"]
)



# =====================================
# FUNCTIONS
# =====================================


def clean_dataframe(df):

    df = df.dropna(
        how="all"
    )

    df = df.dropna(
        axis=1,
        how="all"
    )


    df = df.map(
        lambda x:
        x.strip()
        if isinstance(x,str)
        else x
    )

    return df




def search_row(df, names):

    """
    Finds financial statement rows
    """

    for name in names:

        result = df[
            df.astype(str)
            .apply(
                lambda row:
                row.str.contains(
                    name,
                    case=False,
                    na=False
                )
                .any(),
                axis=1
            )
        ]

        if not result.empty:

            return result.iloc[0]


    return None




def extract_value(row):

    if row is None:

        return 0


    values=[]


    for item in row:

        if isinstance(
            item,
            (int,float)
        ):

            values.append(item)


    if values:

        return values[-1]


    return 0



# =====================================
# LOAD FILES
# =====================================


if balance_file and income_file and cashflow_file:


    balance = clean_dataframe(
        pd.read_excel(
            balance_file,
            header=None
        )
    )


    income = clean_dataframe(
        pd.read_excel(
            income_file,
            header=None
        )
    )


    cashflow = clean_dataframe(
        pd.read_excel(
            cashflow_file,
            header=None
        )
    )



    # =====================================
    # BALANCE SHEET EXTRACTION
    # =====================================


    cash = extract_value(
        search_row(
            balance,
            [
                "Cash and cash equivalents"
            ]
        )
    )


    receivables = extract_value(
        search_row(
            balance,
            [
                "Trade receivables"
            ]
        )
    )


    inventory = extract_value(
        search_row(
            balance,
            [
                "Inventories"
            ]
        )
    )


    current_assets = extract_value(
        search_row(
            balance,
            [
                "Current assets"
            ]
        )
    )


    total_assets = extract_value(
        search_row(
            balance,
            [
                "Assets"
            ]
        )
    )


    current_liabilities = extract_value(
        search_row(
            balance,
            [
                "Current liabilities"
            ]
        )
    )


    total_liabilities = extract_value(
        search_row(
            balance,
            [
                "Liabilities"
            ]
        )
    )


    equity = extract_value(
        search_row(
            balance,
            [
                "Shareholders’ equity",
                "Shareholders' equity"
            ]
        )
    )



    # =====================================
    # INCOME STATEMENT EXTRACTION
    # =====================================


    revenue = extract_value(
        search_row(
            income,
            [
                "Sales",
                "Revenue"
            ]
        )
    )


    net_income = extract_value(
        search_row(
            income,
            [
                "Net profit",
                "Profit for the year",
                "Net income"
            ]
        )
    )



    # =====================================
    # CASH FLOW EXTRACTION
    # =====================================


    operating_cashflow = extract_value(
        search_row(
            cashflow,
            [
                "Operating activities"
            ]
        )
    )
