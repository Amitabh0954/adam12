from flask import Flask
from backend.app.routes.routes import register_routes
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from backend.user_account_management.models.user import Base

def create_app():
    app = Flask(__name__)

    # Initialize the database
    engine = create_engine('sqlite:///user.db')
    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)

    # Register routes
    register_routes(app)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)

#### 7. Update the database schema to include the new fields