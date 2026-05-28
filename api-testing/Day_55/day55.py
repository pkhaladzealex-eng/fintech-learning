import sys
import os

# Rise up to access utils from the api-testing root area
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import utils

print("--- Day 55: Updated to use Centralized Utils Layer ---")

charge_id = "ch_3Mv9xL"
charge_amount = 2500
charge_status = "succeeded"

# Replace the old local try-except block with a single reusable utils call
utils.validate_charge(charge_id, charge_amount, charge_status)
