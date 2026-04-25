#!/usr/bin/python3
"""
Flask app with JSON, CSV and SQLite data sources.
"""

from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__, template_folder="templates")


# ---------------- JSON ----------------
def read_json():
    with open("products.json", "r") as f:
        return json.load(f)


# ---------------- CSV ----------------
def read_csv():
    products = []
    with open("products.csv", "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            row["id"] = int(row["id"])
            row["price"] = float(row["price"])
            products.append(row)
    return products


# ---------------- SQL ----------------
def read_sql():
    try:
        conn = sqlite3.connect("products.db")
        cursor = conn.cursor()

        cursor.execute("SELECT id, name, category, price FROM Products")
        rows = cursor.fetchall()

        conn.close()

        products = []
        for row in rows:
            products.append({
                "id": row[0],
                "name": row[1],
                "category": row[2],
                "price": row[3]
            })

        return products

    except Exception:
        return []


# ---------------- ROUTE ----------------
@app.route('/products')
def products():
    source = request.args.get("source")

    if source == "json":
        data = read_json()

    elif source == "csv":
        data = read_csv()

    elif source == "sql":
        data = read_sql()

    else:
        return render_template(
            "product_display.html",
            error="Wrong source",
            products=[]
        )

    return render_template(
        "product_display.html",
        products=data,
        error=None
    )


if __name__ == '__main__':
    app.run(debug=True, port=5000)
