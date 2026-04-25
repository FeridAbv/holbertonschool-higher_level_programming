#!/usr/bin/python3
"""
Flask app that reads products from JSON, CSV, or SQLite database.
"""

from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__, template_folder="templates")


# ---------------- JSON ----------------
def read_json():
    """Read products from JSON file."""
    try:
        with open("products.json", "r") as f:
            return json.load(f)
    except Exception:
        return []


# ---------------- CSV ----------------
def read_csv():
    """Read products from CSV file."""
    products = []
    try:
        with open("products.csv", "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                products.append({
                    "id": int(row["id"]),
                    "name": row["name"],
                    "category": row["category"],
                    "price": float(row["price"])
                })
    except Exception:
        return []

    return products


# ---------------- SQL ----------------
def read_sql(product_id=None):
    """Read products from SQLite database."""
    try:
        conn = sqlite3.connect("products.db")
        cursor = conn.cursor()

        if product_id:
            cursor.execute(
                "SELECT id, name, category, price FROM Products WHERE id=?",
                (product_id,)
            )
        else:
            cursor.execute(
                "SELECT id, name, category, price FROM Products"
            )

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
    """Display products from JSON, CSV, or SQL based on source."""

    source = request.args.get("source")
    product_id = request.args.get("id")

    if product_id:
        product_id = int(product_id)

    data = []

    if source == "json":
        data = read_json()

    elif source == "csv":
        data = read_csv()

    elif source == "sql":
        data = read_sql(product_id)

    else:
        return render_template(
            "product_display.html",
            error="Wrong source",
            products=[]
        )

    # filter for JSON & CSV
    if product_id and source != "sql":
        data = [p for p in data if int(p["id"]) == product_id]

        if not data:
            return render_template(
                "product_display.html",
                error="Product not found",
                products=[]
            )

    return render_template(
        "product_display.html",
        products=data,
        error=None
    )


if __name__ == '__main__':
    app.run(debug=True, port=5000)
