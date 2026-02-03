from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

def get_db():
    return sqlite3.connect("database.db")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/vendors")
def vendors():
    db = get_db()
    cur = db.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS vendors (name TEXT, category TEXT)")
    cur.execute("SELECT * FROM vendors")
    data = cur.fetchall()
    return render_template("vendors.html", vendors=data)


@app.route("/add_vendor", methods=["POST"])
def add_vendor():
    name = request.form["name"]
    category = request.form["category"]
    db = get_db()
    cur = db.cursor()
    cur.execute("INSERT INTO vendors VALUES (?, ?)", (name, category))
    db.commit()
    return redirect("/vendors")


@app.route("/checklist")
def checklist():
    db = get_db()
    cur = db.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tasks (task TEXT)")
    cur.execute("SELECT * FROM tasks")
    tasks = cur.fetchall()
    return render_template("checklist.html", tasks=tasks)


@app.route("/add_task", methods=["POST"])
def add_task():
    task = request.form["task"]
    db = get_db()
    cur = db.cursor()
    cur.execute("INSERT INTO tasks VALUES (?)", (task,))
    db.commit()
    return redirect("/checklist")


if __name__ == "__main__":
    app.run(debug=True)
@app.route("/delete_task/<task>")
def delete_task(task):
    db = get_db()
    cur = db.cursor()
    cur.execute("DELETE FROM tasks WHERE task=?", (task,))
    db.commit()
    return redirect("/checklist")
