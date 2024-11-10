import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import logging
import os

# Configure logging
log_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'logs')

if not os.path.exists(log_dir):
    os.makedirs(log_dir)

log_file_info = os.path.join(log_dir, 'info.log')
log_file_error = os.path.join(log_dir, 'error.log')

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
info_handler = logging.FileHandler(log_file_info)
error_handler = logging.FileHandler(log_file_error)

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
info_handler.setFormatter(formatter)
error_handler.setFormatter(formatter)

logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(info_handler)
logger.addHandler(error_handler)


class StockEDA:
    def __init__(self, df):
        self.df = df.copy()
        if 'Date' in self.df.columns:
            self.df['Date'] = pd.to_datetime(self.df['Date'])
            self.df.set_index('Date', inplace=True)
        logger.info("StockEDA class initialized with DataFrame.")

    def plot_closing_price(self):
        """Plots the closing price over time to visualize trends and patterns."""
        logger.info("Plotting closing price over time.")
        plt.figure(figsize=(12, 6))
        plt.plot(self.df.index, self.df['Close'], label='Closing Price')
        plt.title('Closing Price Over Time')
        plt.xlabel('Date')
        plt.ylabel('Closing Price')
        plt.legend()
        plt.show()

    def plot_daily_percentage_change(self):
        """Calculates and plots daily percentage change to observe volatility."""
        logger.info("Calculating and plotting daily percentage change.")
        self.df['Daily_Return'] = self.df['Close'].pct_change()
        plt.figure(figsize=(12, 6))
        plt.plot(self.df.index, self.df['Daily_Return'], color='orange', label='Daily % Change')
        plt.title('Daily Percentage Change')
        plt.xlabel('Date')
        plt.ylabel('Percentage Change')
        plt.legend()
        plt.show()

    def analyze_volatility(self, window=20):
        """Analyzes volatility using rolling mean and standard deviation for a given window."""
        logger.info(f"Analyzing volatility with a {window}-day rolling window.")
        self.df['Rolling_Mean'] = self.df['Close'].rolling(window).mean()
        self.df['Rolling_Std'] = self.df['Close'].rolling(window).std()

        plt.figure(figsize=(12, 6))
        plt.plot(self.df.index, self.df['Close'], label='Closing Price')
        plt.plot(self.df.index, self.df['Rolling_Mean'], label=f'{window}-Day Rolling Mean', color='green')
        plt.fill_between(
            self.df.index,
            self.df['Rolling_Mean'] - self.df['Rolling_Std'],
            self.df['Rolling_Mean'] + self.df['Rolling_Std'],
            color='gray', alpha=0.3, label='Rolling Std Dev'
        )
        plt.title('Volatility Analysis with Rolling Mean and Std Dev')
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.legend()
        plt.show()

    def detect_outliers(self):
        """Detects outliers based on Z-scores of the closing price."""
        logger.info("Detecting outliers based on Z-score.")
        self.df['Z_Score'] = (self.df['Close'] - self.df['Close'].mean()) / self.df['Close'].std()
        outliers = self.df[abs(self.df['Z_Score']) > 3]
        logger.info(f"Found {len(outliers)} outliers.")
        return outliers

    def analyze_extreme_returns(self, threshold=0.05):
        """Identifies days with extreme returns based on a threshold percentage change."""
        logger.info(f"Analyzing extreme returns with a threshold of {threshold}.")
        self.df['Daily_Return'] = self.df['Close'].pct_change()
        extreme_returns = self.df[
            (self.df['Daily_Return'] > threshold) | (self.df['Daily_Return'] < -threshold)
        ]
        logger.info(f"Found {len(extreme_returns)} days with extreme returns.")
        return extreme_returns


