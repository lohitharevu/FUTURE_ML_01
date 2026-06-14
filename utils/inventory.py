import pandas as pd

# ==========================================
# LOAD DATA
# ==========================================

def load_data():

    df = pd.read_csv(
        "data/processed_sales.csv"
    )

    return df


# ==========================================
# INVENTORY HEALTH SCORE
# ==========================================

def inventory_health_score():

    df = load_data()

    avg_quantity = df["Quantity"].mean()

    if avg_quantity >= 5:
        return 95

    elif avg_quantity >= 4:
        return 85

    elif avg_quantity >= 3:
        return 75

    elif avg_quantity >= 2:
        return 65

    else:
        return 50


# ==========================================
# HIGH DEMAND PRODUCTS
# ==========================================

def high_demand_products(top_n=10):

    df = load_data()

    high_demand = (
        df.groupby("Product Name")["Quantity"]
        .sum()
        .reset_index()
        .sort_values(
            by="Quantity",
            ascending=False
        )
        .head(top_n)
    )

    return high_demand


# ==========================================
# LOW DEMAND PRODUCTS
# ==========================================

def low_demand_products(top_n=10):

    df = load_data()

    low_demand = (
        df.groupby("Product Name")["Quantity"]
        .sum()
        .reset_index()
        .sort_values(
            by="Quantity",
            ascending=True
        )
        .head(top_n)
    )

    return low_demand


# ==========================================
# STOCK RECOMMENDATIONS
# ==========================================

def stock_recommendations():

    high_products = high_demand_products(5)

    recommendations = []

    for _, row in high_products.iterrows():

        recommendations.append(
            f"Increase stock for {row['Product Name']} "
            f"(Demand: {int(row['Quantity'])} units)"
        )

    return recommendations


# ==========================================
# INVENTORY RISK ANALYSIS
# ==========================================

def inventory_risk():

    df = load_data()

    demand = (
        df.groupby("Product Name")["Quantity"]
        .sum()
        .reset_index()
    )

    high_risk = demand[
        demand["Quantity"] >= demand["Quantity"].quantile(0.90)
    ]

    return high_risk


# ==========================================
# PRODUCT PERFORMANCE
# ==========================================

def product_performance(top_n=15):

    df = load_data()

    performance = (
        df.groupby("Product Name")
        .agg({
            "Sales": "sum",
            "Profit": "sum",
            "Quantity": "sum"
        })
        .reset_index()
        .sort_values(
            by="Sales",
            ascending=False
        )
        .head(top_n)
    )

    return performance


# ==========================================
# INVENTORY ALERTS
# ==========================================

def inventory_alerts():

    alerts = []

    high_risk_products = inventory_risk()

    for _, row in high_risk_products.iterrows():

        alerts.append(
            f"⚠️ High demand detected for "
            f"{row['Product Name']} "
            f"({int(row['Quantity'])} units sold)"
        )

    return alerts


# ==========================================
# RESTOCK SUGGESTIONS
# ==========================================

def restock_plan():

    products = high_demand_products(10)

    restock = []

    for _, row in products.iterrows():

        recommended_stock = int(
            row["Quantity"] * 1.25
        )

        restock.append({

            "Product": row["Product Name"],

            "Current Demand":
            int(row["Quantity"]),

            "Recommended Stock":
            recommended_stock
        })

    return pd.DataFrame(restock)


# ==========================================
# INVENTORY DASHBOARD DATA
# ==========================================

def inventory_summary():

    high_count = len(
        high_demand_products()
    )

    low_count = len(
        low_demand_products()
    )

    risk_count = len(
        inventory_risk()
    )

    return {

        "high_demand_products":
        high_count,

        "low_demand_products":
        low_count,

        "risk_products":
        risk_count,

        "inventory_health":
        inventory_health_score()
    }