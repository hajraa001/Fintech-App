import streamlit as st
import pandas as pd


# ==============================
# APP CONFIG
# ==============================

st.set_page_config(
    page_title="Financial Analyst Pro",
    page_icon="📊",
    layout="wide"
)


# ==============================
# HEADER
# ==============================

st.title("📊 Financial Analyst Pro")

st.caption(
    "Automated financial statement analysis dashboard"
)


# ==============================
# FUNCTIONS
# ==============================

def clean_data(df):

    df = df.dropna(
        how="all"
    )

    df = df.dropna(
        axis=1,
        how="all"
    )

    df = df.map(
        lambda x: x.strip()
        if isinstance(x, str)
        else x
    )

    return df



def find_row(df, keywords):

    for keyword in keywords:

        result = df[
            df.astype(str)
            .apply(
                lambda x:
                x.str.contains(
                    keyword,
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



def extract_number(row):

    if row is None:
        return 0


    numbers = []

    for value in row:

        if isinstance(
            value,
            (int,float)
        ):

            numbers.append(value)


    if numbers:
        return numbers[-1]


    return 0



# ==============================
# UPLOAD SECTION
# ==============================

st.subheader("📂 Upload Financial Statements")


col1,col2,col3 = st.columns(3)


with col1:

    balance_file = st.file_uploader(
        "Balance Sheet",
        type="xlsx"
    )


with col2:

    income_file = st.file_uploader(
        "Income Statement",
        type="xlsx"
    )


with col3:

    cashflow_file = st.file_uploader(
        "Cash Flow",
        type="xlsx"
    )



if balance_file and income_file and cashflow_file:


    st.success(
        "✅ All statements uploaded"
    )


    # ==============================
    # READ FILES
    # ==============================

    balance = clean_data(
        pd.read_excel(
            balance_file,
            header=None
        )
    )


    income = clean_data(
        pd.read_excel(
            income_file,
            header=None
        )
    )


    cashflow = clean_data(
        pd.read_excel(
            cashflow_file,
            header=None
        )
    )


    # ==============================
    # EXTRACT BALANCE VALUES
    # ==============================


    current_assets = extract_number(
        find_row(
            balance,
            [
                "Current assets"
            ]
        )
    )


    current_liabilities = extract_number(
        find_row(
            balance,
            [
                "Current liabilities"
            ]
        )
    )


    total_assets = extract_number(
        find_row(
            balance,
            [
                "Assets"
            ]
        )
    )


    liabilities = extract_number(
        find_row(
            balance,
            [
                "Liabilities"
            ]
        )
    )


    equity = extract_number(
        find_row(
            balance,
            [
                "Shareholders’ equity",
                "Shareholders' equity"
            ]
        )
    )


    # ==============================
    # RATIOS
    # ==============================


    current_ratio = 0

    if current_liabilities:

        current_ratio = (
            current_assets /
            current_liabilities
        )


    debt_equity = 0

    if equity:

        debt_equity = (
            liabilities /
            equity
        )


    working_capital = (
        current_assets -
        current_liabilities
    )



    # ==============================
    # DASHBOARD
    # ==============================


    st.divider()

    st.header(
        "📈 Financial Dashboard"
    )


    a,b,c,d = st.columns(4)


    a.metric(
        "Current Ratio",
        f"{current_ratio:.2f}x"
    )


    b.metric(
        "Debt / Equity",
        f"{debt_equity:.2f}"
    )


    c.metric(
        "Working Capital",
        f"{working_capital:,.0f}"
    )


    d.metric(
        "Total Assets",
        f"{total_assets:,.0f}"
    )



    # ==============================
    # STATEMENT VIEW
    # ==============================


    st.divider()

    st.header(
        "📑 Statements"
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
            balance,
            use_container_width=True
        )


    with tab2:

        st.dataframe(
            income,
            use_container_width=True
        )


    with tab3:

        st.dataframe(
            cashflow,
            use_container_width=True
        )



    # ==============================
    # SUMMARY
    # ==============================


    st.divider()

    st.header(
        "🤖 Analyst Summary"
    )


    if current_ratio >= 1:

        st.success(
            "Liquidity position appears healthy."
        )

    else:

        st.warning(
            "Liquidity may require attention."
        )



else:

    st.info(
        "Upload all three statements to activate analysis."
    )
