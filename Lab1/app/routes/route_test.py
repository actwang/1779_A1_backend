from flask import Blueprint

from app.models.User import User

test_blueprint = Blueprint('route_test', __name__, url_prefix='/test')


@test_blueprint.route('/testlogin')
def index():
    test_user = User("114", "514", ["9", "19"])
    return test_user.to_json()
