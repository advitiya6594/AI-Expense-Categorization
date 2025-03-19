import sqlite3

DATABASE = "transactions.db"

def init_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            description TEXT,
            amount REAL,
            date TEXT,
            category TEXT
        )
    """)
    conn.commit()
    conn.close()

def add_transaction(transaction):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO transactions (description, amount, date, category) VALUES (?, ?, ?, ?)",
                   (transaction.description, transaction.amount, transaction.date, "Uncategorized"))
    conn.commit()
    conn.close()

def get_transactions():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM transactions")
    transactions = cursor.fetchall()
    conn.close()
    return transactions
