import os

STRIPE_API_KEY = os.environ.get('STRIPE_API_KEY', 'st_test_mock_key_12345')
DATABASE_PATH = '/Users/alexpkhaladze/desktop/fintech-learning/global_data/fintech_main.db'


LOG_FILE_PATH = '/Users/alexpkhaladze/desktop/fintech-learning/api-testing/logs/payment_logs.txt'

WEBHOOK_TIMEOUT = 30