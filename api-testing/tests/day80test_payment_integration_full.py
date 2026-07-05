import pytest
import sqlite3
import stripe
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from selenium_utils import (
    login_to_site,
    add_products_to_cart,
    navigate_to_checkout,
    fill_checkout_fields,
    submit_checkout_form,
    complete_checkout
)

import config
import utils
stripe.api_key = os.environ.get("STRIPE_SECRET_KEY")
