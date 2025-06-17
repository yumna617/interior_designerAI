import sys
import os
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from app import create_app,db
from config import Config
from app.models.user import User
from flask import jsonify

app = create_app()

@app.cli.command('init-db')
def init_db_command():
    """Initialize the database."""
    with app.app_context():
        db.create_all()
    print('Initialized the database.')
@app.route('/')
def home():
    return jsonify({"message": "Welcome to Interior AI API!"})
if __name__ == "__main__":
    app.run(debug=True)
