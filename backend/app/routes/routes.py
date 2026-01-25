from flask import Flask
from backend.user_account_management.controllers.registration_controller import registration_controller
from backend.user_account_management.controllers.auth_controller import auth_controller
from backend.user_account_management.controllers.password_reset_controller import password_reset_controller
from backend.user_account_management.controllers.profile_controller import profile_controller
from backend.product_catalog_management.controllers.product_controller import product_controller

def register_routes(app: Flask):
    app.register_blueprint(registration_controller, url_prefix='/api')
    app.register_blueprint(auth_controller, url_prefix='/api')
    app.register_blueprint(password_reset_controller, url_prefix='/api')
    app.register_blueprint(profile_controller, url_prefix='/api')
    app.register_blueprint(product_controller, url_prefix='/api')

#### 5. MySQL database schema

Assuming the Product table already exists, there's no need to add a new SQL file.

#### 6. Ensure this feature works by initializing it in the application