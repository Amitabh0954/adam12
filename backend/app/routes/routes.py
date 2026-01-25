from flask import Flask
from backend.user_account_management.controllers.user_controller import user_controller
from backend.user_account_management.controllers.password_reset_controller import password_reset_controller
from backend.user_account_management.controllers.profile_controller import profile_controller
from backend.product_catalog_management.controllers.product_controller import product_controller
from backend.product_catalog_management.controllers.category_controller import category_controller
from backend.shopping_cart_functionality.controllers.shopping_cart_controller import shopping_cart_controller

def register_routes(app: Flask):
    app.register_blueprint(user_controller, url_prefix='/api')
    app.register_blueprint(password_reset_controller, url_prefix='/api')
    app.register_blueprint(profile_controller, url_prefix='/api')
    app.register_blueprint(product_controller, url_prefix='/api')
    app.register_blueprint(category_controller, url_prefix='/api')
    app.register_blueprint(shopping_cart_controller, url_prefix='/api')

### Summary

This implementation makes sure the shopping cart state is saved to the user's profile and can be retrieved across multiple sessions. The changes made include:

- **Extending Services** to handle saving and retrieving the cart state.
- **Updating Controllers** to include endpoints for save and retrieve functionality.
- **Ensuring Routes** include the necessary endpoints for shopping cart operations.

These changes will ensure that the shopping cart functionality provides a seamless and persistent shopping experience for logged-in users.