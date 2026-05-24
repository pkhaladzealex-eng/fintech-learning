import sqlite3

db_path = '/Users/alexpkhaladze/desktop/fintech-learning/global_data/fintech_main.db'
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

def validate_and_process_finances():
    query = """
    SELECT
        c.stripe_customer_id,
        c.name,
        ch.charge_id,
        ch.amount_cents,
        r.amount
    FROM customers c
    LEFT JOIN charges ch ON c.stripe_customer_id = ch.customer_id
    LEFT JOIN refunds r ON ch.charge_id = r.charge_id
     WHERE c.stripe_customer_id IN ('cus_UW2gvmQ1CMruOG', 'cus_UW2gFZSxugU9M8', 'cus_UW2gvnbOAtKNCJ')
     """
    cursor.execute(query)
    rows = cursor.fetchall()
    company_total_revenue = 0.0
    for row in rows:

        cus_id = row[0]
        name = row[1]
        charge_id = row[2]
        charge_amount = row[3]  if row[3] else 0
        refund_amount = row[4] if row[4] else 0

        has_customer_id = True if cus_id else False
        is_charge_positive = True if charge_amount > 0 else False
        is_refund_valid = True if (refund_amount <= charge_amount) else False
        print(
            f"Customer: {name: <18} | Valid ID: {has_customer_id} | Positive Charge: {is_charge_positive} | Valid Refund: {is_refund_valid}")
        if has_customer_id and is_charge_positive and is_refund_valid:
            charges_usd = charge_amount / 100
            refunds_usd = refund_amount / 100
            net_usd = charges_usd - refunds_usd
            company_total_revenue += net_usd
        else:
            print(f"   ↳ [Validation Failed] Skipping record for {name}")
    print(f'Total Revenue: {company_total_revenue:.2f}')
    conn.close()

validate_and_process_finances()




