#!/usr/bin/python3
from flask import Flask, render_template, request
import json
import csv
import os

app = Flask(__name__)


# Helper function to read JSON file
def read_json(file_path):
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
        return data
    except Exception:
        return []


# Helper function to read CSV file
def read_csv(file_path):
    try:
        products = []
        with open(file_path, newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # Convert price to float and id to int for consistency
                row['id'] = int(row['id'])
                row['price'] = float(row['price'])
                products.append(row)
        return products
    except Exception:
        return []


@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)
    error = None
    products_list = []

    # Determine source file
    if source == "json":
        products_list = read_json("products.json")
    elif source == "csv":
        products_list = read_csv("products.csv")
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
