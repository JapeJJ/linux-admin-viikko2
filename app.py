import os

import pymysql
from flask import Flask

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

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Week 2</title>
</head>
<body>
  <h1>Week 2</h1>
  <p>This page has been visited {count} times.</p>
</body>
</html>"""
