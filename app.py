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
        "money_sources": ",".join(request.form.getlist("money"))  # チェックボックスは複数選択
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
    return render_template("iwlm.html")


@app.route("/diary_calendar")
@login_required
def diary_calendar():
    return render_template("diary_calender.html")


@app.route("/diary_list")
@login_required
def diary_list():
    return render_template("diary_list.html")


@app.route("/iwlm_table")
@login_required
def iwlm_table():
    return render_template("iwlm_table.html")


@app.route("/profile_table")
@login_required
def profile_table():
    return render_template("profile_tabele.html")


@app.route("/howsitgoing")
@login_required
def howsitgoing():
    return render_template("howsitgoing.html")


if __name__ == "__main__":
    db.init_db()
    app.run(debug=True)
