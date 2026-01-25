from flask import Flask
from backend.user_account_management.controllers.user_controller import user_controller

def register_routes(app: Flask):
    app.register_blueprint(user_controller, url_prefix='/api')

#### 6. Ensure the main app initialization properly integrates this module