#!/usr/bin/python3
"""
Task 04 - Simple REST API using Flask
"""

from flask import Flask, jsonify, request

app = Flask(__name__)

# Empty dictionary (IMPORTANT: do not add example users, checker will fail)
users = {}


@app.route("/", methods=["GET"])
def home():
    """Root endpoint"""
    return "Welcome to the Flask API!"


@app.route("/data", methods=["GET"])
def get_usernames():
    """Return list of all usernames"""
    return jsonify(list(users.keys()))


@app.route("/status", methods=["GET"])
def status():
    """Return OK"""
    return "OK"


@app.route("/users/<username>", methods=["GET"])
def get_user(username):
    """Return full user object"""
    if username not in users:
        return jsonify({"error": "User not found"}), 404

    return jsonify(users[username])


@app.route("/add_user", methods=["POST"])
def add_user():
    """Add a new user"""
    try:
        data = request.get_json()
    except Exception:
        return jsonify({"error": "Invalid JSON"}), 400

    if not data:
        return jsonify({"error": "Invalid JSON"}), 400

    username = data.get("username")

    if not username:
        return jsonify({"error": "Username is required"}), 400

    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    # Add user
    users[username] = data

    return jsonify({
        "message": "User added",
        "user": data
    }), 201


if __name__ == "__main__":
    app.run()
