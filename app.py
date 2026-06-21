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
    # =====================================
    # CALCULATIONS
    # =====================================

    current_ratio = 0
    quick_ratio = 0
    debt_equity = 0
    working_capital = 0


    if current_liabilities != 0:

        current_ratio = (
            current_assets /
            current_liabilities
        )


        quick_ratio = (
            cash +
            receivables
        ) / current_liabilities



    if equity != 0:

        debt_equity = (
            total_liabilities /
            equity
        )


    working_capital = (
        current_assets -
        current_liabilities
    )



    # =====================================
    # FINANCIAL HEALTH SCORE
    # =====================================

    score = 50


    if current_ratio >= 1.5:

        score += 15

    elif current_ratio < 1:

        score -= 15



    if debt_equity < 1:

        score += 15

    else:

        score -= 10



    if net_income > 0:

        score += 10


    score = max(
        0,
        min(score,100)
    )



    # =====================================
    # DASHBOARD PAGE
    # =====================================

    if page == "🏠 Dashboard":


        st.header(
            "Executive Dashboard"
        )


        col1,col2,col3,col4 = st.columns(4)


        with col1:

            st.metric(
                "Financial Health Score",
                f"{score}/100"
            )


        with col2:

            st.metric(
                "Revenue",
                f"{revenue:,.0f}"
            )


        with col3:

            st.metric(
                "Net Income",
                f"{net_income:,.0f}"
            )


        with col4:

            st.metric(
                "Total Assets",
                f"{total_assets:,.0f}"
            )



        st.divider()


        st.subheader(
            "Financial Position"
        )


        col5,col6,col7 = st.columns(3)


        with col5:

            st.info(
                f"""
                Liquidity

                Current Ratio:
                {current_ratio:.2f}x
                """
            )


        with col6:

            st.info(
                f"""
                Debt Risk

                Debt / Equity:
                {debt_equity:.2f}
                """
            )


        with col7:

            st.info(
                f"""
                Working Capital

                {working_capital:,.0f}
                """
            )



        st.divider()


        st.subheader(
            "🤖 Analyst Summary"
        )


        if current_ratio >= 1.5:

            st.success(
                """
                The company demonstrates a strong
                liquidity position and appears capable
                of covering short-term obligations.
                """
            )

        else:

            st.warning(
                """
                Liquidity requires monitoring as
                short-term obligations may pressure
                available resources.
                """
            )



    # =====================================
    # STATEMENTS PAGE
    # =====================================

    elif page == "📄 Statements":


        st.header(
            "Financial Statements"
        )


        tab1,tab2,tab3 = st.tabs(
            [
                "SOFP Balance Sheet",
                "SOFL Income Statement",
                "SOCF Cash Flow"
            ]
        )


        with tab1:

            st.dataframe(
                balance,
                use_container_width=True,
                height=600
            )


        with tab2:

            st.dataframe(
                income,
                use_container_width=True,
                height=600
            )


        with tab3:

            st.dataframe(
                cashflow,
                use_container_width=True,
                height=600
            )



    # =====================================
    # RATIOS PAGE
    # =====================================

    elif page == "📈 Ratios":


        st.header(
            "Financial Ratios"
        )


        ratio_data = pd.DataFrame(
            {
                "Metric":
                [
                    "Current Ratio",
                    "Quick Ratio",
                    "Debt / Equity",
                    "Working Capital"
                ],

                "Value":
                [
                    round(current_ratio,2),
                    round(quick_ratio,2),
                    round(debt_equity,2),
                    round(working_capital,2)
                ]
            }
        )


        st.dataframe(
            ratio_data,
            use_container_width=True
        )


        chart = px.bar(
            ratio_data,
            x="Metric",
            y="Value",
            title="Financial Ratio Overview"
        )


        st.plotly_chart(
            chart,
            use_container_width=True
        )



    # =====================================
    # RISK ANALYSIS PAGE
    # =====================================

    elif page == "⚠️ Risk Analysis":


        st.header(
            "Financial Risk Assessment"
        )


        if debt_equity < 1:

            st.success(
                "🟢 Debt level appears manageable."
            )

        else:

            st.warning(
                "🟡 Debt level requires attention."
            )


        if current_ratio >= 1:

            st.success(
                "🟢 Liquidity position is acceptable."
            )

        else:

            st.error(
                "🔴 Liquidity risk detected."
            )


else:


    st.info(
        """
        Upload:

        ✅ SOFP Balance Sheet
        ✅ SOFL Income Statement
        ✅ SOCF Cash Flow

        to activate the Financial Analyst dashboard.
        """
    )
