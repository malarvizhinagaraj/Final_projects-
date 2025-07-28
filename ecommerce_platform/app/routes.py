# At bottom of app/routes.py

from flask import request, jsonify
from .models import Product
from .extensions import db
from flask_login import login_required, current_user

@bp.route('/api/products', methods=['GET'])
def api_get_products():
    products = Product.query.all()
    data = [
        {
            "id": p.id,
            "name": p.name,
            "price": p.price,
            "stock": p.stock,
            "category": p.category,
            "description": p.description
        }
        for p in products
    ]
    return jsonify(data)

@bp.route('/api/products', methods=['POST'])
@login_required
def api_add_product():
    if not current_user.is_admin:
        return jsonify({"error": "Unauthorized"}), 403

    data = request.get_json()
    if not data:
        return jsonify({"error": "Missing JSON"}), 400

    name = data.get('name')
    price = data.get('price')
    stock = data.get('stock')
    category = data.get('category')
    description = data.get('description')

    if not all([name, price, stock]):
        return jsonify({"error": "Missing fields"}), 400

    product = Product(
        name=name,
        price=float(price),
        stock=int(stock),
        category=category,
        description=description
    )
    db.session.add(product)
    db.session.commit()
    return jsonify({"message": "Product added", "product_id": product.id}), 201
