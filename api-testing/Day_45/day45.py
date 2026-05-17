import sqlite3


db_path = '/Users/alexpkhaladze/desktop/fintech-learning/global_data/fintech_main.db'
conn = sqlite3.connect(db_path)
cursor = conn.cursor()


def generate_financial_report():
    print("--- Day 45: Advanced Financial Report (Charges vs Refunds) ---")


    query = """
        SELECT 
            c.name,
            c.email,
            COALESCE(SUM(ch.amount_cents), 0) AS total_charges_cents,
            COALESCE(SUM(r.amount), 0) AS total_refunds_cents
        FROM customers c
        LEFT JOIN charges ch ON c.stripe_customer_id = ch.customer_id
        LEFT JOIN refunds r ON ch.charge_id = r.charge_id
        WHERE c.stripe_customer_id IN ('cus_UW2gvmQ1CMruOG', 'cus_UW2gFZSxugU9M8', 'cus_UW2gvnbOAtKNCJ')
        GROUP BY c.id;
    """

    cursor.execute(query)
    rows = cursor.fetchall()

    company_total_revenue = 0.0


    print(f"{'Customer Name':<18} | {'Email':<20} | {'Total Charges':<13} | {'Total Refunds':<13} | {'Net Amount'}")
    print("-" * 85)

    for row in rows:
        name = row[0]
        email = row[1]


        charges_usd = row[2] / 100
        refunds_usd = row[3] / 100
        net_usd = charges_usd - refunds_usd


        company_total_revenue += net_usd

        print(f"{name:<18} | {email:<20} | ${charges_usd:<12.2f} | ${refunds_usd:<12.2f} | ${net_usd:.2f}")

    print("-" * 85)
    print(f"Total Company Net Revenue: ${company_total_revenue:.2f}\n")


if __name__ == "__main__":
    generate_financial_report()
    conn.close()