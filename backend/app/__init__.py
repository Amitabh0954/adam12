from flask import Flask
from backend.app.routes.routes import register_routes
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from backend.user_account_management.models.user import Base as UserBase
from backend.user_account_management.models.user_session import Base as UserSessionBase
from backend.user_account_management.models.login_attempt import Base as LoginAttemptBase
from backend.user_account_management.models.password_reset_token import Base as PasswordResetTokenBase
from backend.product_catalog_management.models.product import Base as ProductBase
from backend.product_catalog_management.models.category import Base as CategoryBase
from backend.shopping_cart_functionality.models.shopping_cart import Base as ShoppingCartBase

def create_app():
    app = Flask(__name__)
    app.secret_key = "supersecretkey"  # Ensure session management

    # Initialize the database
    user_engine = create_engine('mysql+pymysql://username:password@localhost:3306/databasename')
    UserSession = sessionmaker(bind=user_engine)
    UserBase.metadata.create_all(user_engine)
    UserSessionBase.metadata.create_all(user_engine)
    LoginAttemptBase.metadata.create_all(user_engine)
    PasswordResetTokenBase.metadata.create_all(user_engine)
    ProductBase.metadata.create_all(user_engine)
    CategoryBase.metadata.create_all(user_engine)
    ShoppingCartBase.metadata.create_all(user_engine)

    # Register routes
    register_routes(app)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)

#### 5. Update requirements.txt

##### Requirements File