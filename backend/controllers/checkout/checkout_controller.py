from flask import Blueprint

checkout_controller = Blueprint('checkout_controller', __name__)

@checkout_controller.route('/checkout')
def checkout():
    return "Checkout endpoint"
