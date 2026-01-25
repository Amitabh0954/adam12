from flask import Flask
from backend.app.routes.routes import register_routes
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from backend.user_account_management.models.user import Base as UserBase
from backend.product_catalog_management.models.product import Base as ProductBase
from backend.product_catalog_management.models.category import Base as CategoryBase
from backend.shopping_cart_functionality.models.shopping_cart import Base as ShoppingCartBase
from backend.shopping_cart_functionality.models.shopping_cart_item import Base as ShoppingCartItemBase

def create_app():
    app = Flask(__name__)

    # Initialize the database
    user_engine = create_engine('sqlite:///user.db')
    product_engine = create_engine('sqlite:///product_catalog.db')
    shopping_cart_engine = create_engine('sqlite:///shopping_cart.db')
    UserSession = sessionmaker(bind=user_engine)
    ProductSession = sessionmaker(bind=product_engine)
    ShoppingCartSession = sessionmaker(bind=shopping_cart_engine)
    UserBase.metadata.create_all(user_engine)
    ProductBase.metadata.create_all(product_engine)
    CategoryBase.metadata.create_all(product_engine)
    ShoppingCartBase.metadata.create_all(shopping_cart_engine)
    ShoppingCartItemBase.metadata.create_all(shopping_cart_engine)

    # Register routes
    register_routes(app)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)

#### 7. Create the database schema for shopping cart tables