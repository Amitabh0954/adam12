from flask import Flask
from backend.user_account_management.controllers.user_controller import user_controller
from backend.user_account_management.controllers.password_reset_controller import password_reset_controller
from backend.user_account_management.controllers.profile_controller import profile_controller
from backend.product_catalog_management.controllers.product_controller import product_controller
from backend.product_catalog_management.controllers.category_controller import category_controller

def register_routes(app: Flask):
    app.register_blueprint(user_controller, url_prefix='/api')
    app.register_blueprint(password_reset_controller, url_prefix='/api')
    app.register_blueprint(profile_controller, url_prefix='/api')
    app.register_blueprint(product_controller, url_prefix='/api')
    app.register_blueprint(category_controller, url_prefix='/api')

#### 7. Ensure main application integration