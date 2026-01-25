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

This implementation focuses on enhancing the shopping cart functionality by allowing users to remove items from their cart while ensuring the total price is updated and providing confirmation before removal. The changes made include:

- **Extending Services** to handle item removal from the cart.
- **Updating Controllers** to expose endpoints for cart removal.
- **Ensuring Routes** include the necessary endpoints for shopping cart operations.

With all these changes integrated, the shopping cart functionality will be robust, allowing both adding and removing items securely and efficiently.