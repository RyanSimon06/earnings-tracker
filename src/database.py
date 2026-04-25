import sqlite3 
import logging
from config import DB_NAME
from config import STOCKS

logger = logging.getLogger(__name__)

def create_stocks_table():
    logger.debug("create_stocks_table started")
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS stocks (
                    ticker TEXT PRIMARY KEY,
                    company_name TEXT NOT NULL,
                    sector TEXT NOT NULL
                )
            """)
            conn.commit()
        logger.info("stocks table created successfully")
    except Exception as e:
        logger.exception("failed to create stocks table")

def create_earnings_events_table():
    logger.debug("create_earnings_events_table started")
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS earnings_events (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    ticker TEXT NOT NULL, 
                    earnings_date DATE NOT NULL,
                    actual_eps REAL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (ticker) REFERENCES stocks(ticker)
                )
            """)
            conn.commit()
        logger.info("earnings_events table created successfully")
    except Exception as e:
        logger.exception("failed to create earnings_events table")

def create_price_snapshots_table():
    logger.debug("create_price_snapshots_table started")
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS price_snapshots (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    ticker TEXT NOT NULL,
                    snapshot_date DATE NOT NULL,
                    close_price REAL NOT NULL,
                    volume INTEGER,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (ticker) REFERENCES stocks(ticker)
                )
            """)
            conn.commit()
        logger.info("price_snapshots table created successfully")
    except Exception as e:
        logger.exception("failed to create price_snapshots table")

def create_tables():
    logger.debug("create_tables started")
    create_stocks_table()
    create_earnings_events_table()
    create_price_snapshots_table()
    logger.info("all tables created successfully")

def insert_stock(stock):
    logger.debug("inserting stock: %s", stock)
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT OR IGNORE INTO stocks (ticker, company_name, sector)
                VALUES (?, ?, ?)
            """, stock)
            conn.commit()
        logger.info("stock inserted successfully: %s", stock)
    except Exception as e:
        logger.exception("failed to insert stock: %s", stock)

def insert_earnings_event(earnings_event):
    logger.debug("inserting earnings event: %s", earnings_event)
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT OR IGNORE INTO earnings_events (ticker, earnings_date, actual_eps)
                VALUES (?, ?, ?)
            """, earnings_event)
            conn.commit()
        logger.info("earnings event inserted successfully: %s", earnings_event)
    except Exception as e:
        logger.exception("failed to insert earnings event: %s", earnings_event)

def insert_price_snapshot(snapshot):
    logger.debug("inserting price snapshot: %s", snapshot)
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO price_snapshots (ticker, snapshot_date, close_price, volume)
                VALUES (?, ?, ?, ?)
            """, snapshot)
            conn.commit()
        logger.info("price snapshot inserted successfully: %s", snapshot)
    except Exception as e:
        logger.exception("failed to insert price snapshot: %s", snapshot)

def get_connection():
    logger.debug("creating database connection to %s", DB_NAME)
    try:
        conn = sqlite3.connect(DB_NAME)
        conn.execute("PRAGMA foreign_keys = ON")
        return conn
    except Exception as e:
        logger.exception("failed to connect to database: %s", DB_NAME)
        raise