from flask import Blueprint
from flask import jsonify

cart_bp = Blueprint(
    "cart",
    __name__
)

@cart_bp.route(
    "/api/cart",
    methods=["GET"]
)
def get_cart():

    return jsonify([])