# Mumbai_power_demand_forecasting

Overview

This project aims to forecast Mumbai's power demand using the ARIMA (AutoRegressive Integrated Moving Average) model. The goal is to analyze historical power consumption data and predict future demand patterns, aiding in better resource allocation and load balancing.

Dataset

The dataset should include:

Timestamp: Date and time of power consumption recording.

Power Demand (MW): Historical power demand data.

Temperature, Humidity, and Weather Conditions (Optional): To analyze external factors affecting demand.

Prerequisites

Libraries Required

Ensure you have the following Python libraries installed:

pip install pandas numpy matplotlib seaborn statsmodels pmdarima

Or import them directly in Python:

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.arima.model import ARIMA
from pmdarima import auto_arima

Methodology

Data Preprocessing:

Load the dataset.

Handle missing values.

Convert the time column to a DateTime format.

Resample data (daily/hourly aggregation if needed).

Exploratory Data Analysis (EDA):

Visualize the power demand trend.

Check for seasonality, trends, and stationarity.

Stationarity Check:

Use the Augmented Dickey-Fuller (ADF) test to check stationarity.

If non-stationary, apply differencing to stabilize variance.

Model Selection:

Use Auto-ARIMA to determine the best (p, d, q) parameters.

Train the ARIMA model using the selected parameters.

Model Training & Evaluation:

Split data into training and testing sets.

Train the ARIMA model.

Forecast and compare predictions with actual values using metrics like MAE, RMSE.

Future Forecasting:

Predict power demand for upcoming periods.

Visualize results with confidence intervals.

Model Implementation

1. Load Data

df = pd.read_csv('mumbai_power_demand.csv')
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)

2. Check Stationarity

from statsmodels.tsa.stattools import adfuller

def check_stationarity(series):
    result = adfuller(series)
    print(f'ADF Statistic: {result[0]}')
    print(f'p-value: {result[1]}')
    if result[1] <= 0.05:
        print("✅ Data is Stationary")
    else:
        print("❌ Data is NOT Stationary")

check_stationarity(df['Power_Demand'])

3. Fit ARIMA Model

model = ARIMA(df['Power_Demand'], order=(p,d,q))  # Replace with best values from Auto-ARIMA
model_fit = model.fit()
print(model_fit.summary())

4. Forecast Future Demand

forecast = model_fit.forecast(steps=30)  # Predict next 30 days
plt.figure(figsize=(10,5))
plt.plot(df['Power_Demand'], label='Actual Demand')
plt.plot(pd.date_range(start=df.index[-1], periods=31, freq='D')[1:], forecast, label='Forecasted Demand', color='red')
plt.legend()
plt.show()

Results & Insights

The model successfully captures the trend and seasonal variations.
