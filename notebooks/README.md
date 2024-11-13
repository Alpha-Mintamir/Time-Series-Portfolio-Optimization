# Notebooks for Time-Series Portfolio Optimization

This folder contains Jupyter notebooks that document the step-by-step analysis and modeling of time series data for Tesla (TSLA), SPY ETF (SPY), and Bond ETF (BND) assets. Each notebook focuses on a key aspect of the project, including data preprocessing, exploratory data analysis (EDA), time series analysis, and forecasting using SARIMA models.

## Notebooks Overview

### 1. `pre-processing.ipynb`
   - **Purpose**: This notebook handles data collection, cleaning, and initial processing.
   - **Key Steps**:
     - Data import for each asset.
     - Handling missing values, outliers, and data type conversions.
     - Feature engineering, such as creating log returns or calculating moving averages.
   - **Outputs**: Cleaned and processed CSV files for TSLA, SPY, and BND, saved in the `data/` directory.

### 2. `EDA.ipynb`
   - **Purpose**: Perform exploratory data analysis to understand trends, seasonality, and overall patterns in the historical price data of each asset.
   - **Key Steps**:
     - **Closing Price Analysis**: Visualizes daily closing prices for each asset.
     - **Return Analysis**: Calculates and visualizes daily percentage returns.
     - **Volatility Analysis**: Examines the rolling volatility to assess risk.
     - **Correlation Analysis**: Explores correlations between TSLA, SPY, and BND.
   - **Outputs**: Visualizations and summary statistics to help understand asset behavior over time.

### 3. `time_series_analysis.ipynb`
   - **Purpose**: This notebook dives into time series-specific analysis, including decomposition and volatility modeling.
   - **Key Steps**:
     - **Decomposition**: Breaks down each time series into trend, seasonality, and residual components.
     - **Volatility Modeling**: Uses rolling windows to capture the dynamic volatility of each asset.
     - **Stationarity Tests**: Conducts tests (e.g., ADF test) to check for stationarity in the time series.
   - **Outputs**: Plots for decomposed components, volatility, and test results for stationarity.

### 4. `time_series_model_and_portfolio_optimization.ipynb`
   - **Purpose**: Forecast future prices for each asset using SARIMA models and perform portfolio optimization based on forecasted returns.
   - **Key Steps**:
     - **SARIMA Modeling**: Fits SARIMA models to each asset’s historical prices to forecast future values.
     - **Model Evaluation**: Calculates metrics like Mean Absolute Error (MAE), Root Mean Square Error (RMSE), and Mean Absolute Percentage Error (MAPE) to assess model performance.
     - **Portfolio Optimization**: Uses forecasted returns to construct an optimized portfolio balancing risk and return.
   - **Outputs**: Forecasted prices, evaluation metrics, and portfolio weight recommendations.

## Running the Notebooks

Each notebook is designed to be run sequentially, starting from `pre-processing.ipynb` to `time_series_model_and_portfolio_optimization.ipynb`. To execute these notebooks:

1. Open the notebook in JupyterLab, Jupyter Notebook, or any compatible editor.
2. Run each cell in order to replicate the data processing, analysis, and forecasting steps.
3. Ensure that required dependencies are installed (check the root `requirements.txt` for all necessary packages).

## Requirements

- Python 3.x
- Jupyter Notebook or JupyterLab
- Required libraries are listed in the root `requirements.txt` and can be installed via:
   ```bash
   pip install -r requirements.txt
