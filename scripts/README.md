# Scripts Folder

This folder contains Python scripts designed for stock data analysis, including data preprocessing, exploratory data analysis (EDA), and time series analysis. Each script includes functions and classes that perform specific analytical tasks. Logging is configured to capture detailed information and errors for debugging and monitoring purposes.

## File Structure

```
scripts/
├── data_preprocessing.py  # Script for data fetching and preprocessing
├── EDA.py                 # Script for exploratory data analysis (EDA)
├── time_series_analysis.py # Script for time series analysis
└── logs/                  # Folder for log files (info and error logs)
```

## Scripts Overview

### `data_preprocessing.py`

This script handles data fetching and preprocessing for stock analysis. It includes functions for loading historical stock data from Yahoo Finance, examining data summaries, and identifying missing values.

- **Key Functions**:
    - `get_stock_data(stock_symbol, start_date, end_date)`: Fetches stock data within a date range and removes unwanted columns.
    - `data_understanding(df)`: Logs and displays basic data information, summaries, and missing values.
    - `missing_values_table(df)`: Creates a table summarizing missing values and their percentage in each column.

- **Logging**: Captures data shape, column information, and any errors during data retrieval.

### `EDA.py`

This script performs exploratory data analysis on stock data, focusing on price trends, daily returns, and volatility.

- **Key Class**:
    - `StockEDA(df)`: A class for performing EDA on stock data.
        - `plot_closing_price()`: Plots the closing price over time.
        - `plot_daily_percentage_change()`: Calculates and plots daily percentage changes.
        - `analyze_volatility(window)`: Analyzes volatility using a specified rolling window.
        - `detect_outliers()`: Identifies outliers in closing prices based on Z-scores.
        - `analyze_extreme_returns(threshold)`: Highlights days with extreme returns.

- **Logging**: Captures actions such as plotting and outlier detection with log outputs for tracking.

### `time_series_analysis.py`

This script is focused on time series analysis, specifically for decomposing stock data into components like trend, seasonality, and residuals.

- **Key Class**:
    - `TimeSeriesAnalysis(df)`: A class for time series decomposition and volatility analysis.
        - `decompose_time_series(freq)`: Decomposes time series into observed, trend, seasonal, and residual components.
        - `plot_rolling_volatility(window)`: Plots rolling standard deviation to analyze volatility over a specified window.

- **Logging**: Tracks analysis steps and highlights details like decomposition results and volatility trends.

## Logs Directory

The `logs` directory contains:
- `info.log`: Logs general information about the execution flow.
- `error.log`: Logs errors encountered during the execution of the scripts.

## Usage

1. Place the scripts in a working directory.
2. Install dependencies using:
     ```bash
     pip install yfinance pandas matplotlib statsmodels
     ```
3. Run the scripts as required for data preprocessing, EDA, and time series analysis.

Each script can be imported into a larger pipeline or used independently for stock data analysis tasks.

## License

This project is licensed under the MIT License.

This `README.md` provides an overview of the `scripts` folder contents and functionality, making it easier for users to understand and use each script effectively.
