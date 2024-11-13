# Stock Market Analysis Project

Welcome to the Stock Market Analysis Project! This project, created by [alpha-mintamir](https://github.com/alpha-mintamir), focuses on analyzing stock market data using Python. The repository includes scripts for data preprocessing, exploratory data analysis (EDA), and time series analysis to help gain insights into stock trends, volatility, and performance.

## Project Structure

```
.
├── data/                      # Folder for storing raw and processed data
├── notebook/                  # Jupyter notebooks for interactive analysis
├── scripts/                   # Python scripts for reusable functions
│   ├── data_preprocessing.py  # Script for data fetching and preprocessing
│   ├── EDA.py                 # Script for exploratory data analysis (EDA)
│   ├── time_series_analysis.py# Script for time series analysis
│   └── logs/                  # Folder for log files (info and error logs)
├── README.md                  # Project documentation
├── requirements.txt           # List of dependencies
└── quantitative_analysis.ipynb# Main notebook for analysis
```

## Project Overview

The project is designed to streamline the analysis of stock data, allowing users to:
1. **Fetch and preprocess** stock data from Yahoo Finance.
2. **Explore and analyze** the data for patterns, trends, and anomalies.
3. **Decompose time series** data to identify trend and seasonal components.
4. **Visualize findings** to gain a deeper understanding of stock behavior.

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/alpha-mintamir/stock-market-analysis.git
    cd stock-market-analysis
    ```

2. **Install dependencies**: Install the required Python packages using pip:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

### Data Preprocessing
Run `data_preprocessing.py` to fetch and prepare stock data for analysis. This script provides data summary, checks for missing values, and removes unnecessary columns.

### Exploratory Data Analysis (EDA)
Use `EDA.py` to perform exploratory data analysis. This includes plotting the closing price, calculating daily returns, analyzing volatility, and detecting outliers.

### Time Series Analysis
Use `time_series_analysis.py` to perform time series decomposition and analyze rolling volatility.

### Notebooks Overview

#### 1. `pre-processing.ipynb`
- **Purpose**: Handles data collection, cleaning, and initial processing.
- **Key Steps**:
  - Data import for each asset.
  - Handling missing values, outliers, and data type conversions.
  - Feature engineering, such as creating log returns or calculating moving averages.
- **Outputs**: Cleaned and processed CSV files for TSLA, SPY, and BND, saved in the `data/` directory.

#### 2. `EDA.ipynb`
- **Purpose**: Perform exploratory data analysis to understand trends, seasonality, and overall patterns in the historical price data of each asset.
- **Key Steps**:
  - **Closing Price Analysis**: Visualizes daily closing prices for each asset.
  - **Return Analysis**: Calculates and visualizes daily percentage returns.
  - **Volatility Analysis**: Examines the rolling volatility to assess risk.
  - **Correlation Analysis**: Explores correlations between TSLA, SPY, and BND.
- **Outputs**: Visualizations and summary statistics to help understand asset behavior over time.

#### 3. `time_series_analysis.ipynb`
- **Purpose**: Dives into time series-specific analysis, including decomposition and volatility modeling.
- **Key Steps**:
  - **Decomposition**: Breaks down each time series into trend, seasonality, and residual components.
  - **Volatility Modeling**: Uses rolling windows to capture the dynamic volatility of each asset.
  - **Stationarity Tests**: Conducts tests (e.g., ADF test) to check for stationarity in the time series.
- **Outputs**: Plots for decomposed components, volatility, and test results for stationarity.

#### 4. `time_series_model_and_portfolio_optimization.ipynb`
- **Purpose**: Forecasts future prices for each asset using SARIMA models and performs portfolio optimization based on forecasted returns.
- **Key Steps**:
  - **SARIMA Modeling**: Fits SARIMA models to each asset’s historical prices to forecast future values.
  - **Model Evaluation**: Calculates metrics like Mean Absolute Error (MAE), Root Mean Square Error (RMSE), and Mean Absolute Percentage Error (MAPE) to assess model performance.
  - **Portfolio Optimization**: Uses forecasted returns to construct an optimized portfolio balancing risk and return.
- **Outputs**: Forecasted prices, evaluation metrics, and portfolio weight recommendations.

## Scripts

### data_preprocessing.py
Handles data retrieval and preprocessing, including:
- Fetching historical stock data from Yahoo Finance.
- Displaying basic data info and summaries.
- Identifying missing values.

### EDA.py
Performs EDA tasks like:
- Plotting closing prices and daily percentage changes.
- Analyzing volatility and identifying outliers.

### time_series_analysis.py
Conducts time series analysis, focusing on:
- Decomposing time series data to observe trend and seasonality.
- Analyzing rolling standard deviation for volatility insights.

## Notebooks

`quantitative_analysis.ipynb`: Contains the end-to-end analysis, combining data loading, preprocessing, EDA, and time series decomposition with visualizations.

## Logs

All scripts save log information in the `logs/` folder:
- `info.log`: Logs general information about script execution.
- `error.log`: Logs any errors encountered during execution.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing

Contributions, issues, and feature requests are welcome! Feel free to check out the issues page to get involved.

Happy analyzing!
