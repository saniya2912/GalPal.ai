import sqlite3
from datetime import datetime

DB_PATH = "database/galpal.db"

def get_connection():
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    return conn

def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS journal_entries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT NOT NULL,
            content TEXT NOT NULL
        )
    """)
    
    conn.commit()
    conn.close()

def save_journal_entry(content: str):
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute(
        "INSERT INTO journal_entries (timestamp, content) VALUES (?, ?)",
        (datetime.utcnow().isoformat(), content)
    )
    
    conn.commit()
    conn.close()

def get_all_entries():
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM journal_entries ORDER BY id DESC")
    rows = cursor.fetchall()
    
    conn.close()
    return rows
