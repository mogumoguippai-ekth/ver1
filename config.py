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

        # user_goalsテーブル作成
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS user_goals (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id VARCHAR(50) NOT NULL,
                long_term_goal TEXT NOT NULL,
                short_term_goals TEXT NOT NULL,
                goals_version INTEGER DEFAULT 1,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
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

    def analyze_user_goals(self, user_id):
        """ユーザーのプロフィールとIWLMデータを分析して目標を提案"""
        conn = self.get_connection()
        cursor = conn.cursor()

        # ユーザー情報を取得
        cursor.execute("SELECT * FROM users WHERE user_id = ?", (user_id,))
        user_data = cursor.fetchone()

        # プロフィール情報を取得
        cursor.execute("SELECT * FROM profiles WHERE user_id = ?", (user_id,))
        profile_data = cursor.fetchone()

        # IWLM情報を取得
        cursor.execute("SELECT * FROM iwlm WHERE user_id = ?", (user_id,))
        iwlm_data = cursor.fetchone()

        conn.close()

        # 分析結果に基づいて目標を生成
        goals = self.generate_goals(user_data, profile_data, iwlm_data)
        return goals

    def generate_goals(self, user_data, profile_data, iwlm_data):
        """データに基づいて個人化された目標を生成"""
        long_term_goal = self.generate_long_term_goal(user_data, profile_data, iwlm_data)
        short_term_goals = self.generate_short_term_goals(user_data, profile_data, iwlm_data)

        return {"long_term_goal": long_term_goal, "short_term_goals": short_term_goals}

    def generate_long_term_goal(self, user_data, profile_data, iwlm_data):
        """長期目標（3年後）を生成"""
        base_goals = [
            "趣味と地域活動を通じて、充実した社会的なつながりを築き、心身ともに活力に満ちた毎日を送る",
            "健康で安定した生活リズムを維持しながら、新しい挑戦と学習を通じて成長し続ける",
            "家族や友人との関係を深め、地域社会に貢献しながら、自分らしい充実した人生を歩む",
        ]

        # 年齢に基づく調整
        if user_data and user_data[9]:  # birth_date
            from datetime import datetime, date

            try:
                birth_date = datetime.strptime(user_data[9], "%Y-%m-%d").date()
                today = date.today()
                age = (
                    today.year
                    - birth_date.year
                    - ((today.month, today.day) < (birth_date.month, birth_date.day))
                )

                if age >= 60:
                    base_goals[0] = "健康管理を最優先に、趣味と地域活動を通じて充実したセカンドライフを送る"
                elif age < 30:
                    base_goals[0] = (
                        "キャリア形成と人間関係構築を両立させ、将来への基盤となる充実した生活を築く"
                    )
            except:
                pass

        # IWLMデータに基づく調整
        if iwlm_data:
            # 健康関連の関心が高い場合
            if any(keyword in str(iwlm_data).lower() for keyword in ["運動", "健康", "体力", "ウォーキング"]):
                base_goals[0] = "健康習慣を基盤として、趣味と地域活動を通じて充実した社会的なつながりを築く"

            # 趣味や創作活動への関心が高い場合
            if any(keyword in str(iwlm_data).lower() for keyword in ["趣味", "創作", "芸術", "音楽", "写真"]):
                base_goals[0] = "創作活動と地域活動を通じて、自己表現と社会貢献を両立させた充実した生活を送る"

        return base_goals[0]

    def generate_short_term_goals(self, user_data, profile_data, iwlm_data):
        """短期目標（1年以内）を3つ生成"""
        goals = []

        # 基本の短期目標
        base_short_goals = [
            {
                "title": "新しい趣味の探求と実践",
                "description": "1年以内に、地域のカルチャースクールやオンラインコミュニティを活用して、興味のある趣味を一つ見つけて、半年間継続する。",
                "reason": "新しい趣味に挑戦することで、気分転換になり、同じ趣味を持つ人との新たな出会いにつながります。",
            },
            {
                "title": "健康習慣の確立",
                "description": "週に3日以上、30分間のウォーキングやストレッチを行う習慣を身につける。",
                "reason": "適度な運動は、体力維持や気分向上に効果的であり、いきいきと過ごすための土台となります。",
            },
            {
                "title": "地域コミュニティとの接点作り",
                "description": "今後1年間で、地域のイベント（例：お祭り、マルシェ、ボランティア活動）に3回以上参加する。",
                "reason": "地域活動に参加することで、地域社会への貢献を実感し、新たな交流の機会が生まれます。",
            },
        ]

        # IWLMデータに基づく個人化
        if iwlm_data:
            # 食事関連のデータがある場合
            if iwlm_data[2] or iwlm_data[3] or iwlm_data[4] or iwlm_data[5]:  # meal関連
                base_short_goals[1] = {
                    "title": "食生活の改善と健康習慣の確立",
                    "description": "現在の食事パターンを活かしながら、週に3日以上、30分間の軽い運動習慣を身につける。",
                    "reason": "適切な食事と運動の組み合わせにより、より効果的な健康維持が期待できます。",
                }

            # 趣味や嗜好のデータがある場合
            if iwlm_data[16] or iwlm_data[17] or iwlm_data[18] or iwlm_data[19]:  # favorite関連
                favorite_activities = []
                if iwlm_data[16]:  # favorite_color
                    favorite_activities.append("色彩")
                if iwlm_data[17]:  # favorite_clothing
                    favorite_activities.append("ファッション")
                if iwlm_data[18]:  # favorite_footwear
                    favorite_activities.append("装い")
                if iwlm_data[19]:  # favorite_music
                    favorite_activities.append("音楽")

                if favorite_activities:
                    activity_text = "・".join(favorite_activities)
                    base_short_goals[0] = {
                        "title": f"{activity_text}に関連した趣味の探求",
                        "description": f"現在の好み（{activity_text}）を活かして、関連する新しい趣味や活動を見つけて半年間継続する。",
                        "reason": "既存の興味を発展させることで、より深い楽しみと新しい出会いが期待できます。",
                    }

            # 生活リズムのデータがある場合
            if iwlm_data[8] or iwlm_data[9]:  # wakeup_time, bedtime
                base_short_goals[1] = {
                    "title": "生活リズムの最適化と健康習慣の確立",
                    "description": "現在の生活リズムを維持しながら、週に3日以上、30分間の軽い運動を組み込む。",
                    "reason": "既存の生活パターンに運動を組み込むことで、無理なく健康習慣を確立できます。",
                }

        return base_short_goals

    def save_user_goals(self, user_id, goals_data):
        """ユーザーの目標を保存"""
        import json

        conn = self.get_connection()
        cursor = conn.cursor()

        # 目標データをJSON形式で保存
        long_term_goal = goals_data["long_term_goal"]
        short_term_goals = json.dumps(goals_data["short_term_goals"], ensure_ascii=False)

        cursor.execute(
            "INSERT INTO user_goals (user_id, long_term_goal, short_term_goals) VALUES (?, ?, ?)",
            (user_id, long_term_goal, short_term_goals),
        )

        conn.commit()
        conn.close()
        return cursor.lastrowid

    def get_user_goals(self, user_id, limit=10):
        """ユーザーの目標履歴を取得"""
        import json

        conn = self.get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM user_goals WHERE user_id = ? ORDER BY created_at DESC LIMIT ?", (user_id, limit)
        )
        goals_list = cursor.fetchall()

        # JSON形式のデータをパース
        parsed_goals = []
        for goal in goals_list:
            parsed_goal = list(goal)
            parsed_goal[3] = json.loads(goal[3])  # short_term_goalsをパース
            parsed_goals.append(parsed_goal)

        conn.close()
        return parsed_goals

    def get_latest_user_goals(self, user_id):
        """ユーザーの最新の目標を取得"""
        import json

        conn = self.get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM user_goals WHERE user_id = ? ORDER BY created_at DESC LIMIT 1", (user_id,)
        )
        goal = cursor.fetchone()

        if goal:
            # JSON形式のデータをパース
            parsed_goal = list(goal)
            parsed_goal[3] = json.loads(goal[3])  # short_term_goalsをパース
            conn.close()
            return parsed_goal

        conn.close()
        return None

    def should_update_goals(self, user_id):
        """目標の更新が必要かどうかを判定（90日間隔）"""
        import datetime

        conn = self.get_connection()
        cursor = conn.cursor()

        # 最新の目標作成日を取得
        cursor.execute(
            "SELECT created_at FROM user_goals WHERE user_id = ? ORDER BY created_at DESC LIMIT 1", (user_id,)
        )
        result = cursor.fetchone()

        conn.close()

        if not result:
            return True  # 目標が存在しない場合は作成

        last_created = datetime.datetime.strptime(result[0], "%Y-%m-%d %H:%M:%S")
        days_diff = (datetime.datetime.now() - last_created).days

        return days_diff >= 90  # 90日以上経過している場合は更新

    def has_data_changed(self, user_id):
        """ユーザーデータに変更があるかどうかを判定"""
        conn = self.get_connection()
        cursor = conn.cursor()

        # 最新の目標作成日を取得
        cursor.execute(
            "SELECT created_at FROM user_goals WHERE user_id = ? ORDER BY created_at DESC LIMIT 1", (user_id,)
        )
        goals_result = cursor.fetchone()

        # ユーザー情報の最終更新日を取得
        cursor.execute("SELECT updated_at FROM users WHERE user_id = ?", (user_id,))
        user_result = cursor.fetchone()

        # プロフィール情報の最終更新日を取得
        cursor.execute("SELECT updated_at FROM profiles WHERE user_id = ?", (user_id,))
        profile_result = cursor.fetchone()

        # IWLM情報の最終更新日を取得
        cursor.execute("SELECT updated_at FROM iwlm WHERE user_id = ?", (user_id,))
        iwlm_result = cursor.fetchone()

        conn.close()

        if not goals_result:
            return False  # 目標が存在しない場合は変更判定なし

        goals_created = datetime.datetime.strptime(goals_result[0], "%Y-%m-%d %H:%M:%S")

        # ユーザー情報の更新日をチェック
        if user_result and user_result[0]:
            user_updated = datetime.datetime.strptime(user_result[0], "%Y-%m-%d %H:%M:%S")
            if user_updated > goals_created:
                return True

        # プロフィール情報の更新日をチェック
        if profile_result and profile_result[0]:
            profile_updated = datetime.datetime.strptime(profile_result[0], "%Y-%m-%d %H:%M:%S")
            if profile_updated > goals_created:
                return True

        # IWLM情報の更新日をチェック
        if iwlm_result and iwlm_result[0]:
            iwlm_updated = datetime.datetime.strptime(iwlm_result[0], "%Y-%m-%d %H:%M:%S")
            if iwlm_updated > goals_created:
                return True

        return False

    def save_user_goals(self, user_id, goals_data):
        """ユーザーの目標を保存（重複チェック付き）"""
        import json

        conn = self.get_connection()
        cursor = conn.cursor()

        # 目標データをJSON形式で保存
        long_term_goal = goals_data["long_term_goal"]
        short_term_goals = json.dumps(goals_data["short_term_goals"], ensure_ascii=False)

        # 最新の目標と比較して重複チェック
        cursor.execute(
            "SELECT long_term_goal, short_term_goals FROM user_goals WHERE user_id = ? ORDER BY created_at DESC LIMIT 1",
            (user_id,),
        )
        latest_goal = cursor.fetchone()

        # 同じ内容の場合は保存しない
        if latest_goal and latest_goal[0] == long_term_goal and latest_goal[1] == short_term_goals:
            conn.close()
            return None  # 重複のため保存しない

        cursor.execute(
            "INSERT INTO user_goals (user_id, long_term_goal, short_term_goals) VALUES (?, ?, ?)",
            (user_id, long_term_goal, short_term_goals),
        )

        conn.commit()
        conn.close()
        return cursor.lastrowid


# データベースインスタンス
db = Database()
