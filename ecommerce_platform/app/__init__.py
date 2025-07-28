from flask import Flask
from config import Config
from .extensions import db, login_manager, migrate

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)

    from . import routes, auth
    app.register_blueprint(routes.bp)
    app.register_blueprint(auth.auth)

    return app
