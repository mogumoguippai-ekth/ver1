# app.py コード解説

## 概要
「私の望む暮らし」アプリケーションのメインアプリケーションファイル。Flaskフレームワークを使用してWebアプリケーションを構築し、本人ユーザーと家族ユーザーの両方をサポートする日記・プロフィール・目標管理システムを提供します。

---

## 📋 目次

### 1. インポート・初期設定
- [1.1 必要なライブラリ](#11-必要なライブラリ)

### 2. アプリケーション設定
- [2.1 Flask設定](#21-flask設定)
- [2.2 ファイルアップロード設定](#22-ファイルアップロード設定)

### 3. ユーティリティ関数
- [3.1 ファイル処理関数](#31-ファイル処理関数)
- [3.2 画像処理関数](#32-画像処理関数)

### 4. デコレーター
- [4.1 login_required](#41-login_required)
- [4.2 self_user_required](#42-self_user_required)

### 5. 認証・登録機能
- [5.1 ログイン機能](#51-ログイン機能)
- [5.2 会員登録機能](#52-会員登録機能)
- [5.3 ログアウト機能](#53-ログアウト機能)

### 6. ユーザー管理機能
- [6.1 ユーザー情報更新](#61-ユーザー情報更新)
- [6.2 パスワード変更](#62-パスワード変更)

### 7. プロフィール管理機能
- [7.1 プロフィール表示](#71-プロフィール表示)
- [7.2 プロフィール更新](#72-プロフィール更新)

### 8. 暮らし情報（IWLM）管理
- [8.1 IWLM表示](#81-iwlm表示)
- [8.2 IWLM更新](#82-iwlm更新)

### 9. 目標管理機能
- [9.1 目標表示](#91-目標表示)
- [9.2 目標生成](#92-目標生成)
- [9.3 目標履歴](#93-目標履歴)

### 10. 日記管理機能
- [10.1 日記カレンダー](#101-日記カレンダー)
- [10.2 日記一覧](#102-日記一覧)
- [10.3 日記作成・更新](#103-日記作成更新)
- [10.4 日記削除](#104-日記削除)

### 11. 印刷機能
- [11.1 プロフィール印刷](#111-プロフィール印刷)
- [11.2 IWLM印刷](#112-iwlm印刷)
- [11.3 目標印刷](#113-目標印刷)

### 12. ページ表示機能
- [12.1 ダッシュボード](#121-ダッシュボード)
- [12.2 各種ページ表示](#122-各種ページ表示)

### 13. API機能
- [13.1 招待コード生成](#131-招待コード生成)
- [13.2 家族ユーザー管理](#132-家族ユーザー管理)

### 14. データベース初期化
- [14.1 アプリケーション起動](#141-アプリケーション起動)

---

## 1. インポート・初期設定 <a id="1-インポート初期設定"></a>

```python
from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    session,
    flash,
    jsonify,
)
from config import db
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
from werkzeug.utils import secure_filename
from PIL import Image
import os
from datetime import datetime
from ai_goal_service import AIGoalService
```

**説明:**
- **Flask関連**: Webフレームワークの基本機能
- **config.db**: データベース操作クラス
- **werkzeug.security**: パスワードハッシュ化・検証
- **PIL**: 画像処理（リサイズ・サムネイル作成）
- **ai_goal_service**: AI目標生成サービス

## 2. アプリケーション設定 <a id="2-アプリケーション設定"></a>

```python
app = Flask(__name__)
app.secret_key = "your-secret-key-here-change-in-production"
ai_goal_service = AIGoalService()

# ファイルアップロード設定
UPLOAD_FOLDER = "static/uploads"
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif"}
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["MAX_CONTENT_LENGTH"] = 16 * 1024 * 1024  # 16MB max file size
```

**説明:**
- Flaskアプリケーションインスタンスの作成
- セッション管理用の秘密鍵設定
- AI目標生成サービスの初期化
- ファイルアップロードの設定（対応形式・サイズ制限）

## 3. ユーティリティ関数 <a id="3-ユーティリティ関数"></a>

### ファイル処理関数

```python
def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

def resize_image(image_path, output_path, max_width=1200, max_height=800):
    """画像をリサイズ"""
    with Image.open(image_path) as img:
        img.thumbnail((max_width, max_height), Image.Resampling.LANCZOS)
        img.save(output_path, optimize=True, quality=85)

def create_thumbnail(image_path, output_path, size=(200, 150)):
    """サムネイル画像を作成"""
    with Image.open(image_path) as img:
        img.thumbnail(size, Image.Resampling.LANCZOS)
        img.save(output_path, optimize=True, quality=85)

def remove_exif_data(image_path):
    """画像からEXIFデータ（位置情報など）を削除"""
```

**説明:**
- **allowed_file**: アップロード可能なファイル形式をチェック
- **resize_image**: 画像を指定サイズにリサイズ
- **create_thumbnail**: サムネイル画像を生成
- **remove_exif_data**: プライバシー保護のためEXIFデータを削除

## 4. デコレーター <a id="4-デコレーター"></a>

### ログイン必須デコレーター

```python
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "user_id" not in session:
            return redirect(url_for("index"))
        return f(*args, **kwargs)
    return decorated_function
```

**説明:**
- ログインしていないユーザーをログインページにリダイレクト
- セッションに`user_id`が存在するかチェック

### 本人ユーザー限定デコレーター

```python
def self_user_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "user_id" not in session:
            return redirect(url_for("index"))
        if session.get("user_type") != "self":
            flash("この機能は本人ユーザーのみ利用できます。")
            return redirect(url_for("dashboard"))
        return f(*args, **kwargs)
    return decorated_function
```

**説明:**
- 本人ユーザーのみアクセス可能な機能を保護
- 家族ユーザーがアクセスした場合はダッシュボードにリダイレクト

## 5. 認証・登録機能 <a id="5-認証登録機能"></a>

### トップページ

```python
@app.route("/")
def index():
    # すでにログイン済みの場合はダッシュボードへ
    if "user_id" in session:
        return redirect(url_for("dashboard"))
    return render_template("index.html")
```

**説明:**
- ログイン状態をチェック
- ログイン済みの場合はダッシュボードにリダイレクト
- 未ログインの場合はログインページを表示

### ユーザー登録

```python
@app.route("/register", methods=["POST"])
def register():
    user_id = request.form.get("register-username")
    email = request.form.get("register-email")
    password = request.form.get("register-password")
    user_type = request.form.get("user-type", "self")
    invitation_code = request.form.get("invitation-code")

    # 家族登録の場合は招待コードが必要
    if user_type == "family":
        # 招待コードの有効性をチェック
        is_valid, parent_user_id = db.validate_invitation_code(invitation_code)
        if not is_valid:
            flash("無効な招待コードです。")
            return redirect(url_for("index"))

        # 家族ユーザーを作成
        hashed_password = generate_password_hash(password)
        family_data = {
            "family_user_id": user_id,
            "email": email,
            "password": hashed_password,
            "parent_user_id": parent_user_id,
            "invitation_code": invitation_code,
        }
        # ... 家族ユーザー作成処理
    else:
        # 本人登録の場合
        hashed_password = generate_password_hash(password)
        user_data = {"user_id": user_id, "email": email, "password": hashed_password, "user_type": user_type}
        # ... 本人ユーザー作成処理
```

**説明:**
- **本人登録**: 通常のユーザー登録、基本情報入力案内ツールチップを表示
- **家族登録**: 招待コードが必要、親ユーザーとの関連付け
- パスワードハッシュ化、重複チェック、エラーハンドリング

### ログイン

```python
@app.route("/login", methods=["POST"])
def login():
    user_id = request.form.get("login-id")
    password = request.form.get("login-password")

    # まず本人ユーザーをチェック
    user = db.get_user_by_id(user_id)
    if user and check_password_hash(user[3], password):
        session["user_id"] = user[1]
        session["email"] = user[2]
        session["nickname"] = user[7] if user[7] else user[1]
        session["user_type"] = "self"
        return redirect(url_for("dashboard"))

    # 家族ユーザーをチェック
    family_user = db.get_family_user_by_id(user_id)
    if family_user and check_password_hash(family_user[3], password):
        session["user_id"] = family_user[1]
        session["email"] = family_user[2]
        session["nickname"] = family_user[1]
        session["user_type"] = "family"
        session["parent_user_id"] = family_user[4]
        return redirect(url_for("dashboard"))
```

**説明:**
- 本人ユーザーと家族ユーザーの両方をチェック
- パスワードハッシュの検証
- セッション情報の設定（ユーザーID、メール、ニックネーム、ユーザータイプ）

## 6. ユーザー管理機能 <a id="6-ユーザー管理機能"></a>

### 招待コード生成

```python
@app.route("/generate_invitation_code", methods=["POST"])
@login_required
def generate_invitation_code():
    """招待コードを生成"""
    user_id = session["user_id"]

    # 本人ユーザーのみ招待コードを発行可能
    if session.get("user_type") != "self":
        return jsonify({"success": False, "error": "招待コードは本人ユーザーのみ発行できます。"})

    # 家族登録可能数をチェック
    next_slot = db.get_next_family_slot(user_id)
    if next_slot is None:
        return jsonify({"success": False, "error": "家族登録は3人までです。"})

    try:
        code, expires_at = db.generate_invitation_code(user_id)
        return jsonify(
            {"success": True, "code": code, "expires_at": expires_at.strftime("%Y-%m-%d %H:%M:%S")}
        )
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})
```

**説明:**
- 本人ユーザーのみ招待コード発行可能
- 家族登録は最大3人まで
- 8桁の数字コード生成、有効期限設定

### 家族ユーザー削除

```python
@app.route("/delete_family_user", methods=["POST"])
@self_user_required
def delete_family_user():
    """家族ユーザーを削除"""
    try:
        user_id = session["user_id"]
        data = request.get_json()
        family_user_id = data.get("family_user_id")
        family_slot = data.get("family_slot")

        # 家族ユーザーを削除
        success = db.delete_family_user(user_id, family_user_id, family_slot)

        if success:
            return jsonify({"success": True, "message": "家族ユーザーを削除しました"})
        else:
            return jsonify({"success": False, "error": "家族ユーザーの削除に失敗しました"})

    except Exception as e:
        return jsonify({"success": False, "error": str(e)})
```

**説明:**
- 本人ユーザーのみ家族ユーザー削除可能
- 家族ユーザーIDまたは家族スロットで削除対象を指定
- JSONレスポンスで結果を返す

## 7. プロフィール管理機能 <a id="7-プロフィール管理機能"></a>

### 基本情報更新

```python
@app.route("/update_user", methods=["POST"])
@self_user_required
def update_user():
    # プロフィール更新
    user_id = session["user_id"]

    # 基本情報（userテーブル）
    name = request.form.get("name")
    furigana = request.form.get("furigana")
    nickname = request.form.get("nickname")
    gender = request.form.get("gender")
    birth_date = request.form.get("birth_date")

    # メール・パスワード訂正
    new_email = request.form.get("new_email")
    new_password = request.form.get("new_password")

    conn = db.get_connection()
    cursor = conn.cursor()

    # 基本情報更新
    cursor.execute(
        """
        UPDATE users
        SET name = ?, furigana = ?, nickname = ?, gender = ?, birth_date = ?, updated_at = CURRENT_TIMESTAMP
        WHERE user_id = ?
    """,
        (name, furigana, nickname, gender, birth_date, user_id),
    )

    # メール訂正
    if new_email:
        cursor.execute("UPDATE users SET email = ? WHERE user_id = ?", (new_email, user_id))
        session["email"] = new_email

    # パスワード訂正
    if new_password:
        hashed_password = generate_password_hash(new_password)
        cursor.execute("UPDATE users SET password = ? WHERE user_id = ?", (hashed_password, user_id))

    conn.commit()
    conn.close()

    # ニックネーム更新
    if nickname:
        session["nickname"] = nickname

    # 基本情報入力案内ツールチップを非表示にする
    if "show_basic_info_tooltip" in session:
        del session["show_basic_info_tooltip"]

    flash("基本情報を更新しました。")
    return redirect(url_for("profile"))
```

**説明:**
- 本人ユーザーのみ基本情報更新可能
- 名前、フリガナ、ニックネーム、性別、生年月日を更新
- メールアドレス・パスワードの変更も対応
- 基本情報更新後にツールチップを非表示

### 詳細プロフィール更新

```python
@app.route("/update_profile", methods=["POST"])
@self_user_required
def update_profile():
    # プロフィール詳細情報更新
    user_id = session["user_id"]

    profile_data = {
        "home": request.form.get("home"),
        "spouse": request.form.get("spouse"),
        "children_living": request.form.get("children_living"),
        "children_separate": request.form.get("children_separate"),
        "family_living": request.form.get("family_living"),
        "treated_illness": request.form.get("Treated-illness"),
        "under_treatment": request.form.get("under-treatment"),
        "medical_facilities": request.form.get("receiving-treatment"),
        "most_relied_family": request.form.get("most-relied-upon-family"),
        "trusted_neighbor": request.form.get("trusted-neighbor"),
        "consulted_friend": request.form.get("consulted-friend"),
        "money_sources": ",".join(request.form.getlist("money")),  # チェックボックスは複数選択
    }

    # プロフィール情報を保存
    db.create_or_update_profile(user_id, profile_data)

    flash("私について 詳細を更新しました。")
    return redirect(url_for("profile"))
```

**説明:**
- 家族構成、医療情報、支援体制などの詳細情報を更新
- チェックボックス項目は複数選択に対応
- データベースのcreate_or_update_profileメソッドを使用

## 8. 暮らし情報（IWLM）管理 <a id="8-暮らし情報iwlm管理"></a>

### IWLM情報更新

```python
@app.route("/update_iwlm", methods=["POST"])
@self_user_required
def update_iwlm():
    # IWLM情報更新
    user_id = session["user_id"]

    # IWLM詳細情報
    iwlm_data = {
        "meal_frequency": request.form.get("mealFrequency"),
        "morning_meal_type": request.form.get("morning-mealType"),
        "lunch_meal_type": request.form.get("lunch-mealType"),
        "dinner_meal_type": request.form.get("dinner-mealType"),
        "snac": request.form.get("snac"),
        "habits_alc_smoke": request.form.get("habitsAlcSmoke"),
        "wakeup_time": request.form.get("wakeupTime"),
        "bedtime": request.form.get("bedtime"),
        "daily_chores": request.form.get("dailyChores"),
        "free_times": request.form.get("freeTimes"),
        "people_met": request.form.get("peopleMet"),
        "toilet_style": request.form.get("toiletStyle"),
        "bathing_habits": request.form.get("bathingHabits"),
        "grooming_habits": request.form.get("groomingHabits"),
        "haircut_salon": request.form.get("haircutSalon"),
        "favorite_color": request.form.get("favoriteColor"),
        "favorite_clothing": request.form.get("favoriteClothing"),
        "favorite_footwear": request.form.get("favoriteFootwear"),
        "favorite_music": request.form.get("favoriteMusic"),
        "favorite_tv_radio": request.form.get("favoriteTvRadio"),
        "leisure_activities": request.form.get("leisureActivities"),
        "favorite_place": request.form.get("favoritePlace"),
        "job_status": request.form.get("jobStatus"),
        "interests": request.form.get("interests"),
        "strengths_and_weaknesses": request.form.get("strengthsAndWeaknesses"),
        "characteristics": request.form.get("characteristics"),
        "others": request.form.get("others"),
        "keep_doing": ",".join(request.form.getlist("keepDoing")),
        "keep_doing_other": request.form.get("keep_doing_other"),
        "future_activities": ",".join(request.form.getlist("futureActivities")),
        "future_activities_other": request.form.get("future_activities_other"),
        "residence_type": ",".join(request.form.getlist("residenceType")),
        "residence_type_other": request.form.get("residence_type_other"),
        "anxiety_and_sadness": ",".join(request.form.getlist("anxietyAndSadness")),
        "anxiety_and_sadness_other": request.form.get("anxiety_and_sadness_other"),
        "areas_of_support": ",".join(request.form.getlist("areasOfSupport")),
        "areas_of_support_other": request.form.get("areas_of_support_other"),
        "future_care_plan": ",".join(request.form.getlist("futureCarePlan")),
        "future_care_plan_other": request.form.get("future_care_plan_other"),
    }

    # IWLM情報を保存
    db.create_or_update_iwlm(user_id, iwlm_data)

    flash("私の暮らし情報を更新しました。")
    return redirect(url_for("iwlm_table"))
```

**説明:**
- 食事、睡眠、趣味、性格、将来計画などの詳細な暮らし情報を管理
- 複数選択項目はカンマ区切りで保存
- 「その他」項目も対応

## 9. 目標管理機能 <a id="9-目標管理機能"></a>

### 目標表示

```python
@app.route("/goals")
@login_required
def goals():
    if session.get("user_type") == "family":
        # 家族ユーザーの場合は親ユーザーの情報を取得
        parent_user_id = session.get("parent_user_id")
        user_id = parent_user_id
    else:
        # 本人ユーザーの場合
        user_id = session["user_id"]

    # 更新後のリダイレクトかどうかチェック
    updated = request.args.get("updated", False)

    # 最新の保存された目標を取得
    latest_goals = db.get_latest_user_goals(user_id)

    # データ変更の確認が必要かチェック（更新後はFalseにする）
    data_changed = False if updated else db.has_data_changed(user_id)
    needs_update = db.should_update_goals(user_id)

    # 目標が存在しないか、90日以上経過している場合は新規生成
    if not latest_goals or needs_update:
        # 家族ユーザーまたはデータ変更がない場合はAI動作を無効化
        if session.get("user_type") == "family":
            # 家族ユーザーの場合は既存の目標がない場合はフォールバックを使用
            if not latest_goals:
                goals_data = db.analyze_user_goals(user_id)
                saved_id = db.save_user_goals_check(user_id, goals_data)
                is_new_goals = saved_id is not None
            else:
                # 既存の目標を使用
                goals_data = {"long_term_goal": latest_goals[2], "short_term_goals": latest_goals[3]}
                is_new_goals = False
        elif not data_changed:
            # 本人ユーザーでデータ変更がない場合はAI動作を無効化
            if not latest_goals:
                goals_data = db.analyze_user_goals(user_id)
                saved_id = db.save_user_goals_check(user_id, goals_data)
                is_new_goals = saved_id is not None
            else:
                # 既存の目標を使用
                goals_data = {"long_term_goal": latest_goals[2], "short_term_goals": latest_goals[3]}
                is_new_goals = False
        else:
            # 本人ユーザーでデータ変更がある場合のみAIサービスを使用
            try:
                # ユーザー情報を取得
                user_data = db.get_user_by_id(user_id)
                profile_data = db.get_profile_by_user_id(user_id)
                iwlm_data = db.get_iwlm_by_user_id(user_id)

                # AI目標生成サービスを使用
                goals_data = ai_goal_service.generate_goals(
                    user_data={"name": user_data[5]}
                )

            except Exception as e:
                print(f"AI目標生成に失敗しました: {e}")
                # フォールバック: 従来の固定ロジックで目標を生成
                goals_data = db.analyze_user_goals(user_id)

            # データ変更があった場合は強制保存、そうでなければ重複チェック付き保存
            if data_changed:
                saved_id = db.save_user_goals_forced(user_id, goals_data)
                is_new_goals = True
            else:
                saved_id = db.save_user_goals_check(user_id, goals_data)
                is_new_goals = saved_id is not None
    else:
        # 保存された目標を使用
        goals_data = {"long_term_goal": latest_goals[2], "short_term_goals": latest_goals[3]}
        is_new_goals = False

    # ユーザー情報も取得（表示用）
    user_data = db.get_user_by_id(user_id)

    return render_template(
        "goals.html",
        goals=goals_data,
        user=user_data,
        is_new_goals=is_new_goals,
        goals_created_at=latest_goals[5] if latest_goals else None,
        data_changed=data_changed,
    )
```

**説明:**
- **本人ユーザー**: AIサービスを使用してパーソナライズされた目標を生成
- **家族ユーザー**: 親ユーザーの目標を閲覧のみ
- **データ変更検知**: プロフィールやIWLM情報の変更を検知して目標更新を促す
- **フォールバック機能**: AI生成に失敗した場合は従来のロジックを使用
- **90日ルール**: 目標は90日ごとに自動更新

### 目標更新

```python
@app.route("/goals/update", methods=["POST"])
@self_user_required
def update_goals():
    """目標を手動で更新"""
    user_id = session["user_id"]

    # データ変更があったかチェック
    data_changed = db.has_data_changed(user_id)

    # AIサービスを使用して目標を生成
    try:
        # ユーザー情報を取得
        user_data = db.get_user_by_id(user_id)
        profile_data = db.get_profile_by_user_id(user_id)
        iwlm_data = db.get_iwlm_by_user_id(user_id)

        # AI目標生成サービスを使用
        goals_data = ai_goal_service.generate_goals(
            user_data=user_data, profile_data=profile_data, iwlm_data=iwlm_data, user_id=user_id
        )
    except Exception as e:
        print(f"AI目標生成に失敗しました: {e}")
        # フォールバック: 従来の固定ロジックで目標を生成
        goals_data = db.analyze_user_goals(user_id)

    # データ変更があった場合は強制保存、そうでなければ重複チェック付き保存
    if data_changed:
        saved_id = db.save_user_goals_forced(user_id, goals_data)
        flash("目標を更新しました。")
        return redirect(url_for("goals", updated=True))
    else:
        # 通常の保存（重複チェック付き）
        saved_id = db.save_user_goals_check(user_id, goals_data)

        if saved_id is not None:
            flash("目標を更新しました。")
            return redirect(url_for("goals", updated=True))
        else:
            flash("目標に変更がありませんでした。")
            return redirect(url_for("goals"))
```

**説明:**
- 本人ユーザーのみ手動目標更新可能
- AIサービスを使用してパーソナライズされた目標を生成
- データ変更状況に応じて保存方法を変更
- 重複チェック機能付き

## 10. 日記管理機能 <a id="10-日記管理機能"></a>

### 日記保存

```python
@app.route("/save-diary", methods=["POST"])
@self_user_required
def save_diary():
    try:
        user_id = session["user_id"]
        diary_date = request.form.get("date")
        title = request.form.get("title", "")
        content = request.form.get("content", "")

        # 文字数チェック
        if len(content) > 200:
            return jsonify({"success": False, "error": "日記は200文字以内で入力してください。"})

        photo_path = None
        thumbnail_path = None

        # 写真アップロード処理
        if "photo" in request.files:
            file = request.files["photo"]
            if file and file.filename and allowed_file(file.filename):
                filename = secure_filename(f"{user_id}_{diary_date}_{file.filename}")

                # 元画像保存
                photo_dir = os.path.join(app.config["UPLOAD_FOLDER"], "diary_photos")
                os.makedirs(photo_dir, exist_ok=True)
                photo_path = os.path.join(photo_dir, filename)
                file.save(photo_path)

                # EXIFデータ（位置情報など）を削除
                remove_exif_data(photo_path)

                # リサイズ
                resize_image(photo_path, photo_path, 1200, 800)

                # サムネイル作成
                thumbnail_dir = os.path.join(app.config["UPLOAD_FOLDER"], "diary_thumbnails")
                os.makedirs(thumbnail_dir, exist_ok=True)
                thumbnail_filename = f"thumb_{filename}"
                thumbnail_path = os.path.join(thumbnail_dir, thumbnail_filename)
                create_thumbnail(photo_path, thumbnail_path)

                # パスを相対パスに変換
                photo_path = f"/static/uploads/diary_photos/{filename}"
                thumbnail_path = f"/static/uploads/diary_thumbnails/{thumbnail_filename}"

        # データベースに保存
        db.create_or_update_diary(user_id, diary_date, title, content, photo_path, thumbnail_path)

        return jsonify({"success": True})

    except Exception as e:
        return jsonify({"success": False, "error": str(e)})
```

**説明:**
- 本人ユーザーのみ日記作成・編集可能
- 文字数制限（200文字）
- 写真アップロード機能（リサイズ・サムネイル作成・EXIF削除）
- JSONレスポンスで結果を返す

### 日記削除

```python
@app.route("/delete-diary", methods=["POST"])
@self_user_required
def delete_diary():
    try:
        user_id = session["user_id"]
        data = request.get_json()
        diary_date = data.get("date")

        # 既存の写真ファイルを削除
        diary = db.get_diary_by_date(user_id, diary_date)
        if diary and diary[5]:  # photo_path
            photo_path = diary[5].replace("/static/", "static/")
            if os.path.exists(photo_path):
                os.remove(photo_path)

        if diary and diary[6]:  # thumbnail_path
            thumbnail_path = diary[6].replace("/static/", "static/")
            if os.path.exists(thumbnail_path):
                os.remove(thumbnail_path)

        # データベースから削除
        db.delete_diary(user_id, diary_date)

        return jsonify({"success": True})

    except Exception as e:
        return jsonify({"success": False, "error": str(e)})
```

**説明:**
- 本人ユーザーのみ日記削除可能
- 関連する写真ファイルも同時に削除
- データベースとファイルシステムの両方から削除

## 11. 印刷機能 <a id="11-印刷機能"></a>

### 印刷専用ページ

```python
@app.route("/print/<content_type>")
@login_required
def print_content(content_type):
    """印刷専用ページ"""
    if content_type == "profile":
        # プロフィール印刷用
        if session.get("user_type") == "family":
            parent_user_id = session.get("parent_user_id")
            user_data = db.get_user_by_id(parent_user_id)
            profile_data = db.get_profile_by_user_id(parent_user_id)
        else:
            user_data = db.get_user_by_id(session["user_id"])
            profile_data = db.get_profile_by_user_id(session["user_id"])

        return render_template("print_profile.html", user=user_data, profile=profile_data)

    elif content_type == "goals":
        # 目標印刷用
        if session.get("user_type") == "family":
            parent_user_id = session.get("parent_user_id")
            user_id = parent_user_id
        else:
            user_id = session["user_id"]

        # 最新の目標を取得
        latest_goals = db.get_latest_user_goals(user_id)
        user_data = db.get_user_by_id(user_id)

        if latest_goals:
            goals_data = {"long_term_goal": latest_goals[2], "short_term_goals": latest_goals[3]}
        else:
            goals_data = {"long_term_goal": "目標が設定されていません", "short_term_goals": []}

        return render_template("print_goals.html", goals=goals_data, user=user_data)

    elif content_type == "iwlm":
        # 暮らし情報印刷用
        if session.get("user_type") == "family":
            parent_user_id = session.get("parent_user_id")
            user_data = db.get_user_by_id(parent_user_id)
            iwlm_data = db.get_iwlm_by_user_id(parent_user_id)
        else:
            user_data = db.get_user_by_id(session["user_id"])
            iwlm_data = db.get_iwlm_by_user_id(session["user_id"])

        return render_template("print_iwlm.html", user=user_data, iwlm=iwlm_data)
```

**説明:**
- プロフィール、目標、暮らし情報の印刷専用ページ
- 家族ユーザーは親ユーザーの情報を印刷
- 印刷用の専用テンプレートを使用

## 12. ページ表示機能 <a id="12-ページ表示機能"></a>

### ダッシュボード

```python
@app.route("/dashboard")
@login_required
def dashboard():
    return render_template("dashboard.html")
```

**説明:**
- ログイン後のメインページ
- 本人・家族ユーザー共通のエントリーポイント

### プロフィールページ

```python
@app.route("/profile")
@login_required
def profile():
    # ユーザー基本情報を取得
    if session.get("user_type") == "family":
        # 家族ユーザーの場合は親ユーザーの情報を取得
        parent_user_id = session.get("parent_user_id")
        user_data = db.get_user_by_id(parent_user_id)
        profile_data = db.get_profile_by_user_id(parent_user_id)
    else:
        # 本人ユーザーの場合
        user_data = db.get_user_by_id(session["user_id"])
        profile_data = db.get_profile_by_user_id(session["user_id"])

    return render_template("profile.html", user=user_data, profile=profile_data)
```

**説明:**
- 本人ユーザー：自分のプロフィールを編集可能
- 家族ユーザー：親ユーザーのプロフィールを閲覧のみ

### 日記カレンダー

```python
@app.route("/diary_calendar")
@login_required
def diary_calendar():
    # 現在の年月を取得
    now = datetime.now()
    current_year = now.year
    current_month = now.month

    # 今月の日記がある日付とタイトルを取得
    if session.get("user_type") == "family":
        # 家族ユーザーの場合は親ユーザーの情報を取得
        parent_user_id = session.get("parent_user_id")
        diary_entries = db.get_diary_dates_with_entries(parent_user_id, current_year, current_month)
    else:
        # 本人ユーザーの場合
        diary_entries = db.get_diary_dates_with_entries(session["user_id"], current_year, current_month)

    return render_template(
        "diary_calender.html",
        current_year=current_year,
        current_month=current_month,
        diary_entries=diary_entries,
    )
```

**説明:**
- カレンダー形式で日記を表示
- 本人ユーザー：日記作成・編集可能
- 家族ユーザー：親ユーザーの日記を閲覧のみ

## 13. API機能 <a id="13-api機能"></a>

### 日記API

```python
@app.route("/api/diary/<diary_date>")
@login_required
def get_diary_by_date_api(diary_date):
    if session.get("user_type") == "family":
        # 家族ユーザーの場合は親ユーザーの情報を取得
        parent_user_id = session.get("parent_user_id")
        diary = db.get_diary_by_date(parent_user_id, diary_date)
    else:
        # 本人ユーザーの場合
        diary = db.get_diary_by_date(session["user_id"], diary_date)
    return jsonify({"diary": diary})

@app.route("/api/diary-dates/<int:year>/<int:month>")
@login_required
def get_diary_dates_api(year, month):
    if session.get("user_type") == "family":
        # 家族ユーザーの場合は親ユーザーの情報を取得
        parent_user_id = session.get("parent_user_id")
        diary_entries = db.get_diary_dates_with_entries(parent_user_id, year, month)
    else:
        # 本人ユーザーの場合
        diary_entries = db.get_diary_dates_with_entries(session["user_id"], year, month)
    return jsonify({"diary_entries": diary_entries})
```

**説明:**
- AJAX通信用のAPIエンドポイント
- 特定日付の日記取得
- 月単位の日記エントリ一覧取得
- JSON形式でレスポンス

## 14. データベース初期化 <a id="14-データベース初期化"></a>

```python
@app.route("/init_db")
def init_database():
    """データベース初期化（開発用）"""
    try:
        db.init_db()
        return "Database initialized successfully"
    except Exception as e:
        return f"Database initialization failed: {str(e)}"

if __name__ == "__main__":
    db.init_db()
    app.run(debug=True)
```

**説明:**
- 開発用のデータベース初期化エンドポイント
- アプリケーション起動時に自動でデータベースを初期化
- デバッグモードで起動

## まとめ

このアプリケーションは、本人ユーザーと家族ユーザーの両方をサポートする包括的なライフスタイル管理システムです。主要な機能は以下の通りです：

1. **認証システム**: 本人・家族ユーザーの登録・ログイン
2. **プロフィール管理**: 基本情報・詳細情報の管理
3. **暮らし情報管理**: IWLM（I Want to Live My life）情報の管理
4. **目標管理**: AIを活用したパーソナライズされた目標生成
5. **日記機能**: 写真付き日記の作成・管理
6. **家族機能**: 招待コードによる家族ユーザー登録
7. **印刷機能**: 各種情報の印刷対応
8. **セキュリティ**: パスワードハッシュ化、EXIFデータ削除、アクセス制御

家族ユーザーは閲覧のみ、本人ユーザーは編集権限を持つという適切な権限分離が実装されています。

```python
from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    session,
    flash,
    jsonify,
)
from config import db
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
from werkzeug.utils import secure_filename
from PIL import Image
import os
from datetime import datetime
from ai_goal_service import AIGoalService
```

```python
app = Flask(__name__)
app.secret_key = "your-secret-key-here-change-in-production"
ai_goal_service = AIGoalService()

# ファイルアップロード設定
UPLOAD_FOLDER = "static/uploads"
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif"}
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["MAX_CONTENT_LENGTH"] = 16 * 1024 * 1024  # 16MB max file size
```

```python
def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

def resize_image(image_path, output_path, max_width=1200, max_height=800):
    """画像をリサイズ"""
    with Image.open(image_path) as img:
        img.thumbnail((max_width, max_height), Image.Resampling.LANCZOS)
        img.save(output_path, optimize=True, quality=85)

def create_thumbnail(image_path, output_path, size=(200, 150)):
    """サムネイル画像を作成"""
    with Image.open(image_path) as img:
        img.thumbnail(size, Image.Resampling.LANCZOS)
        img.save(output_path, optimize=True, quality=85)

def remove_exif_data(image_path):
    """画像からEXIFデータ（位置情報など）を削除"""
```

```python
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "user_id" not in session:
            return redirect(url_for("index"))
        return f(*args, **kwargs)
    return decorated_function
```

```python
def self_user_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "user_id" not in session:
            return redirect(url_for("index"))
        if session.get("user_type") != "self":
            flash("この機能は本人ユーザーのみ利用できます。")
            return redirect(url_for("dashboard"))
        return f(*args, **kwargs)
    return decorated_function
```

```python
@app.route("/")
def index():
    # すでにログイン済みの場合はダッシュボードへ
    if "user_id" in session:
        return redirect(url_for("dashboard"))
    return render_template("index.html")
```

```python
@app.route("/register", methods=["POST"])
def register():
    user_id = request.form.get("register-username")
    email = request.form.get("register-email")
    password = request.form.get("register-password")
    user_type = request.form.get("user-type", "self")
    invitation_code = request.form.get("invitation-code")

    # 家族登録の場合は招待コードが必要
    if user_type == "family":
        # 招待コードの有効性をチェック
        is_valid, parent_user_id = db.validate_invitation_code(invitation_code)
        if not is_valid:
            flash("無効な招待コードです。")
            return redirect(url_for("index"))

        # 家族ユーザーを作成
        hashed_password = generate_password_hash(password)
        family_data = {
            "family_user_id": user_id,
            "email": email,
            "password": hashed_password,
            "parent_user_id": parent_user_id,
            "invitation_code": invitation_code,
        }
        # ... 家族ユーザー作成処理
    else:
        # 本人登録の場合
        hashed_password = generate_password_hash(password)
        user_data = {"user_id": user_id, "email": email, "password": hashed_password, "user_type": user_type}
        # ... 本人ユーザー作成処理
```

```python
@app.route("/login", methods=["POST"])
def login():
    user_id = request.form.get("login-id")
    password = request.form.get("login-password")

    # まず本人ユーザーをチェック
    user = db.get_user_by_id(user_id)
    if user and check_password_hash(user[3], password):
        session["user_id"] = user[1]
        session["email"] = user[2]
        session["nickname"] = user[7] if user[7] else user[1]
        session["user_type"] = "self"
        return redirect(url_for("dashboard"))

    # 家族ユーザーをチェック
    family_user = db.get_family_user_by_id(user_id)
    if family_user and check_password_hash(family_user[3], password):
        session["user_id"] = family_user[1]
        session["email"] = family_user[2]
        session["nickname"] = family_user[1]
        session["user_type"] = "family"
        session["parent_user_id"] = family_user[4]
        return redirect(url_for("dashboard"))
```

```python
@app.route("/generate_invitation_code", methods=["POST"])
@login_required
def generate_invitation_code():
    """招待コードを生成"""
    user_id = session["user_id"]

    # 本人ユーザーのみ招待コードを発行可能
    if session.get("user_type") != "self":
        return jsonify({"success": False, "error": "招待コードは本人ユーザーのみ発行できます。"})

    # 家族登録可能数をチェック
    next_slot = db.get_next_family_slot(user_id)
    if next_slot is None:
        return jsonify({"success": False, "error": "家族登録は3人までです。"})

    try:
        code, expires_at = db.generate_invitation_code(user_id)
        return jsonify(
            {"success": True, "code": code, "expires_at": expires_at.strftime("%Y-%m-%d %H:%M:%S")}
        )
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})
```

```python
@app.route("/delete_family_user", methods=["POST"])
@self_user_required
def delete_family_user():
    """家族ユーザーを削除"""
    try:
        user_id = session["user_id"]
        data = request.get_json()
        family_user_id = data.get("family_user_id")
        family_slot = data.get("family_slot")

        # 家族ユーザーを削除
        success = db.delete_family_user(user_id, family_user_id, family_slot)

        if success:
            return jsonify({"success": True, "message": "家族ユーザーを削除しました"})
        else:
            return jsonify({"success": False, "error": "家族ユーザーの削除に失敗しました"})

    except Exception as e:
        return jsonify({"success": False, "error": str(e)})
```

```python
@app.route("/update_user", methods=["POST"])
@self_user_required
def update_user():
    # プロフィール更新
    user_id = session["user_id"]

    # 基本情報（userテーブル）
    name = request.form.get("name")
    furigana = request.form.get("furigana")
    nickname = request.form.get("nickname")
    gender = request.form.get("gender")
    birth_date = request.form.get("birth_date")

    # メール・パスワード訂正
    new_email = request.form.get("new_email")
    new_password = request.form.get("new_password")

    conn = db.get_connection()
    cursor = conn.cursor()

    # 基本情報更新
    cursor.execute(
        """
        UPDATE users
        SET name = ?, furigana = ?, nickname = ?, gender = ?, birth_date = ?, updated_at = CURRENT_TIMESTAMP
        WHERE user_id = ?
    """,
        (name, furigana, nickname, gender, birth_date, user_id),
    )

    # メール訂正
    if new_email:
        cursor.execute("UPDATE users SET email = ? WHERE user_id = ?", (new_email, user_id))
        session["email"] = new_email

    # パスワード訂正
    if new_password:
        hashed_password = generate_password_hash(new_password)
        cursor.execute("UPDATE users SET password = ? WHERE user_id = ?", (hashed_password, user_id))

    conn.commit()
    conn.close()

    # ニックネーム更新
    if nickname:
        session["nickname"] = nickname

    # 基本情報入力案内ツールチップを非表示にする
    if "show_basic_info_tooltip" in session:
        del session["show_basic_info_tooltip"]

    flash("基本情報を更新しました。")
    return redirect(url_for("profile"))
```

```python
@app.route("/update_profile", methods=["POST"])
@self_user_required
def update_profile():
    # プロフィール詳細情報更新
    user_id = session["user_id"]

    profile_data = {
        "home": request.form.get("home"),
        "spouse": request.form.get("spouse"),
        "children_living": request.form.get("children_living"),
        "children_separate": request.form.get("children_separate"),
        "family_living": request.form.get("family_living"),
        "treated_illness": request.form.get("Treated-illness"),
        "under_treatment": request.form.get("under-treatment"),
        "medical_facilities": request.form.get("receiving-treatment"),
        "most_relied_family": request.form.get("most-relied-upon-family"),
        "trusted_neighbor": request.form.get("trusted-neighbor"),
        "consulted_friend": request.form.get("consulted-friend"),
        "money_sources": ",".join(request.form.getlist("money")),  # チェックボックスは複数選択
    }

    # プロフィール情報を保存
    db.create_or_update_profile(user_id, profile_data)

    flash("私について 詳細を更新しました。")
    return redirect(url_for("profile"))
```

```python
@app.route("/update_iwlm", methods=["POST"])
@self_user_required
def update_iwlm():
    # IWLM情報更新
    user_id = session["user_id"]

    # IWLM詳細情報
    iwlm_data = {
        "meal_frequency": request.form.get("mealFrequency"),
        "morning_meal_type": request.form.get("morning-mealType"),
        "lunch_meal_type": request.form.get("lunch-mealType"),
        "dinner_meal_type": request.form.get("dinner-mealType"),
        "snac": request.form.get("snac"),
        "habits_alc_smoke": request.form.get("habitsAlcSmoke"),
        "wakeup_time": request.form.get("wakeupTime"),
        "bedtime": request.form.get("bedtime"),
        "daily_chores": request.form.get("dailyChores"),
        "free_times": request.form.get("freeTimes"),
        "people_met": request.form.get("peopleMet"),
        "toilet_style": request.form.get("toiletStyle"),
        "bathing_habits": request.form.get("bathingHabits"),
        "grooming_habits": request.form.get("groomingHabits"),
        "haircut_salon": request.form.get("haircutSalon"),
        "favorite_color": request.form.get("favoriteColor"),
        "favorite_clothing": request.form.get("favoriteClothing"),
        "favorite_footwear": request.form.get("favoriteFootwear"),
        "favorite_music": request.form.get("favoriteMusic"),
        "favorite_tv_radio": request.form.get("favoriteTvRadio"),
        "leisure_activities": request.form.get("leisureActivities"),
        "favorite_place": request.form.get("favoritePlace"),
        "job_status": request.form.get("jobStatus"),
        "interests": request.form.get("interests"),
        "strengths_and_weaknesses": request.form.get("strengthsAndWeaknesses"),
        "characteristics": request.form.get("characteristics"),
        "others": request.form.get("others"),
        "keep_doing": ",".join(request.form.getlist("keepDoing")),
        "keep_doing_other": request.form.get("keep_doing_other"),
        "future_activities": ",".join(request.form.getlist("futureActivities")),
        "future_activities_other": request.form.get("future_activities_other"),
        "residence_type": ",".join(request.form.getlist("residenceType")),
        "residence_type_other": request.form.get("residence_type_other"),
        "anxiety_and_sadness": ",".join(request.form.getlist("anxietyAndSadness")),
        "anxiety_and_sadness_other": request.form.get("anxiety_and_sadness_other"),
        "areas_of_support": ",".join(request.form.getlist("areasOfSupport")),
        "areas_of_support_other": request.form.get("areas_of_support_other"),
        "future_care_plan": ",".join(request.form.getlist("futureCarePlan")),
        "future_care_plan_other": request.form.get("future_care_plan_other"),
    }

    # IWLM情報を保存
    db.create_or_update_iwlm(user_id, iwlm_data)

    flash("私の暮らし情報を更新しました。")
    return redirect(url_for("iwlm_table"))
```

```python
@app.route("/goals")
@login_required
def goals():
    if session.get("user_type") == "family":
        # 家族ユーザーの場合は親ユーザーの情報を取得
        parent_user_id = session.get("parent_user_id")
        user_id = parent_user_id
    else:
        # 本人ユーザーの場合
        user_id = session["user_id"]

    # 更新後のリダイレクトかどうかチェック
    updated = request.args.get("updated", False)

    # 最新の保存された目標を取得
    latest_goals = db.get_latest_user_goals(user_id)

    # データ変更の確認が必要かチェック（更新後はFalseにする）
    data_changed = False if updated else db.has_data_changed(user_id)
    needs_update = db.should_update_goals(user_id)

    # 目標が存在しないか、90日以上経過している場合は新規生成
    if not latest_goals or needs_update:
        # 家族ユーザーまたはデータ変更がない場合はAI動作を無効化
        if session.get("user_type") == "family":
            # 家族ユーザーの場合は既存の目標がない場合はフォールバックを使用
            if not latest_goals:
                goals_data = db.analyze_user_goals(user_id)
                saved_id = db.save_user_goals_check(user_id, goals_data)
                is_new_goals = saved_id is not None
            else:
                # 既存の目標を使用
                goals_data = {"long_term_goal": latest_goals[2], "short_term_goals": latest_goals[3]}
                is_new_goals = False
        elif not data_changed:
            # 本人ユーザーでデータ変更がない場合はAI動作を無効化
            if not latest_goals:
                goals_data = db.analyze_user_goals(user_id)
                saved_id = db.save_user_goals_check(user_id, goals_data)
                is_new_goals = saved_id is not None
            else:
                # 既存の目標を使用
                goals_data = {"long_term_goal": latest_goals[2], "short_term_goals": latest_goals[3]}
                is_new_goals = False
        else:
            # 本人ユーザーでデータ変更がある場合のみAIサービスを使用
            try:
                # ユーザー情報を取得
                user_data = db.get_user_by_id(user_id)
                profile_data = db.get_profile_by_user_id(user_id)
                iwlm_data = db.get_iwlm_by_user_id(user_id)

                # AI目標生成サービスを使用
                goals_data = ai_goal_service.generate_goals(
                    user_data={"name": user_data[5]}
                )

            except Exception as e:
                print(f"AI目標生成に失敗しました: {e}")
                # フォールバック: 従来の固定ロジックで目標を生成
                goals_data = db.analyze_user_goals(user_id)

            # データ変更があった場合は強制保存、そうでなければ重複チェック付き保存
            if data_changed:
                saved_id = db.save_user_goals_forced(user_id, goals_data)
                is_new_goals = True
            else:
                saved_id = db.save_user_goals_check(user_id, goals_data)
                is_new_goals = saved_id is not None
    else:
        # 保存された目標を使用
        goals_data = {"long_term_goal": latest_goals[2], "short_term_goals": latest_goals[3]}
        is_new_goals = False

    # ユーザー情報も取得（表示用）
    user_data = db.get_user_by_id(user_id)

    return render_template(
        "goals.html",
        goals=goals_data,
        user=user_data,
        is_new_goals=is_new_goals,
        goals_created_at=latest_goals[5] if latest_goals else None,
        data_changed=data_changed,
    )
```

```python
@app.route("/goals/update", methods=["POST"])
@self_user_required
def update_goals():
    """目標を手動で更新"""
    user_id = session["user_id"]

    # データ変更があったかチェック
    data_changed = db.has_data_changed(user_id)

    # AIサービスを使用して目標を生成
    try:
        # ユーザー情報を取得
        user_data = db.get_user_by_id(user_id)
        profile_data = db.get_profile_by_user_id(user_id)
        iwlm_data = db.get_iwlm_by_user_id(user_id)

        # AI目標生成サービスを使用
        goals_data = ai_goal_service.generate_goals(
            user_data=user_data, profile_data=profile_data, iwlm_data=iwlm_data, user_id=user_id
        )
    except Exception as e:
        print(f"AI目標生成に失敗しました: {e}")
        # フォールバック: 従来の固定ロジックで目標を生成
        goals_data = db.analyze_user_goals(user_id)

    # データ変更があった場合は強制保存、そうでなければ重複チェック付き保存
    if data_changed:
        saved_id = db.save_user_goals_forced(user_id, goals_data)
        flash("目標を更新しました。")
        return redirect(url_for("goals", updated=True))
    else:
        # 通常の保存（重複チェック付き）
        saved_id = db.save_user_goals_check(user_id, goals_data)

        if saved_id is not None:
            flash("目標を更新しました。")
            return redirect(url_for("goals", updated=True))
        else:
            flash("目標に変更がありませんでした。")
            return redirect(url_for("goals"))
```

```python
@app.route("/save-diary", methods=["POST"])
@self_user_required
def save_diary():
    try:
        user_id = session["user_id"]
        diary_date = request.form.get("date")
        title = request.form.get("title", "")
        content = request.form.get("content", "")

        # 文字数チェック
        if len(content) > 200:
            return jsonify({"success": False, "error": "日記は200文字以内で入力してください。"})

        photo_path = None
        thumbnail_path = None

        # 写真アップロード処理
        if "photo" in request.files:
            file = request.files["photo"]
            if file and file.filename and allowed_file(file.filename):
                filename = secure_filename(f"{user_id}_{diary_date}_{file.filename}")

                # 元画像保存
                photo_dir = os.path.join(app.config["UPLOAD_FOLDER"], "diary_photos")
                os.makedirs(photo_dir, exist_ok=True)
                photo_path = os.path.join(photo_dir, filename)
                file.save(photo_path)

                # EXIFデータ（位置情報など）を削除
                remove_exif_data(photo_path)

                # リサイズ
                resize_image(photo_path, photo_path, 1200, 800)

                # サムネイル作成
                thumbnail_dir = os.path.join(app.config["UPLOAD_FOLDER"], "diary_thumbnails")
                os.makedirs(thumbnail_dir, exist_ok=True)
                thumbnail_filename = f"thumb_{filename}"
                thumbnail_path = os.path.join(thumbnail_dir, thumbnail_filename)
                create_thumbnail(photo_path, thumbnail_path)

                # パスを相対パスに変換
                photo_path = f"/static/uploads/diary_photos/{filename}"
                thumbnail_path = f"/static/uploads/diary_thumbnails/{thumbnail_filename}"

        # データベースに保存
        db.create_or_update_diary(user_id, diary_date, title, content, photo_path, thumbnail_path)

        return jsonify({"success": True})

    except Exception as e:
        return jsonify({"success": False, "error": str(e)})
```

```python
@app.route("/delete-diary", methods=["POST"])
@self_user_required
def delete_diary():
    try:
        user_id = session["user_id"]
        data = request.get_json()
        diary_date = data.get("date")

        # 既存の写真ファイルを削除
        diary = db.get_diary_by_date(user_id, diary_date)
        if diary and diary[5]:  # photo_path
            photo_path = diary[5].replace("/static/", "static/")
            if os.path.exists(photo_path):
                os.remove(photo_path)

        if diary and diary[6]:  # thumbnail_path
            thumbnail_path = diary[6].replace("/static/", "static/")
            if os.path.exists(thumbnail_path):
                os.remove(thumbnail_path)

        # データベースから削除
        db.delete_diary(user_id, diary_date)

        return jsonify({"success": True})

    except Exception as e:
        return jsonify({"success": False, "error": str(e)})
```

```python
@app.route("/print/<content_type>")
@login_required
def print_content(content_type):
    """印刷専用ページ"""
    if content_type == "profile":
        # プロフィール印刷用
        if session.get("user_type") == "family":
            parent_user_id = session.get("parent_user_id")
            user_data = db.get_user_by_id(parent_user_id)
            profile_data = db.get_profile_by_user_id(parent_user_id)
        else:
            user_data = db.get_user_by_id(session["user_id"])
            profile_data = db.get_profile_by_user_id(session["user_id"])

        return render_template("print_profile.html", user=user_data, profile=profile_data)

    elif content_type == "goals":
        # 目標印刷用
        if session.get("user_type") == "family":
            parent_user_id = session.get("parent_user_id")
            user_id = parent_user_id
        else:
            user_id = session["user_id"]

        # 最新の目標を取得
        latest_goals = db.get_latest_user_goals(user_id)
        user_data = db.get_user_by_id(user_id)

        if latest_goals:
            goals_data = {"long_term_goal": latest_goals[2], "short_term_goals": latest_goals[3]}
        else:
            goals_data = {"long_term_goal": "目標が設定されていません", "short_term_goals": []}

        return render_template("print_goals.html", goals=goals_data, user=user_data)

    elif content_type == "iwlm":
        # 暮らし情報印刷用
        if session.get("user_type") == "family":
            parent_user_id = session.get("parent_user_id")
            user_data = db.get_user_by_id(parent_user_id)
            iwlm_data = db.get_iwlm_by_user_id(parent_user_id)
        else:
            user_data = db.get_user_by_id(session["user_id"])
            iwlm_data = db.get_iwlm_by_user_id(session["user_id"])

        return render_template("print_iwlm.html", user=user_data, iwlm=iwlm_data)
```

```python
@app.route("/dashboard")
@login_required
def dashboard():
    return render_template("dashboard.html")
```

```python
@app.route("/profile")
@login_required
def profile():
    # ユーザー基本情報を取得
    if session.get("user_type") == "family":
        # 家族ユーザーの場合は親ユーザーの情報を取得
        parent_user_id = session.get("parent_user_id")
        user_data = db.get_user_by_id(parent_user_id)
        profile_data = db.get_profile_by_user_id(parent_user_id)
    else:
        # 本人ユーザーの場合
        user_data = db.get_user_by_id(session["user_id"])
        profile_data = db.get_profile_by_user_id(session["user_id"])

    return render_template("profile.html", user=user_data, profile=profile_data)
```

```python
@app.route("/diary_calendar")
@login_required
def diary_calendar():
    # 現在の年月を取得
    now = datetime.now()
    current_year = now.year
    current_month = now.month

    # 今月の日記がある日付とタイトルを取得
    if session.get("user_type") == "family":
        # 家族ユーザーの場合は親ユーザーの情報を取得
        parent_user_id = session.get("parent_user_id")
        diary_entries = db.get_diary_dates_with_entries(parent_user_id, current_year, current_month)
    else:
        # 本人ユーザーの場合
        diary_entries = db.get_diary_dates_with_entries(session["user_id"], current_year, current_month)

    return render_template(
        "diary_calender.html",
        current_year=current_year,
        current_month=current_month,
        diary_entries=diary_entries,
    )
```

```python
@app.route("/api/diary/<diary_date>")
@login_required
def get_diary_by_date_api(diary_date):
    if session.get("user_type") == "family":
        # 家族ユーザーの場合は親ユーザーの情報を取得
        parent_user_id = session.get("parent_user_id")
        diary = db.get_diary_by_date(parent_user_id, diary_date)
    else:
        # 本人ユーザーの場合
        diary = db.get_diary_by_date(session["user_id"], diary_date)
    return jsonify({"diary": diary})

@app.route("/api/diary-dates/<int:year>/<int:month>")
@login_required
def get_diary_dates_api(year, month):
    if session.get("user_type") == "family":
        # 家族ユーザーの場合は親ユーザーの情報を取得
        parent_user_id = session.get("parent_user_id")
        diary_entries = db.get_diary_dates_with_entries(parent_user_id, year, month)
    else:
        # 本人ユーザーの場合
        diary_entries = db.get_diary_dates_with_entries(session["user_id"], year, month)
    return jsonify({"diary_entries": diary_entries})
```

```python
@app.route("/init_db")
def init_database():
    """データベース初期化（開発用）"""
    try:
        db.init_db()
        return "Database initialized successfully"
    except Exception as e:
        return f"Database initialization failed: {str(e)}"

if __name__ == "__main__":
    db.init_db()
    app.run(debug=True)
```

