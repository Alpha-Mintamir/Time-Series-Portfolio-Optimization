import pandas as pd
import matplotlib.pyplot as plt
import logging
import os
from statsmodels.tsa.seasonal import seasonal_decompose

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



class TimeSeriesAnalysis:
    def __init__(self, df):
        self.df = df.copy()
        if 'Date' in self.df.columns:
            self.df['Date'] = pd.to_datetime(self.df['Date'])
            self.df.set_index('Date', inplace=True)
        logger.info("TimeSeriesAnalysis class initialized with DataFrame.")

    def decompose_time_series(self, freq='D'):
        """Decomposes the time series into trend, seasonal, and residual components."""
        logger.info("Decomposing time series into trend, seasonal, and residual components.")
        decomposition = seasonal_decompose(self.df['Close'], model='additive', period=freq)
        
        print("Displaying the observed time series data.")
        plt.figure(figsize=(12, 8))
        plt.subplot(411)
        plt.plot(decomposition.observed)
        plt.title('Observed')
        
        print("Displaying the trend component of the time series.")
        plt.subplot(412)
        plt.plot(decomposition.trend)
        plt.title('Trend')
        
        print("Displaying the seasonal component of the time series.")
        plt.subplot(413)
        plt.plot(decomposition.seasonal)
        plt.title('Seasonal')
        
        print("Displaying the residual component of the time series.")
        plt.subplot(414)
        plt.plot(decomposition.resid)
        plt.title('Residual')
        
        plt.tight_layout()
        plt.show()

    def plot_rolling_volatility(self, window=20):
        """Calculates and plots rolling standard deviation to analyze volatility."""
        logger.info(f"Plotting rolling volatility with a {window}-day window.")
        self.df['Rolling_Std'] = self.df['Close'].rolling(window).std()

        print(f"Displaying the {window}-day rolling volatility.")
        plt.figure(figsize=(12, 6))
        plt.plot(self.df.index, self.df['Rolling_Std'], label=f'{window}-Day Rolling Volatility', color='red')
        plt.title('Rolling Volatility')
        plt.xlabel('Date')
        plt.ylabel('Volatility (Std Dev)')
        plt.legend()
        plt.show()