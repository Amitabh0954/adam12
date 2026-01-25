from flask import Flask
from backend.user_account_management.controllers.registration_controller import registration_controller
from backend.user_account_management.controllers.auth_controller import auth_controller
from backend.user_account_management.controllers.password_reset_controller import password_reset_controller
from backend.user_account_management.controllers.profile_controller import profile_controller
from backend.product_catalog_management.controllers.product_controller import product_controller
from backend.product_catalog_management.controllers.product_search_controller import product_search_controller
from backend.product_catalog_management.controllers.category_controller import category_controller
from backend.shopping_cart_functionality.controllers.shopping_cart_controller import shopping_cart_controller

def register_routes(app: Flask):
    app.register_blueprint(registration_controller, url_prefix='/api')
    app.register_blueprint(auth_controller, url_prefix='/api')
    app.register_blueprint(password_reset_controller, url_prefix='/api')
    app.register_blueprint(profile_controller, url_prefix='/api')
    app.register_blueprint(product_controller, url_prefix='/api')
    app.register_blueprint(product_search_controller, url_prefix='/api')
    app.register_blueprint(category_controller, url_prefix='/api')
    app.register_blueprint(shopping_cart_controller, url_prefix='/api')

#### 5. Update MySQL database schema to ensure constraints are applied

##### Create Users Table