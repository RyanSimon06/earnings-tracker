import sqlite3 

def create_stocks_table():
    conn = sqlite3.connect("stocks.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE stocks (ticker TEXT PRIMARY KEY, company_name TEXT NOT NULL, sector TEXT NOT NULL)")
    conn.commit()

create_stocks_table()
print(stocks)