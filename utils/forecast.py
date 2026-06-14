import pandas as pd
import joblib
from datetime import timedelta

# ==========================================
# LOAD MODEL
# ==========================================

model = joblib.load(
    "models/forecast_model.pkl"
)

# ==========================================
# RECURSIVE FORECAST
# ==========================================

def forecast_sales(days=30):

    sales_df = pd.read_csv(
        "data/processed_sales.csv"
    )

    sales_df["Order Date"] = pd.to_datetime(
        sales_df["Order Date"]
    )

    sales_df = sales_df.sort_values(
        "Order Date"
    )

    history = list(
        sales_df["Sales"].tail(30)
    )

    future_rows = []

    last_date = sales_df[
        "Order Date"
    ].max()

    for i in range(days):

        future_date = (
            last_date +
            timedelta(days=i + 1)
        )

        lag_1 = history[-1]

        lag_7 = (
            history[-7]
            if len(history) >= 7
            else lag_1
        )

        lag_30 = (
            history[-30]
            if len(history) >= 30
            else lag_1
        )

        rolling_7 = (
            sum(history[-7:])
            / min(7, len(history))
        )

        rolling_30 = (
            sum(history[-30:])
            / min(30, len(history))
        )

        row = {

            "Year":
            future_date.year,

            "Month":
            future_date.month,

            "Day":
            future_date.day,

            "Weekday":
            future_date.weekday(),

            "Quarter":
            future_date.quarter,

            "WeekOfYear":
            future_date.isocalendar().week,

            "Sales_Lag_1":
            lag_1,

            "Sales_Lag_7":
            lag_7,

            "Sales_Lag_30":
            lag_30,

            "Rolling_Mean_7":
            rolling_7,

            "Rolling_Mean_30":
            rolling_30
        }

        prediction = model.predict(
            pd.DataFrame([row])
        )[0]

        history.append(
            prediction
        )

        future_rows.append({

            "Date":
            future_date,

            "Forecast Sales":
            round(prediction, 2)
        })

    return pd.DataFrame(
        future_rows
    )

# ==========================================
# FORECAST INSIGHTS
# ==========================================

def generate_insights(
    forecast_df
):

    avg_sales = round(
        forecast_df[
            "Forecast Sales"
        ].mean(),
        2
    )

    peak_sales = round(
        forecast_df[
            "Forecast Sales"
        ].max(),
        2
    )

    lowest_sales = round(
        forecast_df[
            "Forecast Sales"
        ].min(),
        2
    )

    insights = [

        f"Average expected sales: {avg_sales}",

        f"Peak forecast sales: {peak_sales}",

        f"Lowest forecast sales: {lowest_sales}"
    ]

    if avg_sales > 500:

        insights.append(
            "Demand expected to remain strong."
        )

    elif avg_sales > 250:

        insights.append(
            "Demand expected to remain stable."
        )

    else:

        insights.append(
            "Demand expected to remain moderate."
        )

    return insights

# ==========================================
# INVENTORY ALERT
# ==========================================

def inventory_alert(
    forecast_df
):

    avg_sales = forecast_df[
        "Forecast Sales"
    ].mean()

    if avg_sales > 500:

        return (
            "🔴 High demand expected. "
            "Increase inventory levels."
        )

    elif avg_sales > 250:

        return (
            "🟡 Moderate demand expected. "
            "Monitor stock levels."
        )

    else:

        return (
            "🟢 Inventory levels are sufficient."
        )