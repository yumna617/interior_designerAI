from flask import Blueprint, jsonify
from flask_login import login_required, current_user

user_bp = Blueprint('user', __name__, url_prefix='/user')
@user_bp.route('/profile')
@login_required
def profile():
     return render_template('profile.html', user=current_user)

#bp = Blueprint('main', __name__)
# @bp.route('/')
# def home():
#     return {"message": "Welcome to Interior AI API!"}
# bp = Blueprint('user', __name__, url_prefix='/user')

# # Route to get the current user's profile
# @bp.route('/profile', methods=['GET'])
# @login_required
# def profile():
#     return jsonify({
#         "username": current_user.username,
#         "email": current_user.email
#     })
