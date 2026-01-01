from flask import Blueprint

review_controller = Blueprint('review_controller', __name__)

@review_controller.route('/reviews', methods=['GET'])
def get_reviews():
    return "This is the reviews endpoint", 200
