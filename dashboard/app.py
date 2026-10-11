import streamlit as st
import pandas as pd
import plotly.express as px

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------
st.set_page_config(
    page_title="E-Commerce Sales Dashboard",
    page_icon="📊",
    layout="wide"
)
# --------------------------------------------------
# Professional Dashboard Styling
# --------------------------------------------------
st.markdown("""
<style>
    .stApp {
        background-color: #0b0f17;
        color: #f1f5f9;
    }

    h1, h2, h3 {
        color: #f8fafc !important;
        font-weight: 700 !important;
    }

    div[data-testid="stMetric"] {
        background: linear-gradient(145deg, #171e2b, #111722);
        border: 1px solid #293548;
        padding: 22px 20px;
        border-radius: 16px;
        box-shadow: 0 6px 20px rgba(0, 0, 0, 0.18);
    }

    div[data-testid="stMetricLabel"] {
        color: #a8b6cc;
    }

    div[data-testid="stMetricValue"] {
        color: #f8fafc;
        font-weight: 700;
    }

    div[data-testid="stSidebar"] {
        background-color: #121824;
        border-right: 1px solid #273244;
    }

    div[data-testid="stPlotlyChart"] {
        background-color: #111722;
        border: 1px solid #263244;
        border-radius: 14px;
        padding: 10px;
    }

    hr {
        border-color: #273244;
    }
</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# Custom Dashboard Styling
# --------------------------------------------------
st.markdown("""
<style>

    /* Main background */
    .stApp {
        background-color: #0e1117;
    }

    /* Dashboard title */
    h1 {
        font-size: 42px !important;
        font-weight: 700 !important;
        margin-bottom: 5px !important;
    }

    /* Section headings */
    h2, h3 {
        font-weight: 600 !important;
    }

    /* KPI metric cards */
    div[data-testid="metric-container"] {
        background-color: #171b24;
        border: 1px solid #292f3a;
        padding: 20px;
        border-radius: 14px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.25);
    }

    div[data-testid="metric-container"] label {
        color: #aeb6c2 !important;
        font-size: 14px !important;
    }

    div[data-testid="metric-container"] div[data-testid="stMetricValue"] {
        font-size: 28px !important;
        font-weight: 700 !important;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background-color: #171a23;
    }

    section[data-testid="stSidebar"] h2 {
        font-size: 24px !important;
    }

    /* Chart containers */
        div[data-testid="stPlotlyChart"] {
        background-color: #11151d;
        border-radius: 14px;
        padding: 8px;
    }

    /* Professional KPI Cards */
    .kpi-card {
        background: #171b24;
        border: 1px solid #292f3a;
        border-radius: 16px;
        padding: 20px;
        min-height: 115px;
        box-shadow: 0 6px 18px rgba(0, 0, 0, 0.25);
        transition: transform 0.2s ease, border-color 0.2s ease;
    }

    .kpi-card:hover {
        transform: translateY(-3px);
        border-color: #4da3ff;
    }

    .kpi-title {
        font-size: 14px;
        color: #aeb6c2;
        margin-bottom: 10px;
    }

    .kpi-value {
        font-size: 27px;
        font-weight: 700;
        color: #ffffff;
        margin-bottom: 5px;
    }

    .kpi-subtitle {
        font-size: 12px;
        color: #7f8996;
    }

</style>
""", unsafe_allow_html=True)
# --------------------------------------------------
# Load Dataset
# --------------------------------------------------
df = pd.read_csv("data/global_ecommerce_sales-selected-columns.csv")

# Calculate Total Sales
df["Total_Sales"] = df["Quantity"] * df["Unit_Price"]

# Convert Order Date
df["Order_Date"] = pd.to_datetime(df["Order_Date"])

# --------------------------------------------------
# Sidebar Filters
# --------------------------------------------------
st.sidebar.header("🔎 Filters")

selected_region = st.sidebar.multiselect(
    "Select Region",
    options=sorted(df["Region"].unique()),
    default=sorted(df["Region"].unique())
)

selected_category = st.sidebar.multiselect(
    "Select Product Category",
    options=sorted(df["Product_Category"].unique()),
    default=sorted(df["Product_Category"].unique())
)

# Apply filters
filtered_df = df[
    (df["Region"].isin(selected_region)) &
    (df["Product_Category"].isin(selected_category))
]

# --------------------------------------------------
# Dashboard Header
# --------------------------------------------------
st.title("📊 E-Commerce Sales Dashboard")
st.markdown("### Sales Performance Overview")

# --------------------------------------------------
# KPI Calculations
# --------------------------------------------------
total_sales = filtered_df["Total_Sales"].sum()
average_order_value = filtered_df["Total_Sales"].mean()
total_orders = filtered_df["Order_ID"].nunique()
total_customers = filtered_df["Customer_Name"].nunique()

# --------------------------------------------------
# KPI Cards
# --------------------------------------------------
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown("""
    <div class="kpi-card">
        <div class="kpi-title">💰 Total Sales</div>
        <div class="kpi-value">₹{:,.2f}</div>
        <div class="kpi-subtitle">Overall revenue</div>
    </div>
    """.format(total_sales), unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="kpi-card">
        <div class="kpi-title">🛒 Average Order Value</div>
        <div class="kpi-value">₹{:,.2f}</div>
        <div class="kpi-subtitle">Average sales per order</div>
    </div>
    """.format(average_order_value), unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="kpi-card">
        <div class="kpi-title">📦 Total Orders</div>
        <div class="kpi-value">{:,}</div>
        <div class="kpi-subtitle">Orders processed</div>
    </div>
    """.format(total_orders), unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="kpi-card">
        <div class="kpi-title">👥 Total Customers</div>
        <div class="kpi-value">{:,}</div>
        <div class="kpi-subtitle">Unique customers</div>
    </div>
    """.format(total_customers), unsafe_allow_html=True)
