import logging
import os
from logging.handlers import RotatingFileHandler
from datetime import datetime
from Src.constants.constants import LOG_FOLDER

log_folder = LOG_FOLDER
os.makedirs(log_folder, exist_ok=True)

custom_logger = logging.getLogger(__name__)
custom_logger.setLevel(logging.DEBUG)

log_file_path = os.path.join(log_folder, f"app_log_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log")
file_handler = RotatingFileHandler(log_file_path, maxBytes=10240, backupCount=5)
file_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s [%(levelname)s] - %(message)s')
file_handler.setFormatter(formatter)

custom_logger.addHandler(file_handler)