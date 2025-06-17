import os

class Config:
    # Flask configurations
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_default_secret_key'
    FLASK_APP = os.environ.get('FLASK_APP') or 'run.py'
    FLASK_ENV = os.environ.get('FLASK_ENV') or 'development'
    
    # Database configuration (Example: using SQLAlchemy)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///app.db'  # Use your actual DB URL here
    
    # API Keys and Tokens (ensure these are set in your .env file)
    HUGGINGFACE_TOKEN = os.environ.get('HUGGINGFACE_TOKEN')
    FSQ_API_KEY = os.environ.get('FSQ_API_KEY')
    ETSY_API_KEY = os.environ.get('ETSY_API_KEY')
    PINTEREST_TOKEN = os.environ.get('PINTEREST_TOKEN')
    OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')
    ORS_API_KEY = os.environ.get('ORS_API_KEY')
    CLOUDINARY_CLOUD_NAME = os.environ.get('CLOUDINARY_CLOUD_NAME')
    CLOUDINARY_API_KEY = os.environ.get('CLOUDINARY_API_KEY')
    CLOUDINARY_API_SECRET = os.environ.get('CLOUDINARY_API_SECRET')
    UNSPLASH_API_KEY = os.environ.get('UNSPLASH_API_KEY')

    # Other configurations
    MAIL_SERVER = 'smtp.gmail.com'  # If you are using Gmail for emails
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')  # Email username
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')  # Email password
