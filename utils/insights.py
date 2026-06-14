import pandas as pd

# ==========================================
# LOAD DATA
# ==========================================

def load_data():

    df = pd.read_csv(
        "data/processed_sales.csv"
    )

    df["Order Date"] = pd.to_datetime(
        df["Order Date"]
    )

    return df


# ==========================================
# SALES INSIGHTS
# ==========================================

def sales_insights():

    df = load_data()

    total_sales = round(
        df["Sales"].sum(),
        2
    )

    avg_sales = round(
        df["Sales"].mean(),
        2
    )

    max_sale = round(
        df["Sales"].max(),
        2
    )

    insights = []

    insights.append(
        f"Total revenue generated is {total_sales}."
    )

    insights.append(
        f"Average order value is {avg_sales}."
    )

    insights.append(
        f"Highest recorded sale is {max_sale}."
    )

    return insights


# ==========================================
# CATEGORY INSIGHTS
# ==========================================

def category_insights():

    df = load_data()

    category_sales = (
        df.groupby("Category")["Sales"]
        .sum()
        .sort_values(
            ascending=False
        )
    )

    best_category = category_sales.index[0]
    best_sales = round(
        category_sales.iloc[0],
        2
    )

    worst_category = category_sales.index[-1]
    worst_sales = round(
        category_sales.iloc[-1],
        2
    )

    insights = []

    insights.append(
        f"Top-performing category is {best_category} with sales of {best_sales}."
    )

    insights.append(
        f"Lowest-performing category is {worst_category} with sales of {worst_sales}."
    )

    insights.append(
        f"Focus inventory and marketing efforts on {best_category}."
    )

    return insights


# ==========================================
# REGION INSIGHTS
# ==========================================

def region_insights():

    df = load_data()

    region_sales = (
        df.groupby("Region")["Sales"]
        .sum()
        .sort_values(
            ascending=False
        )
    )

    best_region = region_sales.index[0]
    best_sales = round(
        region_sales.iloc[0],
        2
    )

    insights = []

    insights.append(
        f"{best_region} region generates the highest revenue."
    )

    insights.append(
        f"Total sales from {best_region} region: {best_sales}."
    )

    insights.append(
        f"Consider expanding operations in {best_region}."
    )

    return insights


# ==========================================
# PROFIT INSIGHTS
# ==========================================

def profit_insights():

    df = load_data()

    total_profit = round(
        df["Profit"].sum(),
        2
    )

    avg_profit = round(
        df["Profit"].mean(),
        2
    )

    insights = []

    insights.append(
        f"Total profit generated is {total_profit}."
    )

    insights.append(
        f"Average profit per order is {avg_profit}."
    )

    if total_profit > 0:

        insights.append(
            "Business operations are profitable overall."
        )

    else:

        insights.append(
            "Business is operating at a loss."
        )

    return insights


# ==========================================
# DEMAND INSIGHTS
# ==========================================

def demand_insights():

    df = load_data()

    demand = (
        df.groupby("Product Name")["Quantity"]
        .sum()
        .sort_values(
            ascending=False
        )
    )

    top_product = demand.index[0]
    quantity = int(
        demand.iloc[0]
    )

    insights = []

    insights.append(
        f"Highest demand product is {top_product}."
    )

    insights.append(
        f"Total units sold: {quantity}."
    )

    insights.append(
        f"Maintain higher inventory levels for this product."
    )

    return insights


# ==========================================
# SEASONAL INSIGHTS
# ==========================================

def seasonal_insights():

    df = load_data()

    df["Month"] = (
        df["Order Date"]
        .dt.month
    )

    monthly_sales = (
        df.groupby("Month")["Sales"]
        .sum()
        .sort_values(
            ascending=False
        )
    )

    peak_month = monthly_sales.index[0]

    insights = []

    insights.append(
        f"Peak sales month is {peak_month}."
    )

    insights.append(
        "Historical data indicates seasonal purchasing behavior."
    )

    insights.append(
        "Prepare inventory before peak demand periods."
    )

    return insights


# ==========================================
# AI BUSINESS RECOMMENDATIONS
# ==========================================

def business_recommendations():

    recommendations = [

        "Increase inventory for high-demand products.",

        "Focus marketing campaigns on top-performing categories.",

        "Expand operations in high-revenue regions.",

        "Monitor low-performing products and optimize stock levels.",

        "Use demand forecasts to improve procurement planning.",

        "Prepare additional staffing during peak sales periods."
    ]

    return recommendations


# ==========================================
# EXECUTIVE SUMMARY
# ==========================================

def executive_summary():

    summary = []

    summary.extend(
        sales_insights()
    )

    summary.extend(
        category_insights()
    )

    summary.extend(
        region_insights()
    )

    return summary