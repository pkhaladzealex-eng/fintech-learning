# Import test framework and tools
import sys
import os
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

# Find the main project directory automatically to import selenium_utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from selenium_utils import login_to_site, fill_checkout_form, verify_checkout_result


