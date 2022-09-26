import os
from selenium import webdriver

URL = "https://www.booking.com/"
DRIVER_PATH = os.getenv('DRIVER_PATH')
BRAVE_PATH = os.getenv('BRAVE_PATH')
WAIT_TIME = 4  # time to wait for the implicitly_wait method
DEFAULT_AMOUNT_OF_ADULTS = 2

# Brave configuration
brave_path = os.getenv('BRAVE_PATH')
OPTION = webdriver.ChromeOptions() # DRIVER_PATH is a env variable
OPTION.binary_location = brave_path


#  CLASS_NAMES_DICT={'5stars': 'class="bbdb949247"', '4stars': 'class="bbdb949247"'}

API_KEY = os.getenv('API_KEY')
GROUP_CHAT_ID = os.getenv('CHAT_ID')