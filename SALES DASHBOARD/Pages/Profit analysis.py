import streamlit as st
import pandas as pd
import plotly.express as px

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------
st.set_page_config(
    page_title="Profit Analysis",
    layout="wide"
)

# ---------------------------------------------------
# LOAD DATA
# ---------------------------------------------------
@st.cache_data
def load_data():
    df = pd.read_excel("Data/sales.xls")
    df.columns = df.columns.str.strip()
    return df

try:
    df = load_data()

except Exception as e:
    st.error(f"Error loading dataset: {e}")
    st.stop()

# ---------------------------------------------------
# TITLE
# ---------------------------------------------------
st.title(" Profit Analysis Dashboard")

st.markdown("""
This dashboard analyzes:

- Profit Trends
- Region Wise Profit
- Category Wise Profit
- Segment Wise Profit
- Profit vs Sales
- Monthly & Yearly Profit
""")

# ---------------------------------------------------
# DATE PROCESSING
# ---------------------------------------------------
if "Order Date" in df.columns:

    df["Order Date"] = pd.to_datetime(
        df["Order Date"],
        errors="coerce"
    )

    df["Year"] = df["Order Date"].dt.year

    df["Month"] = df["Order Date"].dt.strftime("%B")

    df["Month Number"] = df["Order Date"].dt.month

    df["Year Month"] = df["Order Date"].dt.to_period("M").astype(str)

# ---------------------------------------------------
# SIDEBAR FILTERS
# ---------------------------------------------------
st.sidebar.header("Filters")

filtered_df = df.copy()

# YEAR FILTER
if "Year" in df.columns:

    year_options = sorted(df["Year"].dropna().unique())

    selected_year = st.sidebar.multiselect(
        "Select Year",
        options=year_options,
        default=year_options
    )

    filtered_df = filtered_df[
        filtered_df["Year"].isin(selected_year)
    ]

# REGION FILTER
if "Region" in df.columns:

    region_options = sorted(df["Region"].dropna().unique())

    selected_region = st.sidebar.multiselect(
        "Select Region",
        options=region_options,
        default=region_options
    )

    filtered_df = filtered_df[
        filtered_df["Region"].isin(selected_region)
    ]

# CATEGORY FILTER
if "Category" in df.columns:

    category_options = sorted(df["Category"].dropna().unique())

    selected_category = st.sidebar.multiselect(
        "Select Category",
        options=category_options,
        default=category_options
    )

    filtered_df = filtered_df[
        filtered_df["Category"].isin(selected_category)
    ]

# SEGMENT FILTER
if "Segment" in df.columns:

    segment_options = sorted(df["Segment"].dropna().unique())

    selected_segment = st.sidebar.multiselect(
        "Select Segment",
        options=segment_options,
        default=segment_options
    )

    filtered_df = filtered_df[
        filtered_df["Segment"].isin(selected_segment)
    ]

# ---------------------------------------------------
# KPI SECTION
# ---------------------------------------------------
st.subheader("Key Profit Metrics")

k1, k2, k3, k4 = st.columns(4)

# TOTAL PROFIT
if "Profit" in filtered_df.columns:

    total_profit = filtered_df["Profit"].sum()

    k1.metric(
        "Total Profit",
        f"${total_profit:,.2f}"
    )

# AVERAGE PROFIT
if "Profit" in filtered_df.columns:

    avg_profit = filtered_df["Profit"].mean()

    k2.metric(
        "Average Profit",
        f"${avg_profit:,.2f}"
    )

# MAXIMUM PROFIT
if "Profit" in filtered_df.columns:

    max_profit = filtered_df["Profit"].max()

    k3.metric(
        "Maximum Profit",
        f"${max_profit:,.2f}"
    )

# MINIMUM PROFIT
if "Profit" in filtered_df.columns:

    min_profit = filtered_df["Profit"].min()

    k4.metric(
        "Minimum Profit",
        f"${min_profit:,.2f}"
    )

# ---------------------------------------------------
# MONTHLY PROFIT TREND
# ---------------------------------------------------
st.subheader("Monthly Profit Trend")

if (
    "Year Month" in filtered_df.columns
    and "Profit" in filtered_df.columns
):

    monthly_profit = (
        filtered_df
        .groupby("Year Month", as_index=False)["Profit"]
        .sum()
    )

    fig1 = px.line(
        monthly_profit,
        x="Year Month",
        y="Profit",
        markers=True,
        title="Monthly Profit Trend"
    )

    st.plotly_chart(
        fig1,
        use_container_width=True
    )

# ---------------------------------------------------
# YEARLY PROFIT TREND
# ---------------------------------------------------
st.subheader("Yearly Profit Trend")

