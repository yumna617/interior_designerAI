from flask import Blueprint, jsonify,render_template
from flask_login import login_required

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def home():
    return {"message": "Welcome to Interior AI API!"}

@main_bp.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')

@main_bp.route('/profile')
@login_required
def profile():
    return render_template('profile.html')