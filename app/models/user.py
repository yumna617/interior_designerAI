from app import db
from flask_login import UserMixin  # Add this import

class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120))
    
    def __repr__(self):
        return f'<User {self.username}>'
    # These methods are added by UserMixin:
    # is_authenticated, is_active, is_anonymous, get_id()
    # But you can override them if needed