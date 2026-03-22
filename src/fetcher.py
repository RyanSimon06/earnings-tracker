import yfinance as yf

def fetch_earnings_dates(ticker):
    stock = yf.Ticker(ticker)
    return stock.earnings_dates

def fetch_price_history(ticker, start_date, end_date):
    stock = yf.Ticker(ticker)
    history = stock.history(start=start_date, end=end_date)
    return history[["Close", "Volume"]]
