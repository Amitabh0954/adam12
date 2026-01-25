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

### Summary:

This set of implementations covers the functionality of allowing an admin to update existing product details with appropriate validations and ensuring integration with the current Flask application structure. The routes ensure proper handling of requests, and the service methods encapsulate the logic for managing persistence and business rules.

- **Product model** is already properly defined.
- **ProductUpdateSchema** ensures robust validation.
- **ProductService** handles business logic for updating products.
- **ProductController** provides the API endpoints for product updates.
- **Routes** integration maintains the overall coherence.