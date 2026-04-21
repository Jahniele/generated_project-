from flask import Blueprint, request, jsonify
import sqlite3

customers_bp = Blueprint("customers", __name__)
DB = "database.db"

@customers_bp.route("/", methods=["GET"])
def get_customers():
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("SELECT * FROM customers")
    rows = c.fetchall()
    return jsonify(rows)

@customers_bp.route("/", methods=["POST"])
def add_customer():
    data = request.json
    conn = sqlite3.connect(DB)
    c = conn.cursor()

    c.execute("INSERT INTO customers (name, email) VALUES (?, ?)",
              (data["name"], data["email"]))
    conn.commit()

    return jsonify({"message": "Customer added"})

@customers_bp.route("/<int:id>", methods=["DELETE"])
def delete_customer(id):
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("DELETE FROM customers WHERE id=?", (id,))
    conn.commit()
    return jsonify({"message": "Deleted"})
