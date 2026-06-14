import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from utils.forecast import (
    forecast_sales,
    generate_insights,
    inventory_alert
)

from utils.analytics import (
    get_kpis,
    monthly_sales,
    category_sales,
    region_sales,
    top_products,
    profit_analysis,
    sales_growth_rate,
    business_health_score
)

from utils.inventory import (
    inventory_summary,
    high_demand_products,
    low_demand_products,
    stock_recommendations,
    inventory_alerts,
    restock_plan,
    product_performance
)

from utils.insights import (
    executive_summary,
    business_recommendations,
    demand_insights,
    seasonal_insights,
    profit_insights
)

# ==================================================
# PAGE CONFIG
# ==================================================

st.set_page_config(
    page_title="ForecastIQ AI",
    page_icon="📈",
    layout="wide"
)

# ==================================================
# CUSTOM CSS
# ==================================================

st.markdown("""
<style>

.main{
    background-color:#f8fafc;
}

.metric-card{
    background:white;
    padding:15px;
    border-radius:15px;
    box-shadow:0px 2px 8px rgba(0,0,0,0.08);
}

</style>
""", unsafe_allow_html=True)

# ==================================================
# HEADER
# ==================================================

st.title("📈 ForecastIQ AI")

st.caption(
    "AI-Powered Sales Forecasting & Business Intelligence Platform"
)

st.divider()

# ==================================================
# SIDEBAR
# ==================================================

st.sidebar.title("📈 ForecastIQ AI")

if "page" not in st.session_state:
    st.session_state.page = "Dashboard"

if st.sidebar.button("📊 Dashboard"):
    st.session_state.page = "Dashboard"

if st.sidebar.button("🔮 Sales Forecasting"):
    st.session_state.page = "Sales Forecasting"

if st.sidebar.button("📦 Inventory Intelligence"):
    st.session_state.page = "Inventory Intelligence"

if st.sidebar.button("🧠 Business Insights"):
    st.session_state.page = "Business Insights"

if st.sidebar.button("📉 Analytics"):
    st.session_state.page = "Analytics"

page = st.session_state.page

# ==================================================
# DASHBOARD
# ==================================================