# --------------------------------------------------
# Sales by Product Category
# --------------------------------------------------
st.subheader("Sales by Product Category")

category_sales = (
    filtered_df.groupby("Product_Category")["Total_Sales"]
    .sum()
    .sort_values(ascending=False)
    .reset_index()
)

fig_category = px.bar(
    category_sales,
    x="Product_Category",
    y="Total_Sales",
    title="Sales by Product Category",
    labels={
        "Product_Category": "Category",
        "Total_Sales": "Sales (₹)"
    },
    text="Total_Sales"
)

fig_category.update_traces(
    texttemplate="₹%{text:,.0f}",
    textposition="outside",
    hovertemplate="<b>%{x}</b><br>Sales: ₹%{y:,.2f}<extra></extra>"
)

fig_category.update_layout(
    height=450,
    margin=dict(l=20, r=20, t=70, b=40),
    plot_bgcolor="#11151d",
    paper_bgcolor="#11151d",
    font=dict(color="#ffffff"),
    title_font=dict(size=20),
    xaxis=dict(
        showgrid=False
    ),
    yaxis=dict(
        gridcolor="#292f3a",
        title="Sales (₹)"
    )
)

st.plotly_chart(
    fig_category,
    use_container_width=True
)

# --------------------------------------------------
# Monthly Sales Trend
# --------------------------------------------------
st.subheader("Monthly Sales Trend")

monthly_sales = (
    filtered_df
    .groupby(filtered_df["Order_Date"].dt.to_period("M"))["Total_Sales"]
    .sum()
    .reset_index()
)

monthly_sales["Order_Date"] = monthly_sales["Order_Date"].astype(str)

fig_monthly = px.line(
    monthly_sales,
    x="Order_Date",
    y="Total_Sales",
    title="Monthly Sales Trend",
    markers=True,
    labels={
        "Order_Date": "Month",
        "Total_Sales": "Sales (₹)"
    }
)

fig_monthly.update_traces(
    line=dict(width=3),
    marker=dict(size=7),
    hovertemplate="<b>%{x}</b><br>Sales: ₹%{y:,.2f}<extra></extra>"
)

fig_monthly.update_layout(
    height=450,
    margin=dict(l=20, r=20, t=70, b=40),
    plot_bgcolor="#11151d",
    paper_bgcolor="#11151d",
    font=dict(color="#ffffff"),
    title_font=dict(size=20),
    xaxis=dict(
        showgrid=False,
        title="Month"
    ),
    yaxis=dict(
        gridcolor="#292f3a",
        title="Sales (₹)"
    )
)

st.plotly_chart(
    fig_monthly,
    use_container_width=True
)

# --------------------------------------------------
# Sales by Region
# --------------------------------------------------
st.subheader("Sales by Region")

region_sales = (
    filtered_df.groupby("Region")["Total_Sales"]
    .sum()
    .sort_values(ascending=False)
    .reset_index()
)

fig_region = px.bar(
    region_sales,
    x="Region",
    y="Total_Sales",
    title="Sales by Region",
    labels={
        "Region": "Region",
        "Total_Sales": "Sales (₹)"
    },
    text="Total_Sales"
)

fig_region.update_traces(
    texttemplate="₹%{text:,.0f}",
    textposition="outside",
    hovertemplate="<b>%{x}</b><br>Sales: ₹%{y:,.2f}<extra></extra>"
)

fig_region.update_layout(
    height=450,
    margin=dict(l=20, r=20, t=70, b=40),
    plot_bgcolor="#11151d",
    paper_bgcolor="#11151d",
    font=dict(color="#ffffff"),
    title_font=dict(size=20),
    xaxis=dict(
        showgrid=False,
        title="Region"
    ),
    yaxis=dict(
        gridcolor="#292f3a",
        title="Sales (₹)"
    )
)

st.plotly_chart(
    fig_region,
    use_container_width=True
)

# --------------------------------------------------
# Bottom Section - Products & Customer Segment
# --------------------------------------------------
col1, col2 = st.columns(2)

