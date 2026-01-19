from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from config.config import Config
from controllers.auth.auth_controller import auth_controller
from controllers.products.product_controller import product_controller
from controllers.cart.cart_controller import cart_controller
from controllers.checkout.checkout_controller import checkout_controller
from controllers.orders.order_controller import order_controller
from controllers.reviews.review_controller import review_controller
from controllers.promotions.promotion_controller import promotion_controller
from controllers.analytics.analytics_controller import analytics_controller
from controllers.support.support_controller import support_controller

# Initialize extensions
db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()

def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object(Config)

    # Enable CORS
    CORS(app)
    
    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    # Health check route
    @app.route('/health', methods=['GET'])
    def health_check():
        return jsonify({"status": "OK", "message": "Server is running"}), 200

    # Root route
    @app.route('/', methods=['GET'])
    def index():
        return jsonify({"message": "Welcome to the API backend"}), 200

    # Error handlers
    @app.errorhandler(404)
    def not_found_error(error):
        return jsonify({"error": "Not Found"}), 404

    @app.errorhandler(500)
    def internal_error(error):
        return jsonify({"error": "Internal Server Error"}), 500

    with app.app_context():
        app.register_blueprint(auth_controller)
        app.register_blueprint(product_controller)
        app.register_blueprint(cart_controller)
        app.register_blueprint(checkout_controller)
        app.register_blueprint(order_controller)
        app.register_blueprint(review_controller)
        app.register_blueprint(promotion_controller)
        app.register_blueprint(analytics_controller)
        app.register_blueprint(support_controller)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000, debug=True)