if (
    "Year" in filtered_df.columns
    and "Profit" in filtered_df.columns
):

    yearly_profit = (
        filtered_df
        .groupby("Year", as_index=False)["Profit"]
        .sum()
    )

    fig2 = px.bar(
        yearly_profit,
        x="Year",
        y="Profit",
        text_auto=True,
        title="Yearly Profit Trend"
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

# ---------------------------------------------------
# CATEGORY WISE PROFIT
# ---------------------------------------------------
st.subheader("Category Wise Profit")

if (
    "Category" in filtered_df.columns
    and "Profit" in filtered_df.columns
):

    category_profit = (
        filtered_df
        .groupby("Category", as_index=False)["Profit"]
        .sum()
    )

    fig3 = px.bar(
        category_profit,
        x="Category",
        y="Profit",
        color="Category",
        text_auto=True,
        title="Category Wise Profit"
    )

    st.plotly_chart(
        fig3,
        use_container_width=True
    )

# ---------------------------------------------------
# REGION WISE PROFIT
# ---------------------------------------------------
st.subheader("Region Wise Profit")

if (
    "Region" in filtered_df.columns
    and "Profit" in filtered_df.columns
):

    region_profit = (
        filtered_df
        .groupby("Region", as_index=False)["Profit"]
        .sum()
    )

    fig4 = px.pie(
        region_profit,
        names="Region",
        values="Profit",
        title="Region Wise Profit Distribution"
    )

    st.plotly_chart(
        fig4,
        use_container_width=True
    )

# ---------------------------------------------------
# SEGMENT WISE PROFIT
# ---------------------------------------------------
st.subheader("Segment Wise Profit")

if (
    "Segment" in filtered_df.columns
    and "Profit" in filtered_df.columns
):

    segment_profit = (
        filtered_df
        .groupby("Segment", as_index=False)["Profit"]
        .sum()
    )

    fig5 = px.bar(
        segment_profit,
        x="Segment",
        y="Profit",
        color="Segment",
        text_auto=True,
        title="Segment Wise Profit"
    )

    st.plotly_chart(
        fig5,
        use_container_width=True
    )

# ---------------------------------------------------
# SHIP MODE WISE PROFIT
# ---------------------------------------------------
st.subheader("Ship Mode Wise Profit")

if (
    "Ship Mode" in filtered_df.columns
    and "Profit" in filtered_df.columns
):

    ship_profit = (
        filtered_df
        .groupby("Ship Mode", as_index=False)["Profit"]
        .sum()
    )

    fig6 = px.bar(
        ship_profit,
        x="Ship Mode",
        y="Profit",
        color="Ship Mode",
        text_auto=True,
        title="Ship Mode Wise Profit"
    )

    st.plotly_chart(
        fig6,
        use_container_width=True
    )

# ---------------------------------------------------
# PROFIT VS SALES
# ---------------------------------------------------
st.subheader("Profit vs Sales")

if (
    "Sales" in filtered_df.columns
    and "Profit" in filtered_df.columns
):

    fig7 = px.scatter(
        filtered_df,
        x="Sales",
        y="Profit",
        color="Category",
        title="Profit vs Sales"
    )

    st.plotly_chart(
        fig7,
        use_container_width=True
    )

# ---------------------------------------------------
# MONTH WISE PROFIT COMPARISON
# ---------------------------------------------------
st.subheader("Month Wise Profit Comparison")

if (
    "Month" in filtered_df.columns
    and "Month Number" in filtered_df.columns
    and "Profit" in filtered_df.columns
):

    month_profit = (
        filtered_df
        .groupby(
            ["Month Number", "Month"],
            as_index=False
        )["Profit"]
        .sum()
        .sort_values("Month Number")
    )

    fig8 = px.bar(
        month_profit,
        x="Month",
        y="Profit",
        text_auto=True,
        title="Month Wise Profit Comparison"
    )

    st.plotly_chart(
        fig8,
        use_container_width=True
    )

# ---------------------------------------------------
# PROFIT SUMMARY TABLE
# ---------------------------------------------------
st.subheader("Profit Summary Table")

summary_table = (
    filtered_df
    .groupby("Year Month", as_index=False)
    .agg({
        "Profit": "sum",
        "Sales": "sum",
        "Quantity": "sum",
        "Order ID": "nunique"
    })
)

summary_table = summary_table.rename(
    columns={
        "Order ID": "Total Orders"
    }
)

st.dataframe(
    summary_table,
    use_container_width=True
)

# ---------------------------------------------------
# DOWNLOAD FILTERED DATA
# ---------------------------------------------------
st.subheader("Download Filtered Data")

csv = filtered_df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="Download Profit Analysis Data",
    data=csv,
    file_name="profit_analysis_filtered_data.csv",
    mime="text/csv"
)