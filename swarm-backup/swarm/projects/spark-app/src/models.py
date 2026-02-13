"""SQLite models for Spark App using sqlite3 (no ORM)."""

import sqlite3
from contextlib import contextmanager
from typing import Any, Dict, Iterable, Tuple, List

DB_PATH = "sqlite:///spark.db"
# The path will be relative to the project root; for now just use a file
# In a real app you might use a config.
DB_FILE = "spark.db"

@contextmanager
def get_conn() -> sqlite3.Connection:
    """Context manager for SQLite connections.
    Use as:
        with get_conn() as conn:
            cur = conn.cursor()
            cur.execute(...)
            conn.commit()
    """
    conn = sqlite3.connect(DB_FILE)
    try:
        yield conn
    finally:
        conn.close()

# Table creation statements
TABLES = {
    "agents": """
        CREATE TABLE IF NOT EXISTS agents (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            model TEXT NOT NULL,
            workspace TEXT NOT NULL,
            status TEXT NOT NULL,
            last_active TEXT
        );
    """,
    "tasks": """
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            agent_id INTEGER NOT NULL,
            description TEXT NOT NULL,
            status TEXT NOT NULL,
            created TEXT NOT NULL,
            completed TEXT,
            FOREIGN KEY (agent_id) REFERENCES agents(id)
        );
    """,
    "findings": """
        CREATE TABLE IF NOT EXISTS findings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            agent_id INTEGER NOT NULL,
            title TEXT NOT NULL,
            path TEXT NOT NULL,
            created TEXT NOT NULL,
            tags TEXT,
            FOREIGN KEY (agent_id) REFERENCES agents(id)
        );
    """,
    "training_data": """
        CREATE TABLE IF NOT EXISTS training_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            agent_id INTEGER NOT NULL,
            input TEXT NOT NULL,
            output TEXT NOT NULL,
            tools_used TEXT,
            success INTEGER,
            quality REAL,
            created TEXT NOT NULL,
            FOREIGN KEY (agent_id) REFERENCES agents(id)
        );
    """
}


def create_tables() -> None:
    """Create all tables in the SQLite database."""
    with get_conn() as conn:
        cur = conn.cursor()
        for stmt in TABLES.values():
            cur.execute(stmt)
        conn.commit()

# Example CRUD helpers

def insert_agent(name: str, model: str, workspace: str, status: str, last_active: str | None = None) -> int:
    """Insert a new agent and return its id."""
    with get_conn() as conn:
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO agents (name, model, workspace, status, last_active) VALUES (?, ?, ?, ?, ?)",
            (name, model, workspace, status, last_active),
        )
        conn.commit()
        return cur.lastrowid

# Additional helpers can be added as needed

if __name__ == "__main__":
    # Simple sanity check: create tables
    create_tables()
    print("Tables created.")
