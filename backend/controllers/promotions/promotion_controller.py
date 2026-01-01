from flask import Blueprint

promotion_controller = Blueprint('promotion_controller', __name__)

@promotion_controller.route('/promotions', methods=['GET'])
def get_promotions():
    return "This is the promotions endpoint"
