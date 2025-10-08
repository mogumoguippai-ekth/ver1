from flask import Flask, render_template
from config import db

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    db.init_db()
    app.run(debug=True)
