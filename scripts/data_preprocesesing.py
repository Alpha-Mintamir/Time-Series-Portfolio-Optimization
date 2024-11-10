import yfinance as yahooFinance
import pandas as pd
import logging
import os, io


# Logging configuration
log_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'logs')

if not os.path.exists(log_dir):
    os.makedirs(log_dir)

log_file_info = os.path.join(log_dir, 'info.log')
log_file_error = os.path.join(log_dir, 'error.log')

info_handler = logging.FileHandler(log_file_info)
info_handler.setLevel(logging.INFO)

error_handler = logging.FileHandler(log_file_error)
error_handler.setLevel(logging.ERROR)

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
info_handler.setFormatter(formatter)
error_handler.setFormatter(formatter)

logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(info_handler)
logger.addHandler(error_handler)


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


def get_stock_data(stock_symbol, start_date="2015-01-01", end_date="2024-12-31"):
    """
    Fetches historical data for a stock symbol.

    Args:
    - stock_symbol (str): Stock symbol to fetch data for.
    - start_date (str): Start date for data.
    - end_date (str): End date for data.

    Returns:
    - pandas.DataFrame: Historical stock data.
    """
    try:
        stock_data = yahooFinance.Ticker(stock_symbol).history(start=start_date, end=end_date)
        stock_data = stock_data.drop(columns=['Dividends', 'Stock Splits'])
        return stock_data

    except Exception as e:
        logger.error(f"Failed to fetch data for {stock_symbol}: {e}")
        return None
    
def data_understanding(df):
    """
    Understand the data by logging and printing various summaries.
    """
    logger.info(f"Data Shape: {df.shape}")
    print(f"Data Shape: {df.shape}")

    logger.info("Data Head:")
    logger.info(f"\n{df.head()}")
    print("Data Head:")
    print(df.head())

    logger.info("Data Description:")
    logger.info(f"\n{df.describe()}")
    print("Data Description:")
    print(df.describe())

    buffer = io.StringIO()
    df.info(buf=buffer)
    info = buffer.getvalue()
    logger.info("Data Info:")
    logger.info(f"\n{info}")
    print("Data Info:")
    print(info)

    logger.info(f"Data Columns: {df.columns.tolist()}")
    print(f"Data Columns: {df.columns.tolist()}")

    null_values = df.isnull().sum()
    logger.info("Data Null Values:")
    logger.info(f"\n{null_values}")
    print("Data Null Values:")
    print(null_values)



def missing_values_table(df):
    mis_val = df.isnull().sum()
    mis_val_percent = 100 * df.isnull().sum() / len(df)
    mis_val_data_types = df.dtypes
    mis_val_table = pd.concat([mis_val, mis_val_percent], axis=1)
    mis_val_table_ren_columns = mis_val_table.rename(
        columns={0: 'Missing Values', 1: '% of Total Values', 2: 'Otype'})
    mis_val_table_ren_columns = mis_val_table_ren_columns[
        mis_val_table_ren_columns.iloc[:,1] != 0].sort_values(
        '% of Total Values', ascending=False).round(1)
    logger.info("Your selected dataframe has %d columns.", df.shape[1])
    logger.info("There are %d columns that have missing values.", mis_val_table_ren_columns.shape[0])
    return mis_val_table_ren_columns
