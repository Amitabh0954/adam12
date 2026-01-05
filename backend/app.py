from flask import Flask
from config.config import Config
from controllers.products.product_controller import product_controller
from controllers.cart.cart_controller import cart_controller
from controllers.checkout.checkout_controller import checkout_controller
from controllers.orders.order_controller import order_controller
from controllers.reviews.review_controller import review_controller
from controllers.promotions.promotion_controller import promotion_controller
from controllers.analytics.analytics_controller import analytics_controller
from controllers.support.support_controller import support_controller

def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object(Config)
    
    with app.app_context():
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
    app.run(host="0.0.0.0", port=5000)