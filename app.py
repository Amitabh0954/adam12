from flask import Flask
from backend.config.config import Config
from backend.controllers.auth.registration_controller import registration_bp

def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object(Config)

    # Register blueprints
    app.register_blueprint(registration_bp, url_prefix='/api/v1/auth')

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000)