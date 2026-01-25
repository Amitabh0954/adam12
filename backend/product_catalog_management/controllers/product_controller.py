from flask import Blueprint, request, jsonify
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from backend.product_catalog_management.services.product_service import ProductService
from backend.product_catalog_management.schemas.product_schema import ProductSchema

engine = create_engine('mysql+pymysql://username:password@localhost:3306/databasename')
Session = sessionmaker(bind=engine)

product_controller = Blueprint('product_controller', __name__)

@product_controller.route('/products', methods=['POST'])
def add_product():
    session = Session()
    product_service = ProductService(session)
    
    try:
        data = request.json
        product = product_service.add_product(data)
        product_schema = ProductSchema()
        return jsonify(product_schema.dump(product)), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

##### Product Schema