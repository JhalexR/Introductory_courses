from flask import Blueprint
from flask import jsonify
from flask import request

auth_bp = Blueprint(
    "auth",
    __name__
)

@auth_bp.route(
    "/api/auth/login",
    methods=["POST"]
)
def login():

    data = request.get_json()

    return jsonify({
        "message": "Login pendiente",
        "email": data.get("email")
    })