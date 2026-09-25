# database.py

import sqlite3
from pathlib import Path

from config import DB_PATH


def get_connection():
    db_path = Path(DB_PATH)

    # data folder না থাকলে তৈরি করবে
    db_path.parent.mkdir(parents=True, exist_ok=True)

    conn = sqlite3.connect(db_path)

    conn.row_factory = sqlite3.Row

    return conn


def create_database():
    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS locations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id TEXT NOT NULL,
            route TEXT NOT NULL,
            latitude REAL NOT NULL,
            longitude REAL NOT NULL,
            accuracy REAL,
            speed REAL,
            heading REAL,
            timestamp TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()