from flask import Flask, render_template, request, redirect, url_for, session, flash
from config import db
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps

app = Flask(__name__)
app.secret_key = "your-secret-key-here-change-in-production"  # セッション用の秘密鍵


# ログイン必須デコレーター
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "user_id" not in session:
            return redirect(url_for("index"))
        return f(*args, **kwargs)

    return decorated_function


@app.route("/")
def index():
    # すでにログイン済みの場合はダッシュボードへ
    if "user_id" in session:
        return redirect(url_for("dashboard"))
    return render_template("index.html")


@app.route("/register", methods=["POST"])
def register():
    user_id = request.form.get("register-username")
    email = request.form.get("register-email")
    password = request.form.get("register-password")
    user_type = request.form.get("user-type", "self")

    # パスワードをハッシュ化
    hashed_password = generate_password_hash(password)

    user_data = {"user_id": user_id, "email": email, "password": hashed_password, "user_type": user_type}

    try:
        new_user_id = db.create_user(user_data)
        # 登録後すぐにログイン
        session["user_id"] = user_id
        session["email"] = email
        session["nickname"] = user_id  # 初期値としてuser_idをニックネームにする
        return redirect(url_for("dashboard"))
    except Exception as e:
        flash(f"登録エラー: {str(e)}")
        return redirect(url_for("index"))


@app.route("/login", methods=["POST"])
def login():
    user_id = request.form.get("login-id")
    password = request.form.get("login-password")

    # ユーザー認証
    user = db.get_user_by_id(user_id)

    if user and check_password_hash(user[3], password):  # user[3]はpasswordカラム
        session["user_id"] = user[1]  # user_id
        session["email"] = user[2]  # email
        session["nickname"] = user[7] if user[7] else user[1]  # nickname or user_id
        return redirect(url_for("dashboard"))
    else:
        flash("ユーザーIDかパスワードが正しくありません。")
        return redirect(url_for("index"))


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))


@app.route("/user")
@login_required
def user():
    # ログインユーザーの情報を取得
    user_data = db.get_user_by_id(session["user_id"])
    return render_template("user.html", user=user_data)


@app.route("/update_user", methods=["POST"])
@login_required
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

    flash("基本情報を更新しました。")
    return redirect(url_for("profile"))


@app.route("/update_profile", methods=["POST"])
@login_required
def update_profile():
    # プロフィール詳細情報更新
    user_id = session["user_id"]

    # プロフィール詳細情報
    profile_data = {
        "home": request.form.get("home"),
        "spouse": request.form.get("spouse"),
        "children_living": request.form.get("children_living"),
        "children_separate": request.form.get("children_separate"),
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

    flash("プロフィール詳細を更新しました。")
    return redirect(url_for("profile"))


@app.route("/dashboard")
@login_required
def dashboard():
    return render_template("dashboard.html")


@app.route("/profile")
@login_required
def profile():
    # ユーザー基本情報を取得
    user_data = db.get_user_by_id(session["user_id"])
    # プロフィール詳細情報を取得
    profile_data = db.get_profile_by_user_id(session["user_id"])

    return render_template("profile.html", user=user_data, profile=profile_data)


@app.route("/iwlm")
@login_required
def iwlm():
    # IWLM情報を取得
    iwlm_data = db.get_iwlm_by_user_id(session["user_id"])

    return render_template("iwlm.html", iwlm=iwlm_data)


@app.route("/diary_calendar")
@login_required
def diary_calendar():
    return render_template("diary_calender.html")


@app.route("/diary_list")
@login_required
def diary_list():
    return render_template("diary_list.html")


@app.route("/profile_table")
@login_required
def profile_table():
    # ユーザー基本情報を取得
    user_data = db.get_user_by_id(session["user_id"])
    # プロフィール詳細情報を取得
    profile_data = db.get_profile_by_user_id(session["user_id"])

    return render_template("profile_table.html", user=user_data, profile=profile_data)


@app.route("/delete_profile", methods=["POST"])
@login_required
def delete_profile():
    # プロフィール詳細情報を削除
    user_id = session["user_id"]
    conn = db.get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM profiles WHERE user_id = ?", (user_id,))
    conn.commit()
    conn.close()

    flash("プロフィール詳細を削除しました。")
    return redirect(url_for("dashboard"))


@app.route("/update_iwlm", methods=["POST"])
@login_required
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


@app.route("/delete_iwlm", methods=["POST"])
@login_required
def delete_iwlm():
    # IWLM情報を削除
    user_id = session["user_id"]
    conn = db.get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM iwlm WHERE user_id = ?", (user_id,))
    conn.commit()
    conn.close()

    flash("私の暮らし情報を削除しました。")
    return redirect(url_for("dashboard"))


@app.route("/iwlm_table")
@login_required
def iwlm_table():
    # IWLM情報を取得
    user_data = db.get_user_by_id(session["user_id"])
    iwlm_data = db.get_iwlm_by_user_id(session["user_id"])

    return render_template("iwlm_table.html", user=user_data, iwlm=iwlm_data)


@app.route("/howsitgoing")
@login_required
def howsitgoing():
    return render_template("howsitgoing.html")


if __name__ == "__main__":
    db.init_db()
    app.run(debug=True)
