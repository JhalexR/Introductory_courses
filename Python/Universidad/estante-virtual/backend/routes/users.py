from flask import Blueprint
from flask import jsonify

users_bp = Blueprint(
    "users",
    __name__
)

@users_bp.route(
    "/api/users",
    methods=["GET"]
)
def get_users():

    return jsonify([])