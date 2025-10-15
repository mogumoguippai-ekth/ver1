# config.py コード解説

## 概要
「私の望む暮らし」アプリケーションのデータベース操作を担当するクラス。SQLiteデータベースを使用し、ユーザー管理、プロフィール管理、日記管理、目標管理、家族管理、招待コード管理などの全機能を提供します。

---

## 📋 目次

### 1. クラス定義・初期化
- [1.1 Databaseクラス](#11-databaseクラス)
- [1.2 グローバルインスタンス](#12-グローバルインスタンス)

### 2. ユーティリティ関数
- [2.1 _parse_datetime関数](#21-parse_datetime関数)

### 3. データベース接続管理
- [3.1 get_connection関数](#31-get_connection関数)

### 4. データベース初期化・テーブル作成
- [4.1 init_db関数](#41-init_db関数)

### 5. ユーザー管理機能
- [5.1 create_user関数](#51-create_user関数)
- [5.2 get_user_by_id関数](#52-get_user_by_id関数)
- [5.3 get_user_by_email関数](#53-get_user_by_email関数)
- [5.4 authenticate_user関数](#54-authenticate_user関数)

### 6. プロフィール管理機能
- [6.1 get_profile_by_user_id関数](#61-get_profile_by_user_id関数)
- [6.2 create_or_update_profile関数](#62-create_or_update_profile関数)

### 7. IWLM（暮らし情報）管理機能
- [7.1 get_iwlm_by_user_id関数](#71-get_iwlm_by_user_id関数)
- [7.2 create_or_update_iwlm関数](#72-create_or_update_iwlm関数)

### 8. 日記管理機能
- [8.1 get_diary_by_user_id関数](#81-get_diary_by_user_id関数)
- [8.2 get_diary_by_date関数](#82-get_diary_by_date関数)
- [8.3 get_diary_dates_with_entries関数](#83-get_diary_dates_with_entries関数)
- [8.4 create_or_update_diary関数](#84-create_or_update_diary関数)
- [8.5 delete_diary関数](#85-delete_diary関数)
- [8.6 delete_photo_paths関数](#86-delete_photo_paths関数)

### 9. 目標管理機能
- [9.1 analyze_user_goals関数](#91-analyze_user_goals関数)
- [9.2 generate_goals関数](#92-generate_goals関数)
- [9.3 generate_long_term_goal関数](#93-generate_long_term_goal関数)
- [9.4 generate_short_term_goals関数](#94-generate_short_term_goals関数)
- [9.5 save_user_goals関数](#95-save_user_goals関数)
- [9.6 get_user_goals関数](#96-get_user_goals関数)
- [9.7 get_latest_user_goals関数](#97-get_latest_user_goals関数)
- [9.8 should_update_goals関数](#98-should_update_goals関数)
- [9.9 has_data_changed関数](#99-has_data_changed関数)
- [9.10 save_user_goals_check関数](#910-save_user_goals_check関数)

### 10. 家族管理機能
- [10.1 generate_invitation_code関数](#101-generate_invitation_code関数)
- [10.2 validate_invitation_code関数](#102-validate_invitation_code関数)
- [10.3 use_invitation_code関数](#103-use_invitation_code関数)
- [10.4 create_family_user関数](#104-create_family_user関数)
- [10.5 get_family_user_by_id関数](#105-get_family_user_by_id関数)
- [10.6 get_family_users_by_parent関数](#106-get_family_users_by_parent関数)
- [10.7 update_user_family_ids関数](#107-update_user_family_ids関数)
- [10.8 get_next_family_slot関数](#108-get_next_family_slot関数)
- [10.9 delete_family_user関数](#109-delete_family_user関数)
- [10.10 _delete_family_user_record関数](#1010-delete_family_user_record関数)
- [10.11 _update_parent_family_ids関数](#1011-update_parent_family_ids関数)

### 11. マイグレーション処理
- [11.1 テーブル構造変更](#111-テーブル構造変更)

---

## 1. クラス定義・初期化 <a id="1-クラス定義初期化"></a>

### 1.1 Databaseクラス <a id="11-databaseクラス"></a>
```python
class Database:
    def __init__(self, db_path="db.sqlite"):
        self.db_path = db_path
```

**説明:**
- SQLiteデータベースファイルへのパスを管理
- デフォルトは`db.sqlite`
- 単一のデータベースインスタンスとして使用

### 1.2 グローバルインスタンス <a id="12-グローバルインスタンス"></a>
```python
db = Database()
```

**説明:**
- アプリケーション全体で使用するデータベースインスタンス
- app.pyから`from config import db`でインポート

---

## 2. ユーティリティ関数 <a id="2-ユーティリティ関数"></a>

### 2.1 _parse_datetime関数 <a id="21-parse_datetime関数"></a>
```python
def _parse_datetime(self, datetime_str):
    """マイクロ秒対応の日時解析ヘルパー関数"""
    try:
        if "." in datetime_str:
            return datetime.datetime.strptime(datetime_str, "%Y-%m-%d %H:%M:%S.%f")
        else:
            return datetime.datetime.strptime(datetime_str, "%Y-%m-%d %H:%M:%S")
    except ValueError:
        # フォーマットが合わない場合は現在時刻を返す
        return datetime.datetime.now()
```

**説明:**
- SQLiteの日時文字列をPythonのdatetimeオブジェクトに変換
- マイクロ秒対応（`.%f`フォーマット）
- エラー時は現在時刻を返すフォールバック機能

---

## 3. データベース接続管理 <a id="3-データベース接続管理"></a>

### 3.1 get_connection関数 <a id="31-get_connection関数"></a>
```python
def get_connection(self):
    """データベース接続を取得"""
    conn = sqlite3.connect(self.db_path, timeout=30.0)
    # WALモードを有効にして同時アクセスを改善
    conn.execute("PRAGMA journal_mode=WAL")
    # ロックタイムアウトを設定
    conn.execute("PRAGMA busy_timeout=30000")  # 30秒
    return conn
```

**説明:**
- SQLiteデータベースへの接続を確立
- **WALモード**: Write-Ahead Loggingで同時アクセス性能向上
- **タイムアウト設定**: 30秒の接続タイムアウト
- **ビジータイムアウト**: 30秒のロック待機時間

---

## 4. データベース初期化・テーブル作成 <a id="4-データベース初期化テーブル作成"></a>

### 4.1 init_db関数 <a id="41-init_db関数"></a>
```python
def init_db(self):
    """データベースとテーブルを初期化"""
    conn = self.get_connection()
    cursor = conn.cursor()
    
    # 各種テーブルの作成処理...
```

**説明:**
- アプリケーション起動時にデータベースとテーブルを初期化
- 6つの主要テーブルを作成
- マイグレーション処理も含む

#### 4.1.1 usersテーブル
```sql
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
```

**説明:**
- **基本情報**: ユーザーID、メール、パスワード、ユーザータイプ
- **個人情報**: 名前、フリガナ、ニックネーム、性別、生年月日
- **家族管理**: family_id1-3で家族ユーザーとの関連付け
- **制約**: ユーザータイプと性別にCHECK制約

#### 4.1.2 profilesテーブル
```sql
CREATE TABLE IF NOT EXISTS profiles (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id VARCHAR(50) NOT NULL,
    home VARCHAR(100),
    spouse TEXT,
    children_living TEXT,
    children_separate TEXT,
    family_living TEXT,
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
```

**説明:**
- **家族構成**: 配偶者、同居・別居の子ども
- **医療情報**: 治療歴、現在の治療、医療機関
- **支援体制**: 頼れる家族、近所の人、相談できる友人
- **経済状況**: 収入源

#### 4.1.3 iwlmテーブル
```sql
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
```

**説明:**
- **I Want to Live My life**: 暮らしに関する詳細情報
- **生活習慣**: 食事、睡眠、トイレ、入浴、身だしなみ
- **趣味・嗜好**: 好きな色、音楽、服装、活動
- **将来計画**: 続けたいこと、新しい活動、住まい、不安、支援

#### 4.1.4 diaryテーブル
```sql
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
```

**説明:**
- **日記管理**: 日付、タイトル、内容
- **写真機能**: 元画像とサムネイルのパス保存
- **制約**: ユーザーごとに1日1つの日記のみ

#### 4.1.5 user_goalsテーブル
```sql
CREATE TABLE IF NOT EXISTS user_goals (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id VARCHAR(50) NOT NULL,
    long_term_goal TEXT NOT NULL,
    short_term_goals TEXT NOT NULL,
    goals_version INTEGER DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users (user_id)
)
```

**説明:**
- **目標管理**: 長期目標（3年後）と短期目標（1年以内）
- **バージョン管理**: goals_versionで目標の更新履歴
- **履歴機能**: 過去の目標も保存

#### 4.1.6 family_usersテーブル
```sql
CREATE TABLE IF NOT EXISTS family_users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    family_user_id VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    parent_user_id VARCHAR(50) NOT NULL,
    invitation_code VARCHAR(8) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (parent_user_id) REFERENCES users (user_id)
)
```

**説明:**
- **家族ユーザー管理**: 本人ユーザーの家族メンバー
- **親子関係**: parent_user_idで本人ユーザーとの関連付け
- **招待システム**: 招待コードによる登録

#### 4.1.7 invitation_codesテーブル
```sql
CREATE TABLE IF NOT EXISTS invitation_codes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    code VARCHAR(8) UNIQUE NOT NULL,
    user_id VARCHAR(50) NOT NULL,
    expires_at TIMESTAMP NOT NULL,
    used BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users (user_id)
)
```

**説明:**
- **招待コード管理**: 8桁の数字コード
- **有効期限**: 30分間の有効期限
- **使用状況**: 使用済みフラグ

---

## 5. ユーザー管理機能 <a id="5-ユーザー管理機能"></a>

### 5.1 create_user関数 <a id="51-create_user関数"></a>
```python
def create_user(self, user_data):
    """新しいユーザーを作成"""
    conn = self.get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO users (user_id, email, password, user_type, name, furigana, nickname, gender, birth_date, family_id1, family_id2, family_id3)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (user_data.get("user_id"), user_data.get("email"), user_data.get("password"), ...)
    )

    user_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return user_id
```

**説明:**
- 新規ユーザーの登録
- パラメータ化クエリでSQLインジェクション対策
- 作成されたユーザーのIDを返す

### 5.2 get_user_by_id関数 <a id="52-get_user_by_id関数"></a>
```python
def get_user_by_id(self, user_id):
    """ユーザーIDでユーザー情報を取得"""
    conn = self.get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT id, user_id, email, password, user_type, name, furigana, nickname, 
               gender, birth_date, family_id1, family_id2, family_id3, 
               created_at, updated_at 
        FROM users WHERE user_id = ?
    """,
        (user_id,),
    )
    user = cursor.fetchone()
    conn.close()
    return user
```

**説明:**
- ユーザーIDによる検索
- 全カラムを取得
- タプル形式で返却

### 5.3 get_user_by_email関数 <a id="53-get_user_by_email関数"></a>
```python
def get_user_by_email(self, email):
    """メールアドレスでユーザー情報を取得"""
    conn = self.get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
    user = cursor.fetchone()
    conn.close()
    return user
```

**説明:**
- メールアドレスによる検索
- 重複チェック用

### 5.4 authenticate_user関数 <a id="54-authenticate_user関数"></a>
```python
def authenticate_user(self, user_id, password):
    """ユーザー認証"""
    conn = self.get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE user_id = ? AND password = ?", (user_id, password))
    user = cursor.fetchone()
    conn.close()
    return user
```

**説明:**
- ユーザーIDとパスワードによる認証
- 注意: 実際はパスワードハッシュを使用

---

## 6. プロフィール管理機能 <a id="6-プロフィール管理機能"></a>

### 6.1 get_profile_by_user_id関数 <a id="61-get_profile_by_user_id関数"></a>
```python
def get_profile_by_user_id(self, user_id):
    """ユーザーIDでプロフィール情報を取得"""
    conn = self.get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM profiles WHERE user_id = ?", (user_id,))
    profile = cursor.fetchone()
    conn.close()
    return profile
```

**説明:**
- ユーザーのプロフィール詳細情報を取得
- 家族構成、医療情報、支援体制など

### 6.2 create_or_update_profile関数 <a id="62-create_or_update_profile関数"></a>
```python
def create_or_update_profile(self, user_id, profile_data):
    """プロフィール情報を作成または更新"""
    conn = self.get_connection()
    cursor = conn.cursor()

    # 既存のプロフィールがあるかチェック
    cursor.execute("SELECT id FROM profiles WHERE user_id = ?", (user_id,))
    existing_profile = cursor.fetchone()

    if existing_profile:
        # 更新処理
        cursor.execute(
            """
            UPDATE profiles 
            SET home = ?, spouse = ?, children_living = ?, children_separate = ?, family_living = ?,
                treated_illness = ?, under_treatment = ?, medical_facilities = ?,
                most_relied_family = ?, trusted_neighbor = ?, consulted_friend = ?,
                money_sources = ?, updated_at = CURRENT_TIMESTAMP
            WHERE user_id = ?
            """,
            (profile_data.get("home"), profile_data.get("spouse"), ...)
        )
    else:
        # 新規作成処理
        cursor.execute(
            """
            INSERT INTO profiles (user_id, home, spouse, children_living, children_separate, family_living,
                                treated_illness, under_treatment, medical_facilities,
                                most_relied_family, trusted_neighbor, consulted_friend, money_sources)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (user_id, profile_data.get("home"), profile_data.get("spouse"), ...)
        )

    conn.commit()
    conn.close()
```

**説明:**
- **UPSERT処理**: 既存データがあれば更新、なければ新規作成
- **デバッグログ**: family_livingの値変更をログ出力
- **全フィールド更新**: プロフィールの全項目を一括更新

---

## 7. IWLM（暮らし情報）管理機能 <a id="7-iwlm暮らし情報管理機能"></a>

### 7.1 get_iwlm_by_user_id関数 <a id="71-get_iwlm_by_user_id関数"></a>
```python
def get_iwlm_by_user_id(self, user_id):
    """ユーザーIDでIWLM情報を取得"""
    conn = self.get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM iwlm WHERE user_id = ?", (user_id,))
    iwlm = cursor.fetchone()
    conn.close()
    return iwlm
```

**説明:**
- 暮らしに関する詳細情報を取得
- 生活習慣、趣味、将来計画など

### 7.2 create_or_update_iwlm関数 <a id="72-create_or_update_iwlm関数"></a>
```python
def create_or_update_iwlm(self, user_id, iwlm_data):
    """IWLM情報を作成または更新"""
    conn = self.get_connection()
    cursor = conn.cursor()

    # 既存のIWLMレコードがあるかチェック
    cursor.execute("SELECT id FROM iwlm WHERE user_id = ?", (user_id,))
    existing_iwlm = cursor.fetchone()

    if existing_iwlm:
        # 更新処理（全39項目）
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
            (iwlm_data.get("meal_frequency"), iwlm_data.get("morning_meal_type"), ...)
        )
    else:
        # 新規作成処理
        cursor.execute(
            """
            INSERT INTO iwlm (user_id, meal_frequency, morning_meal_type, ...)
            VALUES (?, ?, ?, ...)
            """,
            (user_id, iwlm_data.get("meal_frequency"), ...)
        )

    conn.commit()
    conn.close()
```

**説明:**
- **大規模UPSERT**: 39項目の暮らし情報を一括処理
- **複雑なデータ構造**: 生活習慣、趣味、将来計画を包括的に管理
- **効率的な更新**: 全項目を一度に更新

---

## 8. 日記管理機能 <a id="8-日記管理機能"></a>

### 8.1 get_diary_by_user_id関数 <a id="81-get_diary_by_user_id関数"></a>
```python
def get_diary_by_user_id(self, user_id):
    """ユーザーIDで日記一覧を取得"""
    conn = self.get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM diary WHERE user_id = ? ORDER BY date DESC", (user_id,))
    diaries = cursor.fetchall()
    conn.close()
    return diaries
```

**説明:**
- ユーザーの全日記を日付降順で取得
- 日記一覧表示用

### 8.2 get_diary_by_date関数 <a id="82-get_diary_by_date関数"></a>
```python
def get_diary_by_date(self, user_id, date):
    """指定日の日記を取得"""
    conn = self.get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM diary WHERE user_id = ? AND date = ?", (user_id, date))
    diary = cursor.fetchone()
    conn.close()
    return diary
```

**説明:**
- 特定の日付の日記を取得
- 日記編集・表示用

### 8.3 get_diary_dates_with_entries関数 <a id="83-get_diary_dates_with_entries関数"></a>
```python
def get_diary_dates_with_entries(self, user_id, year, month):
    """指定月に日記がある日付とタイトルの辞書を取得"""
    conn = self.get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT date, title FROM diary WHERE user_id = ? AND strftime('%Y', date) = ? AND strftime('%m', date) = ?",
        (user_id, str(year), str(month).zfill(2)),
    )
    diary_entries = {}
    for row in cursor.fetchall():
        date, title = row
        diary_entries[date] = title if title else ""
    conn.close()
    return diary_entries
```

**説明:**
- **カレンダー表示用**: 指定月の日記がある日付を取得
- **辞書形式**: 日付をキー、タイトルを値とする辞書
- **strftime関数**: SQLiteの日付関数で年月を抽出

### 8.4 create_or_update_diary関数 <a id="84-create_or_update_diary関数"></a>
```python
def create_or_update_diary(self, user_id, date, title, content, photo_path=None, thumbnail_path=None):
    """日記を作成または更新"""
    conn = self.get_connection()
    cursor = conn.cursor()

    # 既存の日記があるかチェック
    cursor.execute("SELECT id FROM diary WHERE user_id = ? AND date = ?", (user_id, date))
    existing_diary = cursor.fetchone()

    if existing_diary:
        # 更新処理
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
```

**説明:**
- **写真対応**: 写真がある場合とない場合で処理を分岐
- **UPSERT処理**: 既存日記があれば更新、なければ新規作成
- **日付制約**: 1日1つの日記のみ許可

### 8.5 delete_diary関数 <a id="85-delete_diary関数"></a>
```python
def delete_diary(self, user_id, date):
    """指定日の日記を削除"""
    conn = self.get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM diary WHERE user_id = ? AND date = ?", (user_id, date))
    conn.commit()
    conn.close()
```

**説明:**
- 指定日の日記を完全削除
- 関連する写真ファイルは別途削除処理が必要

### 8.6 delete_photo_paths関数 <a id="86-delete_photo_paths関数"></a>
```python
def delete_photo_paths(self, user_id, date):
    """指定日の日記の写真パスのみを削除"""
    conn = self.get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE diary SET photo_path = NULL, thumbnail_path = NULL WHERE user_id = ? AND date = ?",
        (user_id, date),
    )
    conn.commit()
    conn.close()
```

**説明:**
- 日記は残して写真のみ削除
- 写真パスをNULLに設定

---

## 9. 目標管理機能 <a id="9-目標管理機能"></a>

### 9.1 analyze_user_goals関数 <a id="91-analyze_user_goals関数"></a>
```python
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
    return self.generate_goals(user_data, profile_data, iwlm_data)
```

**説明:**
- **データ収集**: ユーザー、プロフィール、IWLM情報を統合取得
- **分析処理**: 取得したデータを基に目標を生成
- **統合処理**: 複数のテーブルから情報を統合

### 9.2 generate_goals関数 <a id="92-generate_goals関数"></a>
```python
def generate_goals(self, user_data, profile_data, iwlm_data):
    """データに基づいて個人化された目標を生成"""
    long_term_goal = self.generate_long_term_goal(user_data, profile_data, iwlm_data)
    short_term_goals = self.generate_short_term_goals(user_data, profile_data, iwlm_data)

    return {"long_term_goal": long_term_goal, "short_term_goals": short_term_goals}
```

**説明:**
- **目標構造**: 長期目標（3年後）と短期目標（1年以内）
- **個人化**: ユーザーデータに基づくカスタマイズ

### 9.3 generate_long_term_goal関数 <a id="93-generate_long_term_goal関数"></a>
```python
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
        except Exception:
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
```

**説明:**
- **基本目標**: 3つのベースとなる長期目標
- **年齢調整**: 60歳以上はセカンドライフ、30歳未満はキャリア形成
- **データ分析**: IWLMデータからキーワードを抽出して目標をカスタマイズ
- **キーワード検索**: 健康、趣味、創作などのキーワードで個人化

### 9.4 generate_short_term_goals関数 <a id="94-generate_short_term_goals関数"></a>
```python
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

    return base_short_goals
```

**説明:**
- **基本構造**: タイトル、説明、理由の3要素
- **データ分析**: IWLMデータから具体的な項目を抽出
- **個人化**: 食事、趣味、嗜好データに基づくカスタマイズ
- **詳細設計**: 具体的で実行可能な目標を生成

### 9.5 save_user_goals関数 <a id="95-save_user_goals関数"></a>
```python
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
```

**説明:**
- **JSON保存**: 短期目標をJSON形式で保存
- **日本語対応**: ensure_ascii=Falseで日本語を正しく保存
- **履歴管理**: 複数の目標を履歴として保存

### 9.6 get_user_goals関数 <a id="96-get_user_goals関数"></a>
```python
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
```

**説明:**
- **履歴取得**: 最新10件の目標履歴を取得
- **JSON解析**: 保存されたJSONデータをPythonオブジェクトに変換
- **日付順**: 作成日時の降順で取得

### 9.7 get_latest_user_goals関数 <a id="97-get_latest_user_goals関数"></a>
```python
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
```

**説明:**
- **最新目標**: 最も新しい目標を1件取得
- **JSON解析**: 短期目標のJSONを解析
- **null対応**: 目標がない場合はNoneを返す

### 9.8 should_update_goals関数 <a id="98-should_update_goals関数"></a>
```python
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

    # マイクロ秒対応の日時解析
    last_created = self._parse_datetime(result[0])
    # days_diff = (datetime.datetime.now() - last_created).days
    # return days_diff >= 90  # 90日以上経過している場合は更新
    return True
```

**説明:**
- **90日ルール**: 目標は90日ごとに更新
- **現在は無効化**: 常にTrueを返す（更新を強制）
- **日時解析**: マイクロ秒対応の日時解析を使用

### 9.9 has_data_changed関数 <a id="99-has_data_changed関数"></a>
```python
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

    # マイクロ秒対応の日時解析（目標作成日）
    goals_created = self._parse_datetime(goals_result[0])

    # ユーザー情報の更新日をチェック
    if user_result and user_result[0]:
        user_updated = self._parse_datetime(user_result[0])
        if user_updated > goals_created:
            return True

    # プロフィール情報の更新日をチェック
    if profile_result and profile_result[0]:
        profile_updated = self._parse_datetime(profile_result[0])
        if profile_updated > goals_created:
            return True

    # IWLM情報の更新日をチェック
    if iwlm_result and iwlm_result[0]:
        iwlm_updated = self._parse_datetime(iwlm_result[0])
        if iwlm_updated > goals_created:
            return True

    return False
```

**説明:**
- **変更検知**: 目標作成後にデータが変更されたかを判定
- **複数テーブル**: users、profiles、iwlmテーブルの更新日をチェック
- **日時比較**: 目標作成日とデータ更新日を比較
- **目標更新のトリガー**: データ変更があった場合に目標更新を促す

### 9.10 save_user_goals_check関数 <a id="910-save_user_goals_check関数"></a>
```python
def save_user_goals_check(self, user_id, goals_data):
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
```

**説明:**
- **重複防止**: 前回と同じ内容の目標は保存しない
- **効率化**: 不要な履歴レコードの作成を防止
- **比較処理**: 長期目標と短期目標の両方を比較

### 9.11 save_user_goals_forced関数
```python
def save_user_goals_forced(self, user_id, goals_data):
    """ユーザーの目標を強制保存（重複チェックなし）"""
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
```

**説明:**
- **強制保存**: 重複チェックなしで必ず保存
- **データ変更時**: プロフィールやIWLMが変更された場合は強制保存

### 9.12 delete_user_goal関数
```python
def delete_user_goal(self, user_id, goal_id):
    """指定された目標履歴を削除"""
    conn = self.get_connection()
    cursor = conn.cursor()

    # 目標が存在し、かつそのユーザーのものであることを確認
    cursor.execute("SELECT id FROM user_goals WHERE id = ? AND user_id = ?", (goal_id, user_id))
    goal = cursor.fetchone()

    if not goal:
        conn.close()
        return False

    # 目標を削除
    cursor.execute("DELETE FROM user_goals WHERE id = ? AND user_id = ?", (goal_id, user_id))

    conn.commit()
    conn.close()
    return True
```

**説明:**
- **権限チェック**: 目標がそのユーザーのものであることを確認
- **安全削除**: 他人の目標を削除できないよう保護
- **履歴管理**: 不要な目標履歴を削除

---

## 10. 家族管理機能 <a id="10-家族管理機能"></a>

### 10.1 generate_invitation_code関数 <a id="101-generate_invitation_code関数"></a>
```python
def generate_invitation_code(self, user_id):
    """8桁の招待コードを生成し、30分間有効にする"""
    import random
    import datetime

    conn = self.get_connection()
    cursor = conn.cursor()

    # 8桁のランダムな数字を生成
    code = str(random.randint(10000000, 99999999))

    # 有効期限（現在時刻から30分後）
    expires_at = datetime.datetime.now() + datetime.timedelta(minutes=30)

    # 招待コードを保存
    cursor.execute(
        "INSERT INTO invitation_codes (code, user_id, expires_at) VALUES (?, ?, ?)",
        (code, user_id, expires_at),
    )

    conn.commit()
    conn.close()

    return code, expires_at
```

**説明:**
- **8桁コード**: 10000000-99999999のランダムな数字
- **有効期限**: 30分間の制限時間
- **セキュリティ**: 短時間での自動無効化

### 10.2 validate_invitation_code関数 <a id="102-validate_invitation_code関数"></a>
```python
def validate_invitation_code(self, code):
    """招待コードの有効性を検証"""
    import datetime

    conn = self.get_connection()
    cursor = conn.cursor()

    # コードが存在し、有効期限内で、未使用かチェック
    cursor.execute(
        "SELECT user_id, expires_at FROM invitation_codes WHERE code = ? AND used = FALSE", (code,)
    )
    result = cursor.fetchone()

    conn.close()

    if not result:
        return False, None

    user_id, expires_at = result
    current_time = datetime.datetime.now()

    # 有効期限チェック（マイクロ秒対応）
    expires_datetime = self._parse_datetime(expires_at)

    if current_time > expires_datetime:
        return False, None

    return True, user_id
```

**説明:**
- **三重チェック**: 存在、有効期限、使用状況を確認
- **親ユーザー取得**: 有効な場合は親ユーザーIDを返す
- **時刻比較**: マイクロ秒対応の日時解析を使用

### 10.3 use_invitation_code関数 <a id="103-use_invitation_code関数"></a>
```python
def use_invitation_code(self, code):
    """招待コードを使用済みにマーク"""
    conn = self.get_connection()
    cursor = conn.cursor()

    cursor.execute("UPDATE invitation_codes SET used = TRUE WHERE code = ?", (code,))

    conn.commit()
    conn.close()
```

**説明:**
- **一回限り**: 招待コードを使用済みにマーク
- **セキュリティ**: 再利用を防止

### 10.4 create_family_user関数 <a id="104-create_family_user関数"></a>
```python
def create_family_user(self, family_data):
    """家族ユーザーを作成"""
    conn = self.get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO family_users (family_user_id, email, password, parent_user_id, invitation_code)
        VALUES (?, ?, ?, ?, ?)
        """,
        (
            family_data.get("family_user_id"),
            family_data.get("email"),
            family_data.get("password"),
            family_data.get("parent_user_id"),
            family_data.get("invitation_code"),
        ),
    )

    family_id = cursor.lastrowid
    conn.commit()
    conn.close()

    return family_id
```

**説明:**
- **家族登録**: 招待コードを使用した家族ユーザー登録
- **親子関係**: parent_user_idで本人ユーザーとの関連付け
- **招待コード記録**: 使用した招待コードを記録

### 10.5 get_family_user_by_id関数 <a id="105-get_family_user_by_id関数"></a>
```python
def get_family_user_by_id(self, family_user_id):
    """家族ユーザーIDで家族ユーザー情報を取得"""
    conn = self.get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM family_users WHERE family_user_id = ?", (family_user_id,))
    family_user = cursor.fetchone()
    conn.close()
    return family_user
```

**説明:**
- 家族ユーザーの詳細情報を取得
- ログイン認証用

### 10.6 get_family_users_by_parent関数 <a id="106-get_family_users_by_parent関数"></a>
```python
def get_family_users_by_parent(self, parent_user_id):
    """親ユーザーIDで家族ユーザー一覧を取得"""
    conn = self.get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM family_users WHERE parent_user_id = ?", (parent_user_id,))
    family_users = cursor.fetchall()
    conn.close()
    return family_users
```

**説明:**
- 本人ユーザーの家族メンバー一覧を取得
- 最大3人まで

### 10.7 update_user_family_ids関数 <a id="107-update_user_family_ids関数"></a>
```python
def update_user_family_ids(self, user_id, family_ids):
    """ユーザーの家族IDを更新"""
    conn = self.get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE users 
        SET family_id1 = ?, family_id2 = ?, family_id3 = ?, updated_at = CURRENT_TIMESTAMP
        WHERE user_id = ?
        """,
        (family_ids[0], family_ids[1], family_ids[2], user_id),
    )

    conn.commit()
    conn.close()
```

**説明:**
- 本人ユーザーのfamily_id1-3を更新
- 家族登録・削除時に実行

### 10.8 get_next_family_slot関数 <a id="108-get_next_family_slot関数"></a>
```python
def get_next_family_slot(self, user_id):
    """次の家族スロット（family_id1-3）を取得"""
    conn = self.get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT family_id1, family_id2, family_id3 FROM users WHERE user_id = ?", (user_id,))
    result = cursor.fetchone()
    conn.close()

    if not result:
        return None

    family_id1, family_id2, family_id3 = result

    if family_id1 is None:
        return 1
    elif family_id2 is None:
        return 2
    elif family_id3 is None:
        return 3
    else:
        return None  # 3人まで登録済み
```

**説明:**
- **空きスロット検索**: family_id1-3のうち空いている位置を返す
- **制限**: 最大3人まで
- **優先順位**: 1→2→3の順で空きを検索

### 10.9 delete_family_user関数 <a id="109-delete_family_user関数"></a>
```python
def delete_family_user(self, parent_user_id, family_user_id=None, family_slot=None):
    """家族ユーザーを削除し、親ユーザーの家族IDを更新

    Args:
        parent_user_id: 親ユーザーID
        family_user_id: 家族ユーザーID（優先）
        family_slot: family_id1-3の位置（1, 2, 3）
    """
    # データベースロック対策：複数の短いトランザクションに分割
    try:
        # ステップ1: 家族ユーザーを削除
        success = self._delete_family_user_record(parent_user_id, family_user_id, family_slot)
        if not success:
            return False

        # ステップ2: 親ユーザーの家族IDを更新（別の接続で）
        success = self._update_parent_family_ids(parent_user_id)
        return success

    except Exception as e:
        print(f"ERROR: Exception occurred during family user deletion: {e}")
        print(f"ERROR: Exception type: {type(e)}")
        import traceback

        print(f"ERROR: Traceback: {traceback.format_exc()}")
        return False
```

**説明:**
- **複雑な削除処理**: 家族ユーザー削除と親ユーザー更新を組み合わせ
- **ロック回避**: 複数の短いトランザクションに分割
- **エラーハンドリング**: 詳細なエラーログ出力
- **柔軟な削除**: family_user_idまたはfamily_slotで指定可能

### 10.10 _delete_family_user_record関数 <a id="1010-delete_family_user_record関数"></a>
```python
def _delete_family_user_record(self, parent_user_id, family_user_id=None, family_slot=None):
    """家族ユーザーレコードを削除（短いトランザクション）"""
    conn = self.get_connection()
    cursor = conn.cursor()

    try:
        # デバッグ情報を出力
        print(f"DEBUG: _delete_family_user_record called with parent_user_id={parent_user_id}, family_user_id={family_user_id}, family_slot={family_slot}")

        # 削除対象の家族ユーザーを特定
        if family_user_id:
            # family_user_idが指定されている場合
            print(f"DEBUG: Method 1 - Deleting with family_user_id='{family_user_id}'")
            cursor.execute(
                "DELETE FROM family_users WHERE family_user_id = ? AND parent_user_id = ?",
                (family_user_id, parent_user_id),
            )
            print(f"DEBUG: Method 1 result: rowcount={cursor.rowcount}")
        elif family_slot and 1 <= family_slot <= 3:
            # family_slotが指定されている場合（family_user_idが空の場合）
            print(f"DEBUG: Method 2 - Using family_slot={family_slot}")
            # 複雑な削除ロジック...
            
        print(f"DEBUG: DELETE query executed, rowcount={cursor.rowcount}")

        if cursor.rowcount == 0:
            conn.close()
            return False  # 削除対象が見つからない

        conn.commit()
        return True

    except Exception as e:
        conn.rollback()
        print(f"ERROR: Exception in _delete_family_user_record: {e}")
        return False
    finally:
        conn.close()
```

**説明:**
- **詳細なデバッグ**: 削除プロセスの詳細ログ
- **複数削除方法**: family_user_idまたはfamily_slotでの削除
- **エラー処理**: rollbackとエラーログ
- **安全な削除**: 親ユーザーとの関連付けを確認

### 10.11 _update_parent_family_ids関数 <a id="1011-update_parent_family_ids関数"></a>
```python
def _update_parent_family_ids(self, parent_user_id):
    """親ユーザーの家族IDを更新（短いトランザクション）"""
    conn = self.get_connection()
    cursor = conn.cursor()

    try:
        print(f"DEBUG: _update_parent_family_ids called for parent_user_id={parent_user_id}")

        # 現在の家族ユーザーを取得
        family_users = self.get_family_users_by_parent(parent_user_id)
        family_ids = [None, None, None]
        for i, family_user in enumerate(family_users[:3]):
            family_ids[i] = family_user[1]  # family_user_id

        print(f"DEBUG: Updating family_ids to: {family_ids}")

        cursor.execute(
            """
            UPDATE users 
            SET family_id1 = ?, family_id2 = ?, family_id3 = ?, updated_at = CURRENT_TIMESTAMP
            WHERE user_id = ?
            """,
            (family_ids[0], family_ids[1], family_ids[2], parent_user_id),
        )

        print(f"DEBUG: UPDATE query executed, rowcount={cursor.rowcount}")
        conn.commit()
        return True

    except Exception as e:
        conn.rollback()
        print(f"ERROR: Exception in _update_parent_family_ids: {e}")
        return False
    finally:
        conn.close()
```

**説明:**
- **再構築**: 残りの家族ユーザーからfamily_idsを再構築
- **順序維持**: 配列の順序でfamily_id1-3に設定
- **デバッグログ**: 更新プロセスの詳細ログ
- **エラー処理**: rollbackとエラーログ

---

## 11. マイグレーション処理 <a id="11-マイグレーション処理"></a>

### 11.1 テーブル構造変更 <a id="111-テーブル構造変更"></a>
```python
# 既存のprofilesテーブルにfamily_livingカラムを追加（マイグレーション）
try:
    cursor.execute("ALTER TABLE profiles ADD COLUMN family_living TEXT")
    print("Added family_living column to profiles table")
except sqlite3.OperationalError:
    # カラムが既に存在する場合はエラーを無視
    pass

# 既存のusersテーブルからfamily_livingカラムを削除（マイグレーション）
try:
    # SQLiteではカラムの直接削除ができないため、新しいテーブルを作成してデータを移行
    cursor.execute(
        """
        CREATE TABLE users_new AS 
        SELECT id, user_id, email, password, user_type, name, furigana, nickname, 
               gender, birth_date, family_id1, family_id2, family_id3, 
               created_at, updated_at 
        FROM users
    """
    )
    cursor.execute("DROP TABLE users")
    cursor.execute("ALTER TABLE users_new RENAME TO users")
    print("Removed family_living column from users table")
except sqlite3.OperationalError as e:
    # エラーが発生した場合は無視（カラムが存在しない場合など）
    print(f"Migration skipped: {e}")
```

**説明:**
- **カラム追加**: profilesテーブルにfamily_livingカラムを追加
- **カラム削除**: usersテーブルからfamily_livingカラムを削除
- **SQLite制限**: 直接削除できないためテーブル再作成
- **エラー処理**: 既存の場合はスキップ

---

## まとめ

config.pyは「私の望む暮らし」アプリケーションのデータ層を担当する重要なファイルです。

### 主要機能
1. **ユーザー管理**: 本人・家族ユーザーの登録・認証・管理
2. **プロフィール管理**: 詳細な個人情報と家族構成の管理
3. **暮らし情報管理**: IWLM（I Want to Live My life）の包括的なデータ管理
4. **日記管理**: 写真付き日記の作成・編集・削除
5. **目標管理**: AI連携による個人化された目標生成と履歴管理
6. **家族管理**: 招待コードシステムによる家族登録と管理
7. **招待システム**: 8桁コードによる安全な家族招待

### 技術的特徴
- **SQLite**: 軽量で高性能なデータベース
- **WALモード**: 同時アクセス性能の向上
- **トランザクション管理**: 適切なコミット・ロールバック処理
- **エラーハンドリング**: 詳細なエラーログと例外処理
- **マイグレーション**: データベース構造変更の自動処理
- **セキュリティ**: パラメータ化クエリによるSQLインジェクション対策

### データ設計
- **正規化**: 適切なテーブル分割と外部キー制約
- **制約**: CHECK制約によるデータ整合性
- **インデックス**: ユニーク制約による重複防止
- **履歴管理**: 目標の履歴保存機能

このファイルは、アプリケーションの全機能を支える堅牢なデータ層を提供しています。
