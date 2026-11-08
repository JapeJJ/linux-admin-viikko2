import os

import pymysql
from flask import Flask, render_template

app = Flask(__name__)


def get_db():
    return pymysql.connect(
        host="localhost",
        user=os.environ["DB_USER"],
        password=os.environ["DB_PASSWORD"],
        database="laskuri",
        autocommit=True,
    )


@app.route("/")
def index():
    conn = get_db()
    try:
        with conn.cursor() as cur:
            cur.execute("UPDATE visits SET count = count + 1 WHERE id = 1")
            cur.execute("SELECT count FROM visits WHERE id = 1")
            count = cur.fetchone()[0]
    finally:
        conn.close()

    return render_template("index.html", count=count)

