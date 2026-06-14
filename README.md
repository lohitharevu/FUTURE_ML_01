# 🚀 ForecastIQ AI

ForecastIQ AI is an AI-powered Sales Forecasting and Business Intelligence platform that helps businesses predict future sales, analyze performance, optimize inventory, and generate actionable insights using Machine Learning.

---

## ✨ Features

- 📈 Sales Forecasting
- 📦 Inventory Intelligence
- 📊 Business Analytics
- 🧠 AI Business Insights
- ❤️ Business Health Monitoring
- 📉 Demand Trend Analysis
- 📋 Executive Summary Reports

---

## 🛠️ Tech Stack

- Python
- Streamlit
- Pandas
- NumPy
- Scikit-Learn
- Plotly
- Joblib

---

## 🤖 Machine Learning Model

ForecastIQ AI uses a **Random Forest Regressor** trained on historical sales data.

### Features Used

- Year
- Month
- Day
- Weekday
- Quarter
- WeekOfYear
- Sales Lag Features
- Rolling Average Features

### Target

```text
Sales
```

---

## 📂 Project Structure

```text
FUTURE_ML_01
│
├── app.py
├── requirements.txt
├── README.md
│
├── data/
│   ├── sales.csv
│   └── processed_sales.csv
│
├── scripts/
│   ├── preprocess.py
│   └── train_model.py
│
└── utils/
    ├── forecast.py
    ├── analytics.py
    ├── inventory.py
    └── insights.py
```

---

## 📥 Installation

```bash
git clone https://github.com/lohitharevu/FUTURE_ML_01.git
cd FUTURE_ML_01
pip install -r requirements.txt
```

---

## 🧠 Generate Model

The trained model file is not included due to its large size.

Generate it locally:

```bash
python scripts/train_model.py
```

This creates:

```text
models/forecast_model.pkl
```

---

## ▶️ Run Application

```bash
streamlit run app.py
```

---

## 📊 Business Value

ForecastIQ AI helps businesses:

- Predict future demand
- Improve inventory planning
- Analyze sales trends
- Identify top-performing products
- Support data-driven decision making

---

## ⚠️ Disclaimer

Forecasts are generated using machine learning and historical data. Prediction accuracy depends on dataset quality and business conditions.

---

## 👩‍💻 Author

**Lohitha Revu**  

---

