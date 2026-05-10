import sqlite3

conn = sqlite3.connect('/Users/alexpkhaladze/desktop/fintech-learning/global_data/fintech_main.db')
cursor = conn.cursor()

cursor.execute("""SELECT 
    c.charge_id, 
    c.amount_cents, 
    r.amount AS refund_amount,
    (c.amount_cents - IFNULL(r.amount, 0)) AS net_amount
FROM charges c
LEFT JOIN refunds r ON c.charge_id = r.charge_id""")


rows = cursor.fetchall()
total_net_revenue = 0


print("--- Charges Without Refunds ---")
for row in rows:

    total_net_revenue += row[3]


    if row[2] is None:
        print(f"Charge ID: {row[0]} has no refunds")


print("\n--- Summary Report ---")
print(f"Total Net Revenue: {total_net_revenue / 100:.2f} USD")