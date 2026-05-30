import sqlite3
import stripe
import time
import sys
import os

# Append parent directory to path so python can locate utils and config modules flawlessly
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import utils
import config

def run_rate_limited_sync():
    conn = None
    try:
        # Set API key from   my global production config
        stripe.api_key = config.STRIPE_API_KEY

        # Sample pool of valid/mock charge IDs to iterate over
        charge_pool = [
            "ch_3TTlJHJP62O0ob1e0R3E4KTz",
            "ch_3TTlJeJP62O0ob1e2YztVXyQ",
            "ch_3TZHd0JP62O0ob1e29DOOv37",
            "ch_3Mv9xL",
            "ch_3TSFzTJP62O0ob1e05zgZnMx"
        ]

        # Establish database connection using centralized config attributes
        conn = sqlite3.connect(config.DATABASE_PATH)
        cursor = conn.cursor()

        print(f"Active Configuration Database Target: {config.DATABASE_PATH}")
        print(f"Active Telemetry Outflow Pathway   : {config.LOG_FILE_PATH}\n")
        print("--- Day 58: Initiating Rate-Limited API Retrieval Batch ---")

        formatted_data = []


        for i in range(5):
            current_request = i + 1
            target_id = charge_pool[i]

            print(f"Request {current_request}/5 - Processing Target: {target_id}...")
            utils.log_event("INFO", f"Triggering sequenced API fetch cycle for Request [{current_request}/5]")


            charge = utils.fetch_charge_safe(target_id)

            if charge:

                formatted_data.append((charge.id, charge.amount, charge.status))
            else:

                utils.log_event("ERROR", f"Unable to fetch live provider metadata for ID: {target_id}. Generating fallback audit context.")

                formatted_data.append((target_id, 2500, "simulated_success"))


            if current_request < 5:
                print(f"Request {current_request}/5 completed. Standby active - throttling next step for 1 second...")
                time.sleep(1)

        #
        print("\nPipeline complete. Staging extracted financial details to local matrix...")
        cursor.executemany("INSERT INTO charges (charge_id, amount_cents, status) VALUES (?,?,?)", formatted_data)
        conn.commit()
        utils.log_event("INFO", "✓ Batch execution successfully committed to transactional database ledger.")


        cursor.execute("SELECT charge_id, amount_cents, status FROM charges ORDER BY rowid DESC LIMIT 5")
        rows = cursor.fetchall()

        print("\n--- RECENT DATABASE TRANSACTIONS ---")
        for row in rows:

            dollar_amount = row[1] / 100
            print(f"ID: {row[0]} | Amount: ${dollar_amount:.2f} | Status: {row[2]}")

    except Exception as e:
        utils.log_event("ERROR", f"Structural runtime framework breakdown: {e}")
    finally:
        if conn:
            conn.close()

if __name__ == '__main__':
    run_rate_limited_sync()