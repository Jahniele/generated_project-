from flask import Blueprint, request, jsonify
import sqlite3

auth_bp = Blueprint("auth", __name__)
DB = "database.db"

@auth_bp.route("/signup", methods=["POST"])
def signup():
    data = request.json
    conn = sqlite3.connect(DB)
    c = conn.cursor()

    try:
        c.execute("INSERT INTO users (username, password) VALUES (?, ?)",
                  (data["username"], data["password"]))
        conn.commit()
        return jsonify({"message": "User created"}), 201
    except:
        return jsonify({"error": "User exists"}), 400

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    conn = sqlite3.connect(DB)
    c = conn.cursor()

    c.execute("SELECT * FROM users WHERE username=? AND password=?",
              (data["username"], data["password"]))
    user = c.fetchone()

    if user:
        return jsonify({"message": "Login success", "user": user[1]})
    return jsonify({"error": "Invalid credentials"}), 401
