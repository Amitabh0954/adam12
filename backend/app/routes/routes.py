from flask import Flask
from backend.user_account_management.controllers.registration_controller import registration_controller

def register_routes(app: Flask):
    app.register_blueprint(registration_controller, url_prefix='/api')

#### 5. Update MySQL database schema to ensure constraints are applied

##### Create Users Table