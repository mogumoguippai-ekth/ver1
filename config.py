import sqlite3
import os


class Database:
    def __init__(self, db_path="db.sqlite"):
        self.db_path = db_path

    def get_connection(self):
        """データベース接続を取得"""
        return sqlite3.connect(self.db_path)

    def init_db(self):
        """データベースとテーブルを初期化"""
        conn = self.get_connection()
        cursor = conn.cursor()

        # ユーザーテーブル作成
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id VARCHAR(50) UNIQUE NOT NULL,
                email VARCHAR(100) UNIQUE NOT NULL,
                password VARCHAR(255) NOT NULL,
                name VARCHAR(100) NOT NULL,
                furigana VARCHAR(100),
                nickname VARCHAR(50),
                gender VARCHAR(10) CHECK(gender IN ('男', '女', 'その他')),
                birth_date DATE,
                family_id1 INTEGER,
                family_id2 INTEGER,
                family_id3 INTEGER,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """
        )

        conn.commit()
        conn.close()

    def create_user(self, user_data):
        """新しいユーザーを作成"""
        conn = self.get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO users (user_id, email, password, name, furigana, nickname, gender, birth_date, family_id1, family_id2, family_id3)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                user_data.get("user_id"),
                user_data.get("email"),
                user_data.get("password"),
                user_data.get("name"),
                user_data.get("furigana"),
                user_data.get("nickname"),
                user_data.get("gender"),
                user_data.get("birth_date"),
                user_data.get("family_id1"),
                user_data.get("family_id2"),
                user_data.get("family_id3"),
            ),
        )

        user_id = cursor.lastrowid
        conn.commit()
        conn.close()
        return user_id

    def get_user_by_id(self, user_id):
        """ユーザーIDでユーザー情報を取得"""
        conn = self.get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM users WHERE user_id = ?", (user_id,))
        user = cursor.fetchone()
        conn.close()
        return user

    def get_user_by_email(self, email):
        """メールアドレスでユーザー情報を取得"""
        conn = self.get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
        user = cursor.fetchone()
        conn.close()
        return user

    def authenticate_user(self, user_id, password):
        """ユーザー認証"""
        conn = self.get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM users WHERE user_id = ? AND password = ?", (user_id, password))
        user = cursor.fetchone()
        conn.close()
        return user


# データベースインスタンス
db = Database()
