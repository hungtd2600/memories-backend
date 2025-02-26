import sqlite3
import os
from typing import List, Dict, Optional, Tuple

class DatabaseManager:
    def __init__(self, db_path: str = 'database/memories.db'):
        os.makedirs(os.path.dirname(db_path), exist_ok=True)
        self.db_path = db_path

    def get_connection(self) -> sqlite3.Connection:
        return sqlite3.connect(self.db_path)

    def init_db(self) -> None:
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT UNIQUE NOT NULL,
                    password TEXT NOT NULL
                )
            ''')
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS memories (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    description TEXT
                )
            ''')
            conn.commit()

    def get_user(self, username: str) -> Optional[Tuple[str, str]]:
        query = "SELECT username, password FROM users WHERE username = ?"
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(query, (username,))
            return cursor.fetchone()

    def get_all_memories(self) -> List[Dict[str, any]]:
        query = "SELECT id, name, description FROM memories"
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(query)
            return [{"id": m[0], "name": m[1], "description": m[2]} for m in cursor.fetchall()]

    def add_user(self, username: str, password: str) -> bool:
        try:
            query = "INSERT INTO users (username, password) VALUES (?, ?)"
            with self.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(query, (username, password))
                conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False

if __name__ == "__main__":
    db = DatabaseManager()
    db.init_db()