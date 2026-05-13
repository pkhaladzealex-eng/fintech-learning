import os
import stripe
import sqlite3

# 1. Stripe Configuration
stripe.api_key = os.environ.get('STRIPE_API_KEY')

# 2. Database Connection
db_path = '/Users/alexpkhaladze/desktop/fintech-learning/global_data/fintech_main.db'
conn = sqlite3.connect(db_path)
cursor = conn.cursor()


def update_schema():
    """Ensure the charges table has a card_brand column."""
    cursor.execute("PRAGMA table_info(charges)")
    columns = [column[1] for column in cursor.fetchall()]
    if 'card_brand' not in columns:
        print("🔧 Updating database schema: Adding 'card_brand' column...")
        cursor.execute("ALTER TABLE charges ADD COLUMN card_brand TEXT")
        conn.commit()


def create_card_charges():
    # Test cards from Stripe documentation
    test_cards = [
        {"brand": "Visa", "source": "tok_visa", "amount": 1200},
        {"brand": "Mastercard", "source": "tok_mastercard", "amount": 2500},
        {"brand": "Amex", "source": "tok_amex", "amount": 4500}
    ]

    print("--- Creating Charges for Different Card Types ---")

    for card in test_cards:
        try:
            # Create charge in Stripe
            charge = stripe.Charge.create(
                amount=card['amount'],
                currency="usd",
                source=card['source'],
                description=f"Day 41 Test - {card['brand']}"
            )

            # Insert into database with card brand
            cursor.execute("""
                INSERT INTO charges (charge_id, amount_cents, status, card_brand)
                VALUES (?, ?, ?, ?)
            """, (charge.id, charge.amount, charge.status, card['brand']))

            print(f" Success: {card['brand']} charge created.")

        except Exception as e:
            print(f" Error creating {card['brand']} charge: {e}")

    conn.commit()


def show_card_statistics():
    print("\n--- Charges Grouped by Card Type ---")
    # SQL uses NULL instead of None
    cursor.execute("""
        SELECT card_brand, COUNT(*) 
        FROM charges 
        WHERE card_brand IS NOT NULL
        GROUP BY card_brand
    """)
    stats = cursor.fetchall()

    if not stats:
        print("No grouped data found.")

    for brand, count in stats:
        print(f" {brand}: {count} charge(s)")


if __name__ == "__main__":
    try:
        update_schema()
        create_card_charges()
        show_card_statistics()
    except Exception as e:
        print(f" Error: {e}")
    finally:
        conn.close()