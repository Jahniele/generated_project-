from flask import Blueprint, jsonify
import sqlite3

dashboard_bp = Blueprint("dashboard", __name__)
DB = "database.db"

@dashboard_bp.route("/", methods=["GET"])
def dashboard():
    conn = sqlite3.connect(DB)
    c = conn.cursor()

    c.execute("SELECT COUNT(*) FROM users")
    users = c.fetchone()[0]

    c.execute("SELECT COUNT(*) FROM customers")
    customers = c.fetchone()[0]

    return jsonify({
        "users": users,
        "customers": customers
    })
