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

        # IWLMテーブル作成
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS iwlm (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id VARCHAR(50) NOT NULL,
                meal_frequency TEXT,
                morning_meal_type TEXT,
                lunch_meal_type TEXT,
                dinner_meal_type TEXT,
                snac TEXT,
                habits_alc_smoke TEXT,
                wakeup_time TEXT,
                bedtime TEXT,
                daily_chores TEXT,
                free_times TEXT,
                people_met TEXT,
                toilet_style TEXT,
                bathing_habits TEXT,
                grooming_habits TEXT,
                haircut_salon TEXT,
                favorite_color TEXT,
                favorite_clothing TEXT,
                favorite_footwear TEXT,
                favorite_music TEXT,
                favorite_tv_radio TEXT,
                leisure_activities TEXT,
                favorite_place TEXT,
                job_status TEXT,
                interests TEXT,
                strengths_and_weaknesses TEXT,
                characteristics TEXT,
                others TEXT,
                keep_doing TEXT,
                keep_doing_other TEXT,
                future_activities TEXT,
                future_activities_other TEXT,
                residence_type TEXT,
                residence_type_other TEXT,
                anxiety_and_sadness TEXT,
                anxiety_and_sadness_other TEXT,
                areas_of_support TEXT,
                areas_of_support_other TEXT,
                future_care_plan TEXT,
                future_care_plan_other TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users (user_id)
            )
        """
        )

        # diaryテーブル作成
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS diary (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id VARCHAR(50) NOT NULL,
                date DATE NOT NULL,
                title VARCHAR(100),
                content TEXT,
                photo_path VARCHAR(255),
                thumbnail_path VARCHAR(255),
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users (user_id),
                UNIQUE(user_id, date)
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
                    user_id,
                ),
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
                    profile_data.get("money_sources"),
                ),
            )

        conn.commit()
        conn.close()

    def get_iwlm_by_user_id(self, user_id):
        """ユーザーIDでIWLM情報を取得"""
        conn = self.get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM iwlm WHERE user_id = ?", (user_id,))
        iwlm = cursor.fetchone()
        conn.close()
        return iwlm

    def create_or_update_iwlm(self, user_id, iwlm_data):
        """IWLM情報を作成または更新"""
        conn = self.get_connection()
        cursor = conn.cursor()

        # 既存のIWLMレコードがあるかチェック
        cursor.execute("SELECT id FROM iwlm WHERE user_id = ?", (user_id,))
        existing_iwlm = cursor.fetchone()

        if existing_iwlm:
            # 更新
            cursor.execute(
                """
                UPDATE iwlm 
                SET meal_frequency = ?, morning_meal_type = ?, lunch_meal_type = ?, dinner_meal_type = ?,
                    snac = ?, habits_alc_smoke = ?, wakeup_time = ?, bedtime = ?, daily_chores = ?,
                    free_times = ?, people_met = ?, toilet_style = ?, bathing_habits = ?,
                    grooming_habits = ?, haircut_salon = ?, favorite_color = ?, favorite_clothing = ?,
                    favorite_footwear = ?, favorite_music = ?, favorite_tv_radio = ?,
                    leisure_activities = ?, favorite_place = ?, job_status = ?, interests = ?,
                    strengths_and_weaknesses = ?, characteristics = ?, others = ?, keep_doing = ?,
                    keep_doing_other = ?, future_activities = ?, future_activities_other = ?,
                    residence_type = ?, residence_type_other = ?, anxiety_and_sadness = ?,
                    anxiety_and_sadness_other = ?, areas_of_support = ?, areas_of_support_other = ?,
                    future_care_plan = ?, future_care_plan_other = ?, updated_at = CURRENT_TIMESTAMP
                WHERE user_id = ?
                """,
                (
                    iwlm_data.get("meal_frequency"),
                    iwlm_data.get("morning_meal_type"),
                    iwlm_data.get("lunch_meal_type"),
                    iwlm_data.get("dinner_meal_type"),
                    iwlm_data.get("snac"),
                    iwlm_data.get("habits_alc_smoke"),
                    iwlm_data.get("wakeup_time"),
                    iwlm_data.get("bedtime"),
                    iwlm_data.get("daily_chores"),
                    iwlm_data.get("free_times"),
                    iwlm_data.get("people_met"),
                    iwlm_data.get("toilet_style"),
                    iwlm_data.get("bathing_habits"),
                    iwlm_data.get("grooming_habits"),
                    iwlm_data.get("haircut_salon"),
                    iwlm_data.get("favorite_color"),
                    iwlm_data.get("favorite_clothing"),
                    iwlm_data.get("favorite_footwear"),
                    iwlm_data.get("favorite_music"),
                    iwlm_data.get("favorite_tv_radio"),
                    iwlm_data.get("leisure_activities"),
                    iwlm_data.get("favorite_place"),
                    iwlm_data.get("job_status"),
                    iwlm_data.get("interests"),
                    iwlm_data.get("strengths_and_weaknesses"),
                    iwlm_data.get("characteristics"),
                    iwlm_data.get("others"),
                    iwlm_data.get("keep_doing"),
                    iwlm_data.get("keep_doing_other"),
                    iwlm_data.get("future_activities"),
                    iwlm_data.get("future_activities_other"),
                    iwlm_data.get("residence_type"),
                    iwlm_data.get("residence_type_other"),
                    iwlm_data.get("anxiety_and_sadness"),
                    iwlm_data.get("anxiety_and_sadness_other"),
                    iwlm_data.get("areas_of_support"),
                    iwlm_data.get("areas_of_support_other"),
                    iwlm_data.get("future_care_plan"),
                    iwlm_data.get("future_care_plan_other"),
                    user_id,
                ),
            )
        else:
            # 新規作成
            cursor.execute(
                """
                INSERT INTO iwlm (user_id, meal_frequency, morning_meal_type, lunch_meal_type, dinner_meal_type,
                                snac, habits_alc_smoke, wakeup_time, bedtime, daily_chores, free_times, people_met,
                                toilet_style, bathing_habits, grooming_habits, haircut_salon, favorite_color,
                                favorite_clothing, favorite_footwear, favorite_music, favorite_tv_radio,
                                leisure_activities, favorite_place, job_status, interests, strengths_and_weaknesses,
                                characteristics, others, keep_doing, keep_doing_other, future_activities, future_activities_other,
                                residence_type, residence_type_other, anxiety_and_sadness, anxiety_and_sadness_other,
                                areas_of_support, areas_of_support_other, future_care_plan, future_care_plan_other)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    user_id,
                    iwlm_data.get("meal_frequency"),
                    iwlm_data.get("morning_meal_type"),
                    iwlm_data.get("lunch_meal_type"),
                    iwlm_data.get("dinner_meal_type"),
                    iwlm_data.get("snac"),
                    iwlm_data.get("habits_alc_smoke"),
                    iwlm_data.get("wakeup_time"),
                    iwlm_data.get("bedtime"),
                    iwlm_data.get("daily_chores"),
                    iwlm_data.get("free_times"),
                    iwlm_data.get("people_met"),
                    iwlm_data.get("toilet_style"),
                    iwlm_data.get("bathing_habits"),
                    iwlm_data.get("grooming_habits"),
                    iwlm_data.get("haircut_salon"),
                    iwlm_data.get("favorite_color"),
                    iwlm_data.get("favorite_clothing"),
                    iwlm_data.get("favorite_footwear"),
                    iwlm_data.get("favorite_music"),
                    iwlm_data.get("favorite_tv_radio"),
                    iwlm_data.get("leisure_activities"),
                    iwlm_data.get("favorite_place"),
                    iwlm_data.get("job_status"),
                    iwlm_data.get("interests"),
                    iwlm_data.get("strengths_and_weaknesses"),
                    iwlm_data.get("characteristics"),
                    iwlm_data.get("others"),
                    iwlm_data.get("keep_doing"),
                    iwlm_data.get("keep_doing_other"),
                    iwlm_data.get("future_activities"),
                    iwlm_data.get("future_activities_other"),
                    iwlm_data.get("residence_type"),
                    iwlm_data.get("residence_type_other"),
                    iwlm_data.get("anxiety_and_sadness"),
                    iwlm_data.get("anxiety_and_sadness_other"),
                    iwlm_data.get("areas_of_support"),
                    iwlm_data.get("areas_of_support_other"),
                    iwlm_data.get("future_care_plan"),
                    iwlm_data.get("future_care_plan_other"),
                ),
            )

        conn.commit()
        conn.close()

    def get_diary_by_user_id(self, user_id):
        """ユーザーIDで日記一覧を取得"""
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM diary WHERE user_id = ? ORDER BY date DESC", (user_id,))
        diaries = cursor.fetchall()
        conn.close()
        return diaries

    def get_diary_by_date(self, user_id, date):
        """指定日の日記を取得"""
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM diary WHERE user_id = ? AND date = ?", (user_id, date))
        diary = cursor.fetchone()
        conn.close()
        return diary

    def get_diary_dates_with_entries(self, user_id, year, month):
        """指定月に日記がある日付のリストを取得"""
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT date FROM diary WHERE user_id = ? AND strftime('%Y', date) = ? AND strftime('%m', date) = ?",
            (user_id, str(year), str(month).zfill(2)),
        )
        dates = [row[0] for row in cursor.fetchall()]
        conn.close()
        return dates

    def create_or_update_diary(self, user_id, date, title, content, photo_path=None, thumbnail_path=None):
        """日記を作成または更新"""
        conn = self.get_connection()
        cursor = conn.cursor()

        # 既存の日記があるかチェック
        cursor.execute("SELECT id FROM diary WHERE user_id = ? AND date = ?", (user_id, date))
        existing_diary = cursor.fetchone()

        if existing_diary:
            # 更新
            if photo_path and thumbnail_path:
                cursor.execute(
                    "UPDATE diary SET title = ?, content = ?, photo_path = ?, thumbnail_path = ?, updated_at = CURRENT_TIMESTAMP WHERE user_id = ? AND date = ?",
                    (title, content, photo_path, thumbnail_path, user_id, date),
                )
            else:
                cursor.execute(
                    "UPDATE diary SET title = ?, content = ?, updated_at = CURRENT_TIMESTAMP WHERE user_id = ? AND date = ?",
                    (title, content, user_id, date),
                )
        else:
            # 新規作成
            cursor.execute(
                "INSERT INTO diary (user_id, date, title, content, photo_path, thumbnail_path) VALUES (?, ?, ?, ?, ?, ?)",
                (user_id, date, title, content, photo_path, thumbnail_path),
            )

        conn.commit()
        conn.close()

    def delete_diary(self, user_id, date):
        """指定日の日記を削除"""
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM diary WHERE user_id = ? AND date = ?", (user_id, date))
        conn.commit()
        conn.close()


# データベースインスタンス
db = Database()
