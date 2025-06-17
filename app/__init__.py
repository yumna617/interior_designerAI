# app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_mail import Mail
from flask_migrate import Migrate
from config import Config


db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.login_message_category = 'info'
mail = Mail()
migrate = Migrate()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
    
    if app.config['FLASK_ENV'] == 'production':
        app.config['SQLALCHEMY_DATABASE_URI'] = app.config.get('DATABASE_URL').replace("postgres://", "postgresql://", 1)
    else:
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
  
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    migrate.init_app(app, db)

    from app.models.user import User
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    
    from app.routes.auth import auth
    from app.routes.ai import bp as ai_blueprint
    from app.routes.user import  user_bp 
    from app.routes.main import main_bp 

    app.register_blueprint(main_bp) 
    app.register_blueprint(auth)
    app.register_blueprint(ai_blueprint)
    app.register_blueprint(user_bp)
   # print(dir(app.routes.user))  # Check if 'user_bp' is there   ,,,,This error occurs because you're trying to access 
   # app.routes.user when Flask doesn't automatically create a routes attribute.  so delete this 

    #user = app.routes.user.user_bp          Delete this line from __init__.py as it's unnecessary and causing errors:
     with app.app_context():
        db.create_all()
    return app
