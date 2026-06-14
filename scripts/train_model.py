import pandas as pd
import joblib

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

# ==========================================
# LOAD DATA
# ==========================================

print("Loading processed dataset...")

df = pd.read_csv(
    "data/processed_sales.csv"
)

# ==========================================
# FEATURES
# ==========================================

features = [

    "Year",
    "Month",
    "Day",
    "Weekday",
    "Quarter",
    "WeekOfYear",

    "Sales_Lag_1",
    "Sales_Lag_7",
    "Sales_Lag_30",

    "Rolling_Mean_7",
    "Rolling_Mean_30"
]

target = "Sales"

# ==========================================
# X AND y
# ==========================================

X = df[features]

y = df[target]

# ==========================================
# TRAIN TEST SPLIT
# ==========================================

X_train, X_test, y_train, y_test = train_test_split(

    X,
    y,

    test_size=0.2,

    random_state=42
)

# ==========================================
# MODEL
# ==========================================

print("Training model...")

model = RandomForestRegressor(

    n_estimators=300,

    max_depth=15,

    random_state=42,

    n_jobs=-1
)

model.fit(

    X_train,
    y_train
)

# ==========================================
# PREDICTIONS
# ==========================================

predictions = model.predict(
    X_test
)

# ==========================================
# EVALUATION
# ==========================================

mae = mean_absolute_error(

    y_test,
    predictions
)

mse = mean_squared_error(

    y_test,
    predictions
)

rmse = mse ** 0.5

r2 = r2_score(

    y_test,
    predictions
)

print("\n========== MODEL PERFORMANCE ==========")

print(f"MAE  : {mae:.2f}")

print(f"RMSE : {rmse:.2f}")

print(f"R²   : {r2:.4f}")

# ==========================================
# FEATURE IMPORTANCE
# ==========================================

importance_df = pd.DataFrame({

    "Feature": features,

    "Importance":
    model.feature_importances_
})

importance_df = importance_df.sort_values(

    by="Importance",

    ascending=False
)

print("\n========== FEATURE IMPORTANCE ==========")

print(importance_df)

# ==========================================
# SAVE MODEL
# ==========================================

joblib.dump(

    model,

    "models/forecast_model.pkl"
)

print("\nModel saved successfully.")

print(
    "models/forecast_model.pkl"
)