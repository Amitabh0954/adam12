from flask import Blueprint, request, jsonify
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from backend.product_catalog_management.services.product_service import ProductService

engine = create_engine('mysql+pymysql://username:password@localhost:3306/databasename')
Session = sessionmaker(bind=engine)

product_controller = Blueprint('product_controller', __name__)

@product_controller.route('/product', methods=['POST'])
def add_product():
    session = Session()
    product_service = ProductService(session)

    try:
        product = product_service.add_product(request.json)
        product_schema = ProductSchema()
        return jsonify(product_schema.dump(product)), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

##### Product Schema