if page == "Dashboard":

    st.header("📊 Executive Dashboard")

    kpis = get_kpis()

    growth = sales_growth_rate()

    health = business_health_score()

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "💰 Total Sales",
        f"${kpis['total_sales']:,.0f}"
    )

    c2.metric(
        "📈 Total Profit",
        f"${kpis['total_profit']:,.0f}"
    )

    c3.metric(
        "🧾 Orders",
        f"{kpis['total_orders']:,}"
    )

    c4.metric(
        "❤️ Health Score",
        f"{health}%"
    )

    st.divider()

    left, right = st.columns(2)

    with left:

        st.subheader("📈 Monthly Sales Trend")

        monthly = monthly_sales()

        fig = px.line(
            monthly,
            x="Month",
            y="Sales",
            markers=True
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    with right:

        st.subheader("🚀 Growth Rate")

        st.metric(
            "Month-over-Month Growth",
            f"{growth}%"
        )

        categories = category_sales()

        fig = px.pie(
            categories,
            names="Category",
            values="Sales"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    st.divider()

    st.subheader("🏆 Top Products")

    top_df = top_products()

    st.dataframe(
        top_df,
        use_container_width=True
    )

# ==================================================
# SALES FORECASTING
# ==================================================

elif page == "Sales Forecasting":

    st.header("🔮 Sales Forecasting")

    days = st.slider(
        "Select Forecast Horizon (Days)",
        min_value=1,
        max_value=365,
        value=30
    )

    if st.button("Generate Forecast"):

        forecast_df = forecast_sales(days)

        st.success(
            "Forecast Generated Successfully"
        )

        avg_forecast = round(
            forecast_df["Forecast Sales"].mean(),
            2
        )

        max_forecast = round(
            forecast_df["Forecast Sales"].max(),
            2
        )

        min_forecast = round(
            forecast_df["Forecast Sales"].min(),
            2
        )

        a, b, c = st.columns(3)

        a.metric(
            "Average Forecast",
            f"${avg_forecast:,.0f}"
        )

        b.metric(
            "Peak Forecast",
            f"${max_forecast:,.0f}"
        )

        c.metric(
            "Lowest Forecast",
            f"${min_forecast:,.0f}"
        )

        st.divider()

        fig = px.line(
            forecast_df,
            x="Date",
            y="Forecast Sales",
            markers=True,
            title="Future Sales Forecast"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

        st.subheader(
            "📋 Forecast Table"
        )

        st.dataframe(
            forecast_df,
            use_container_width=True
        )

        st.divider()

        st.subheader(
            "🧠 Forecast Insights"
        )

        insights = generate_insights(
            forecast_df
        )

        for item in insights:

            st.info(item)

        st.subheader(
            "📦 Inventory Alert"
        )

        st.warning(
            inventory_alert(
                forecast_df
            )
        )
        
# ==================================================
# INVENTORY INTELLIGENCE
# ==================================================

elif page == "Inventory Intelligence":

    st.header("📦 Inventory Intelligence")

    summary = inventory_summary()

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "🔥 High Demand",
        summary["high_demand_products"]
    )

    c2.metric(
        "📉 Low Demand",
        summary["low_demand_products"]
    )

    c3.metric(
        "⚠️ Risk Products",
        summary["risk_products"]
    )

    c4.metric(
        "❤️ Inventory Health",
        f"{summary['inventory_health']}%"
    )

    st.divider()

    left, right = st.columns(2)

    with left:

        st.subheader(
            "🔥 High Demand Products"
        )

        high_df = high_demand_products()

        st.dataframe(
            high_df,
            use_container_width=True
        )

    with right:

        st.subheader(
            "📉 Low Demand Products"
        )

        low_df = low_demand_products()

        st.dataframe(
            low_df,
            use_container_width=True
        )

    st.divider()

    st.subheader(
        "📦 Restock Plan"
    )

    st.dataframe(
        restock_plan(),
        use_container_width=True
    )

    st.divider()

    st.subheader(
        "⚠️ Inventory Alerts"
    )

    alerts = inventory_alerts()

    for alert in alerts:

        st.warning(alert)

    st.divider()

    st.subheader(
        "💡 Stock Recommendations"
    )

    recommendations = stock_recommendations()

    for rec in recommendations:

        st.success(rec)

# ==================================================
# BUSINESS INSIGHTS
# ==================================================

elif page == "Business Insights":

    st.header(
        "🧠 Business Intelligence"
    )

    st.subheader(
        "📋 Executive Summary"
    )

    summary = executive_summary()

    for item in summary:

        st.info(item)

    st.divider()

    st.subheader(
        "💰 Profit Insights"
    )

    for item in profit_insights():

        st.success(item)

    st.divider()

    st.subheader(
        "📦 Demand Insights"
    )

    for item in demand_insights():

        st.info(item)

    st.divider()

    st.subheader(
        "🌤 Seasonal Insights"
    )

    for item in seasonal_insights():

        st.warning(item)

    st.divider()

    st.subheader(
        "🚀 Business Recommendations"
    )

    recommendations = business_recommendations()

    for rec in recommendations:

        st.success(rec)

# ==================================================
# ANALYTICS
# ==================================================

elif page == "Analytics":

    st.header(
        "📊 Business Analytics"
    )

    st.subheader(
        "🌍 Regional Performance"
    )

    region_df = region_sales()

    fig = px.bar(
        region_df,
        x="Region",
        y="Sales",
        color="Sales",
        title="Sales by Region"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.divider()

    st.subheader(
        "📦 Category Performance"
    )

    category_df = category_sales()

    fig = px.bar(
        category_df,
        x="Category",
        y="Sales",
        color="Sales",
        title="Sales by Category"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.divider()

    st.subheader(
        "💰 Profit Analysis"
    )

    profit_df = profit_analysis()

    fig = px.bar(
        profit_df,
        x="Category",
        y="Profit",
        color="Profit",
        title="Profit by Category"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.divider()

    st.subheader(
        "🏆 Product Performance"
    )

    product_df = product_performance()

    st.dataframe(
        product_df,
        use_container_width=True
    )

# ==================================================
# FOOTER
# ==================================================

st.divider()

st.caption(
    """
ForecastIQ AI • Sales Forecasting • Demand Intelligence • Inventory Optimization • Business Analytics
"""
)

st.caption(
    """
Disclaimer: Forecasts, insights and recommendations are generated using machine learning models trained on historical data. Prediction accuracy depends on data quality, feature engineering and market conditions.
"""
)