from flask import Flask, render_template, request
from config import db

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/user")
def user():
    return render_template("user.html")


@app.route("/register_user", methods=["GET", "POST"])
def register_user():
    if request.method == "POST":
        # フォームデータを取得
        user_data = {
            "user_id": request.form.get("user_id"),
            "email": request.form.get("email"),
            "password": request.form.get("password"),
            "name": request.form.get("name"),
            "furigana": request.form.get("furigana"),
            "nickname": request.form.get("nickname"),
            "gender": request.form.get("gender"),
            "birth_date": request.form.get("birth_date"),
            "family_id1": request.form.get("family_id1"),
            "family_id2": request.form.get("family_id2"),
            "family_id3": request.form.get("family_id3"),
        }

        # データベースにユーザーを登録
        try:
            user_id = db.create_user(user_data)
            return f"ユーザー登録が完了しました。ユーザーID: {user_id}"
        except Exception as e:
            return f"登録エラー: {str(e)}"

    # GETリクエストの場合はユーザー登録ページを表示
    return render_template("user.html")


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


@app.route("/profile")
def profile():
    return render_template("profile.html")


@app.route("/iwlm")
def iwlm():
    return render_template("iwlm.html")


@app.route("/diary_calendar")
def diary_calendar():
    return render_template("diary_calender.html")


@app.route("/diary_list")
def diary_list():
    return render_template("diary_list.html")


@app.route("/iwlm_table")
def iwlm_table():
    return render_template("iwlm_table.html")


@app.route("/profile_table")
def profile_table():
    return render_template("profile_tabele.html")


@app.route("/howsitgoing")
def howsitgoing():
    return render_template("howsitgoing.html")


if __name__ == "__main__":
    db.init_db()
    app.run(debug=True)
