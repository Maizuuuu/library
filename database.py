import sqlite3


def create_con():
    return sqlite3.connect("data.db")


def create_tables():
    con = create_con()

    # Задача: id, title, status, user_id
    SQL = """
        CREATE TABLE IF NOT EXISTS task (
            id INTEGER PRIMARY KEY,
            user_id INTEGER,
            title TEXT,
            author TEXT,
            status TEXT,
            added_at TEXT
        )
    """
    con.execute(SQL)