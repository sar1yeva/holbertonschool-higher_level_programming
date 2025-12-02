#!/usr/bin/python3
from flask import Flask, render_template
import json
import os

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

# -------------------------
#     NEW ITEMS ROUTE
# -------------------------
@app.route('/items')
def items():
    file_path = os.path.join(os.path.dirname(__file__), "items.json")

    # Read JSON file safely
    try:
        with open(file_path, "r") as f:
            data = json.load(f)
            items_list = data.get("items", [])
    except Exception:
        items_list = []

    return render_template("items.html", items=items_list)


if __name__ == "__main__":
    app.run(debug=True)
