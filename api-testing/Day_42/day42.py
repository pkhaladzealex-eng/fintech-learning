import os
import stripe
import sqlite3

# 1. Stripe Configuration
stripe.api_key = os.environ.get('STRIPE_API_KEY')

# 2. Database Connection
db_path = '/Users/alexpkhaladze/desktop/fintech-learning/global_data/fintech_main.db'
conn = sqlite3.connect(db_path)
cursor = conn.cursor()


def create_stripe_customers():
    print("--- Creating New Customers via Stripe API ---")

    new_customers = [
        {"name": "Alice Wonderland", "email": "alice@example.com"},
        {"name": "Bob Builder", "email": "bob@example.com"},
        {"name": "Charlie Brown", "email": "charlie@example.com"}
    ]

    for person in new_customers:
        try:
            # Create in Stripe
            customer = stripe.Customer.create(
                name=person['name'],
                email=person['email'],
                description="Day 42 Automation Test"
            )

            # Insert into your existing database schema
            # We'll leave payment_method as 'API Generated' for now
            cursor.execute("""
                INSERT INTO customers (name, email, payment_method, stripe_customer_id)
                VALUES (?, ?, ?, ?)
            """, (customer.name, customer.email, "API Generated", customer.id))

            print(f"✅ Created: {customer.name} ({customer.id})")

        except Exception as e:
            print(f" Error creating customer: {e}")

    conn.commit()


def list_all_customers():
    print("\n---  Current Customer List (Database) ---")
    cursor.execute("SELECT id, name, email, stripe_customer_id FROM customers ORDER BY id DESC LIMIT 10")
    rows = cursor.fetchall()

    print(f"{'ID':<4} | {'Name':<20} | {'Email':<25} | {'Stripe ID'}")
    print("-" * 75)
    for row in rows:
        print(f"{row[0]:<4} | {row[1]:<20} | {row[2]:<25} | {row[3]}")


if __name__ == "__main__":
    try:
        create_stripe_customers()
        list_all_customers()
    except Exception as e:
        print(f" Script Error: {e}")
    finally:
        conn.close()