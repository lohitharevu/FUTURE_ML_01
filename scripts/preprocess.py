import pandas as pd

# ==========================================
# LOAD DATASET
# ==========================================

print("Loading dataset...")

df = pd.read_csv(
    "data/sales.csv",
    encoding="latin1"
)

# ==========================================
# DATE CONVERSION
# ==========================================

df["Order Date"] = pd.to_datetime(
    df["Order Date"],
    errors="coerce"
)

# Remove invalid dates
df = df.dropna(
    subset=["Order Date"]
)

# ==========================================
# HANDLE MISSING VALUES
# ==========================================

df = df.fillna(0)

# ==========================================
# TIME FEATURES
# ==========================================

df["Year"] = df["Order Date"].dt.year

df["Month"] = df["Order Date"].dt.month

df["Day"] = df["Order Date"].dt.day

df["Weekday"] = df["Order Date"].dt.weekday

df["Quarter"] = df["Order Date"].dt.quarter

df["WeekOfYear"] = (
    df["Order Date"]
    .dt.isocalendar()
    .week
)

# ==========================================
# SALES TREND FEATURE
# ==========================================

df = df.sort_values(
    "Order Date"
)

df["Sales_Lag_1"] = (
    df["Sales"]
    .shift(1)
)

df["Sales_Lag_7"] = (
    df["Sales"]
    .shift(7)
)

df["Sales_Lag_30"] = (
    df["Sales"]
    .shift(30)
)

# ==========================================
# MOVING AVERAGES
# ==========================================

df["Rolling_Mean_7"] = (
    df["Sales"]
    .rolling(7)
    .mean()
)

df["Rolling_Mean_30"] = (
    df["Sales"]
    .rolling(30)
    .mean()
)

# ==========================================
# REMOVE NULLS CREATED BY LAGS
# ==========================================

df = df.fillna(0)

# ==========================================
# SAVE PROCESSED DATA
# ==========================================

df.to_csv(
    "data/processed_sales.csv",
    index=False
)

print("Processed data saved successfully.")
print(f"Rows: {len(df)}")
print(f"Columns: {len(df.columns)}")