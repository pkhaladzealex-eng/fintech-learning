charge_id = "ch_3Mv9xL"
charge_amount = 2500
charge_status = "succeeded"

try:
    assert charge_id is not None, "Charge ID missing"
    assert charge_amount > 0, "Amount must be positive"
    assert charge_status in ["succeeded", "failed"], "Invalid charge status"
    print("All tests passed")

except AssertionError as e:
    print(f'Test Failed: {e}')
