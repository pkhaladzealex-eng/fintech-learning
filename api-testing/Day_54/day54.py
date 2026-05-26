import config
api_status = "Present" if config.STRIPE_API_KEY else "Missing"

print(f"Using config: {config.DATABASE_PATH}, {config.LOG_FILE_PATH}, API Key Status: {api_status}")

