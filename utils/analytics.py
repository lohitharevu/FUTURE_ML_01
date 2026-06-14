import pandas as pd

# ==========================================
# LOAD DATA
# ==========================================

def load_sales_data():

    df = pd.read_csv(
        "data/processed_sales.csv"
    )

    df["Order Date"] = pd.to_datetime(
        df["Order Date"]
    )

    return df


# ==========================================
# KPI METRICS
# ==========================================

def get_kpis():

    df = load_sales_data()

    total_sales = round(
        df["Sales"].sum(),
        2
    )

    total_profit = round(
        df["Profit"].sum(),
        2
    )

    total_orders = len(df)

    avg_order_value = round(
        total_sales / total_orders,
        2
    )

    return {
        "total_sales": total_sales,
        "total_profit": total_profit,
        "total_orders": total_orders,
        "avg_order_value": avg_order_value
    }


# ==========================================
# MONTHLY SALES TREND
# ==========================================

def monthly_sales():

    df = load_sales_data()

    monthly = (
        df.groupby(
            pd.Grouper(
                key="Order Date",
                freq="M"
            )
        )["Sales"]
        .sum()
        .reset_index()
    )

    monthly.columns = [
        "Month",
        "Sales"
    ]

    return monthly


# ==========================================
# CATEGORY PERFORMANCE
# ==========================================

def category_sales():

    df = load_sales_data()

    category = (
        df.groupby("Category")["Sales"]
        .sum()
        .reset_index()
        .sort_values(
            by="Sales",
            ascending=False
        )
    )

    return category


# ==========================================
# REGION PERFORMANCE
# ==========================================

def region_sales():

    df = load_sales_data()

    region = (
        df.groupby("Region")["Sales"]
        .sum()
        .reset_index()
        .sort_values(
            by="Sales",
            ascending=False
        )
    )

    return region


# ==========================================
# TOP PRODUCTS
# ==========================================

def top_products(top_n=10):

    df = load_sales_data()

    products = (
        df.groupby(
            "Product Name"
        )["Sales"]
        .sum()
        .reset_index()
        .sort_values(
            by="Sales",
            ascending=False
        )
        .head(top_n)
    )

    return products


# ==========================================
# PROFIT ANALYSIS
# ==========================================

def profit_analysis():

    df = load_sales_data()

    profit = (
        df.groupby("Category")["Profit"]
        .sum()
        .reset_index()
        .sort_values(
            by="Profit",
            ascending=False
        )
    )

    return profit


# ==========================================
# DEMAND ANALYSIS
# ==========================================

def demand_analysis():

    df = load_sales_data()

    demand = (
        df.groupby(
            "Product Name"
        )["Quantity"]
        .sum()
        .reset_index()
        .sort_values(
            by="Quantity",
            ascending=False
        )
    )

    high_demand = demand.head(10)

    low_demand = demand.tail(10)

    return high_demand, low_demand


# ==========================================
# GROWTH RATE
# ==========================================

def sales_growth_rate():

    monthly = monthly_sales()

    if len(monthly) < 2:
        return 0

    latest = monthly.iloc[-1]["Sales"]

    previous = monthly.iloc[-2]["Sales"]

    growth = (
        (latest - previous)
        / previous
    ) * 100

    return round(growth, 2)


# ==========================================
# BUSINESS HEALTH SCORE
# ==========================================

def business_health_score():

    growth = sales_growth_rate()

    if growth >= 15:
        return 95

    elif growth >= 10:
        return 85

    elif growth >= 5:
        return 75

    elif growth >= 0:
        return 65

    else:
        return 50