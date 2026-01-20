from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

DATABASE_URL = 'sqlite:////tmp/test.db'  # For simplicity, using an SQLite database

engine = create_engine(DATABASE_URL, convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

def init_db():
    import backend.account.models
    import backend.profile.models
    import backend.product.models
    import backend.cart.models
    import backend.checkout.models
    import backend.order.models
    import backend.analytics.models
    import backend.support.models
    Base.metadata.create_all(bind=engine)