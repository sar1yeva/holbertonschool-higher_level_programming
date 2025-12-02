#!/usr/bin/python3
from flask import Flask, render_template, request
import json
import csv
import sqlite3
import os

app = Flask(__name__)


# ---------- JSON Reader ----------
def read_json(file_path):
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
        return data
    except Exception:
        return []


# ---------- CSV Reader ----------
def read_csv(file_path):
    try:
        products = []
        with open(file_path, newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                row['id'] = int(row['id'])
                row['price'] = float(row['price'])
                products.append(row)
        return products
    except Exception:
        return []


# ---------- SQLite Reader ----------
def read_sqlite(db_path):
    products = []
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, category, price FROM Products")
        rows = cursor.fetchall()
        for r in rows:
            products.append({
                'id': r[0],
                'name': r[1],
                'category': r[2],
                'price': r[3]
            })
        conn.close()
    except Exception:
        products = []
    return products


@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)
    error = None
    products_list = []

    # Determine source
    if source == "json":
        products_list = read_json("products.json")
    elif source == "csv":
        products_list = read_csv("products.csv")
    elif source == "sql":
        products_list = read_sqlite("products.db")
    else:
        error = "Wrong source"
        return render_template("product_display.html", error=error, products=[])

    # Filter by id if provided
    if product_id is not None:
        filtered = [p for p in products_list if p.get("id") == product_id]
        if not filtered:
            error = "Product not found"
            products_list = []
        else:
            products_list = filtered

    return render_template("product_display.html", products=products_list, error=error)


if __name__ == "__main__":
    app.run(debug=True)
