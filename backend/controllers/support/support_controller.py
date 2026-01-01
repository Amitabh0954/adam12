from flask import Blueprint

support_controller = Blueprint('support_controller', __name__)

# Define a test route or function
@support_controller.route('/support', methods=['GET'])
def get_support():
    return "Support Controller"
