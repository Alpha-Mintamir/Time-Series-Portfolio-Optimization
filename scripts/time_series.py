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

def split_data(df):
    try:
        train_size = int(len(df) * 0.8)
        train, test = df[:train_size], df[train_size:]
        logger.info("Data split into train and test sets successfully.")
        return train, test
    except Exception as e:
        logger.error(f"Error splitting data: {e}")
        raise

