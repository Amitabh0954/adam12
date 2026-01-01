from flask import Blueprint

analytics_controller = Blueprint('analytics_controller', __name__)

@analytics_controller.route('/analytics', methods=['GET'])
def get_analytics():
    return "Analytics data"