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
                user_type VARCHAR(20) DEFAULT 'self' CHECK(user_type IN ('self', 'family')),
                name VARCHAR(100),
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

        # プロフィールテーブル作成
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS profiles (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id VARCHAR(50) NOT NULL,
                home VARCHAR(100),
                spouse TEXT,
                children_living TEXT,
                children_separate TEXT,
                treated_illness TEXT,
                under_treatment TEXT,
                medical_facilities TEXT,
                most_relied_family TEXT,
                trusted_neighbor TEXT,
                consulted_friend TEXT,
                money_sources TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users (user_id)
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
            INSERT INTO users (user_id, email, password, user_type, name, furigana, nickname, gender, birth_date, family_id1, family_id2, family_id3)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                user_data.get("user_id"),
                user_data.get("email"),
                user_data.get("password"),
                user_data.get("user_type", "self"),
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

    def get_profile_by_user_id(self, user_id):
        """ユーザーIDでプロフィール情報を取得"""
        conn = self.get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM profiles WHERE user_id = ?", (user_id,))
        profile = cursor.fetchone()
        conn.close()
        return profile

    def create_or_update_profile(self, user_id, profile_data):
        """プロフィール情報を作成または更新"""
        conn = self.get_connection()
        cursor = conn.cursor()

        # 既存のプロフィールがあるかチェック
        cursor.execute("SELECT id FROM profiles WHERE user_id = ?", (user_id,))
        existing_profile = cursor.fetchone()

        if existing_profile:
            # 更新
            cursor.execute(
                """
                UPDATE profiles 
                SET home = ?, spouse = ?, children_living = ?, children_separate = ?,
                    treated_illness = ?, under_treatment = ?, medical_facilities = ?,
                    most_relied_family = ?, trusted_neighbor = ?, consulted_friend = ?,
                    money_sources = ?, updated_at = CURRENT_TIMESTAMP
                WHERE user_id = ?
                """,
                (
                    profile_data.get("home"),
                    profile_data.get("spouse"),
                    profile_data.get("children_living"),
                    profile_data.get("children_separate"),
                    profile_data.get("treated_illness"),
                    profile_data.get("under_treatment"),
                    profile_data.get("medical_facilities"),
                    profile_data.get("most_relied_family"),
                    profile_data.get("trusted_neighbor"),
                    profile_data.get("consulted_friend"),
                    profile_data.get("money_sources"),
                    user_id
                )
            )
        else:
            # 新規作成
            cursor.execute(
                """
                INSERT INTO profiles (user_id, home, spouse, children_living, children_separate,
                                    treated_illness, under_treatment, medical_facilities,
                                    most_relied_family, trusted_neighbor, consulted_friend, money_sources)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    user_id,
                    profile_data.get("home"),
                    profile_data.get("spouse"),
                    profile_data.get("children_living"),
                    profile_data.get("children_separate"),
                    profile_data.get("treated_illness"),
                    profile_data.get("under_treatment"),
                    profile_data.get("medical_facilities"),
                    profile_data.get("most_relied_family"),
                    profile_data.get("trusted_neighbor"),
                    profile_data.get("consulted_friend"),
                    profile_data.get("money_sources")
                )
            )

        conn.commit()
        conn.close()


# データベースインスタンス
db = Database()
