
# Wedding Planning Platform
# Developed by: Swayam Vishwakarma
# Technologies: Flask, HTML, CSS
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/vendors")
def vendors():
    return render_template("vendors.html")

@app.route("/checklist")
def checklist():
    return render_template("checklist.html")

app.run(debug=True)
