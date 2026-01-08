from flask import Flask, session
from backend.config.config import Config
from backend.controllers.auth.registration_controller import registration_bp
from backend.controllers.auth.login_controller import login_bp
from backend.controllers.auth.password_reset_controller import password_reset_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.secret_key = Config.SECRET_KEY

    app.register_blueprint(registration_bp, url_prefix='/api/auth')
    app.register_blueprint(login_bp, url_prefix='/api/auth')
    app.register_blueprint(password_reset_bp, url_prefix='/api/auth')

    @app.before_request
    def make_session_permanent():
        session.permanent = True
        app.permanent_session_lifetime = timedelta(minutes=10)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host='0.0.0.0', port=5000)