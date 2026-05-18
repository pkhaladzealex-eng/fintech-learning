import json

charge_succeeded_webhook = """
{
  "type": "charge.succeeded",
  "data": {
    "object": {
      "id": "ch_3MTAuBClCI6A",
      "amount": 2000,
      "currency": "usd",
      "status": "succeeded"
    }
  }
} """
charge_refunded_webhook = """
{
  "type": "charge.refunded",
  "data": {
    "object": {
      "id": "ch_3MTAuBClCI6A",
      "amount_refunded": 2000,
      "currency": "usd",
      "status": "refunded"
    }
  }
} """

customer_created_webhook = """
{
  "type": "customer.created",
  "data": {
    "object": {
      "id": "cus_NOb7H789",
      "email": "alex.pkhaladze@example.com"
    }
  }
} """

def process_webhook(webhook_raw_json):
    event = json.loads(webhook_raw_json) # parsing data
    event_type= event["type"] # Extracting the specific webhook event type
    stripe_obj = event["data"]["object"] # this is the main data object
    if event_type == "charge.succeeded":
        charge_id = stripe_obj["id"]
        amount = stripe_obj["amount"]
        currency = stripe_obj["currency"]
        status = stripe_obj["status"]
        print(f'Charge Succeeded! ID: {charge_id}, Amount: {amount / 100 :.2f} {currency.upper()} , Status: {status}')

    elif event_type == "charge.refunded":
        charge_id = stripe_obj["id"]
        amount = stripe_obj["amount_refunded"]
        currency = stripe_obj["currency"]
        status = stripe_obj["status"]
        print(f'Successfully Refunded: ID: {charge_id}, Amount: {amount / 100 :.2f} {currency.upper()},  Status: {status}')

    elif event_type == "customer.created":
        customer_id = stripe_obj["id"]
        email = stripe_obj["email"]
        print(f'Customer Created: ID: {customer_id}, Email: {email}')
    else:
        print('Unknown Event Type')

process_webhook(charge_succeeded_webhook)
process_webhook(charge_refunded_webhook)
process_webhook(customer_created_webhook)




