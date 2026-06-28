from flask import Blueprint, jsonify

products_bp = Blueprint(
    "products",
    __name__
)

@products_bp.route(
    "/api/products",
    methods=["GET"]
)
def get_products():

    return jsonify([
        {
            "id": 1,
            "titulo": "El Quijote",
            "autor": "Miguel de Cervantes",
            "precio": 25.99
        }
    ])