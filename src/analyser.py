from datetime import timedelta, datetime
from fetcher import fetch_price_history
from config import PRICE_MOVE_THRESHOLD

def get_earnings_window(earnings_date):
    start_date = earnings_date - timedelta(days=5)
    end_date = earnings_date + timedelta(days=5)
    return (start_date, end_date)

def calculate_price_move(ticker, earnings_date):
    start_date, end_date = get_earnings_window(earnings_date)
    price_history = fetch_price_history(ticker, start_date, end_date)
    price_before = price_history.iloc[0]["Close"]
    price_after = price_history.iloc[-1]["Close"]
    price_move = ((price_after - price_before) / price_before) * 100
    return float(price_move)

def is_anomalous(price_move):
    return abs(price_move) > PRICE_MOVE_THRESHOLD
