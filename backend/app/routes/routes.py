from flask import Flask
from backend.user_account_management.controllers.user_controller import user_controller
from backend.user_account_management.controllers.password_reset_controller import password_reset_controller
from backend.user_account_management.controllers.profile_controller import profile_controller
from backend.product_catalog_management.controllers.product_controller import product_controller

def register_routes(app: Flask):
    app.register_blueprint(user_controller, url_prefix='/api')
    app.register_blueprint(password_reset_controller, url_prefix='/api')
    app.register_blueprint(profile_controller, url_prefix='/api')
    app.register_blueprint(product_controller, url_prefix='/api')

### Summary

This implementation adds the product search functionality, ensuring that users can search products based on various criteria and that the API supports pagination. The service layer contains the logic for searching and paginating results, while the controller handles client requests and forward them to the service. The routes are updated to include endpoints for search functionality. 

These steps ensure a complete and coherent integration within the provided folder structure.