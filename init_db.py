from app import create_app, db
from app.models.user import User  # Now this should work

app = create_app()

with app.app_context():
    print("Creating tables...")
    db.create_all()
    print("Database tables created successfully!")
    print("Tables created:",  db.Model.metadata.tables.keys())  # Verify