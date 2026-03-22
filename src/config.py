from dotenv import load_dotenv
import os

load_dotenv()

DB_NAME = os.getenv("DB_NAME","earnings_tracker.db")
PRICE_MOVE_THRESHOLD = float(os.getenv("PRICE_MOVE_THRESHOLD", 0.05))