# --------------------------------------------------
# Top 10 Products
# --------------------------------------------------
with col1:

    st.subheader("Top 10 Products by Sales")

    product_sales = (
        filtered_df.groupby("Product_Name")["Total_Sales"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )

    fig_products = px.bar(
    product_sales.sort_values("Total_Sales"),
    x="Total_Sales",
    y="Product_Name",
    orientation="h",
    title="Top 10 Products by Sales",
    labels={
        "Product_Name": "Product",
        "Total_Sales": "Sales (₹)"
    },
    text="Total_Sales"
)

fig_products.update_traces(
    texttemplate="₹%{text:,.0f}",
    textposition="outside",
    hovertemplate="<b>%{y}</b><br>Sales: ₹%{x:,.2f}<extra></extra>"
)

fig_products.update_layout(
    height=500,
    margin=dict(l=20, r=30, t=70, b=40),
    plot_bgcolor="#11151d",
    paper_bgcolor="#11151d",
    font=dict(color="#ffffff"),
    title_font=dict(size=20),
    xaxis=dict(
        showgrid=True,
        gridcolor="#292f3a",
        title="Sales (₹)"
    ),
    yaxis=dict(
        showgrid=False,
        title=""
    )
)
st.plotly_chart(
        fig_products,
        use_container_width=True
    )

# --------------------------------------------------
# Sales by Customer Segment
# --------------------------------------------------
with col2:

    st.subheader("Sales by Customer Segment")

    segment_sales = (
        filtered_df.groupby("Customer_Segment")["Total_Sales"]
        .sum()
        .sort_values(ascending=False)
        .reset_index()
    )

    fig_segment = px.pie(
        segment_sales,
        names="Customer_Segment",
        values="Total_Sales",
        title="Sales Distribution by Customer Segment",
        hole=0.45
    )

    fig_segment.update_traces(
        textinfo="percent+label",
        hovertemplate="<b>%{label}</b><br>Sales: ₹%{value:,.2f}<br>Share: %{percent}<extra></extra>"
    )

    fig_segment.update_layout(
        height=500,
        margin=dict(l=20, r=20, t=70, b=20),
        plot_bgcolor="#11151d",
        paper_bgcolor="#11151d",
        font=dict(color="#ffffff"),
        title_font=dict(size=20),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=-0.15,
            xanchor="center",
            x=0.5
        )
    )

    st.plotly_chart(
        fig_segment,
        use_container_width=True
    )
# --------------------------------------------------
# Monthly Sales Trend
# --------------------------------------------------
st.markdown("---")
st.subheader("📈 Monthly Sales Trend")

trend_df = filtered_df.copy()

trend_df["Order_Date"] = pd.to_datetime(
    trend_df["Order_Date"],
    errors="coerce"
)

trend_df = trend_df.dropna(subset=["Order_Date"])

if not trend_df.empty:

    trend_df["Month"] = (
        trend_df["Order_Date"]
        .dt.to_period("M")
        .astype(str)
    )

    monthly_sales = (
        trend_df.groupby("Month", as_index=False)["Total_Sales"]
        .sum()
        .sort_values("Month")
    )

    fig_trend = px.line(
        monthly_sales,
        x="Month",
        y="Total_Sales",
        title="Monthly Revenue Trend",
        markers=True,
        labels={
            "Month": "Month",
            "Total_Sales": "Total Sales (₹)"
        }
    )

    fig_trend.update_traces(
        line=dict(color="#38bdf8", width=3),
        marker=dict(size=8),
        hovertemplate=(
            "<b>%{x}</b><br>"
            "Sales: ₹%{y:,.2f}"
            "<extra></extra>"
        )
    )

    fig_trend.update_layout(
        height=420,
        plot_bgcolor="#111722",
        paper_bgcolor="#111722",
        font=dict(color="#f1f5f9"),
        title_font=dict(size=20),
        margin=dict(l=20, r=20, t=70, b=30),
        xaxis=dict(showgrid=False),
        yaxis=dict(
            showgrid=True,
            gridcolor="#293548"
        )
    )

    st.plotly_chart(
        fig_trend,
        use_container_width=True
    )

else:
    st.info("No valid order dates available for the selected filters.")

# --------------------------------------------------
# Download Filtered Sales Report
# --------------------------------------------------
st.markdown("---")
st.subheader("📥 Download Sales Report")

st.write(
    "Download the sales data based on your selected filters."
)

download_df = filtered_df.copy()

csv_data = download_df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="⬇️ Download Filtered Report (CSV)",
    data=csv_data,
    file_name="filtered_ecommerce_sales_report.csv",
    mime="text/csv",
    use_container_width=True
)

# --------------------------------------------------
# Footer
# --------------------------------------------------
st.markdown("---")
st.caption("E-Commerce Sales Analytics Dashboard | Built with Python, Streamlit & Plotly")


