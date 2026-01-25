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

This completes the implementation of the functionality to delete products from the product catalog, with checks ensuring only admins can perform this action, following the given folder structure. 

Routes, service and controller methods are appropriately modified, and the verification for admin functionality is in place. The implementation takes into account the need to update the information across different controllers and makes sure that the user has the proper permissions to delete a product.