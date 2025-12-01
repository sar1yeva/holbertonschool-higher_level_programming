from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

app = Flask(__name__)
auth = HTTPBasicAuth()
app.config["JWT_SECRET_KEY"] = "secretkey"
jwt = JWTManager(app)

users = {
    "user1": {"username": "user1", "password": generate_password_hash("password"), "role": "user"},
    "admin1": {"username": "admin1", "password": generate_password_hash("password"), "role": "admin"}
}

@auth.verify_password
def verify(username, password):
    if username in users and check_password_hash(users[username]["password"], password):
        return username

@app.route("/basic-protected")
@auth.login_required
def basic():
    return "Basic Auth: Access Granted"

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    if not data: return jsonify({"error": "Invalid JSON"}), 401
    u, p = data.get("username"), data.get("password")
    if u not in users or not check_password_hash(users[u]["password"], p):
        return jsonify({"error": "Invalid credentials"}), 401
    token = create_access_token(identity={"username": u, "role": users[u]["role"]})
    return jsonify(access_token=token)

@app.route("/jwt-protected")
@jwt_required()
def jwt_protected():
    return "JWT Auth: Access Granted"

@app.route("/admin-only")
@jwt_required()
def admin():
    if get_jwt_identity()["role"] != "admin":
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Granted"

# ---- JWT Error Handlers (required for tests) ----
@jwt.unauthorized_loader
def e1(e): return jsonify({"error": "Missing or invalid token"}), 401
@jwt.invalid_token_loader
def e2(e): return jsonify({"error": "Invalid token"}), 401
@jwt.expired_token_loader
def e3(h, p): return jsonify({"error": "Token has expired"}), 401

if __name__ == "__main__":
    app.run()
