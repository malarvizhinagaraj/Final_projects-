from flask import Flask
from config import Config
from .extensions import db, login_manager, migrate, mail

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)
    mail.init_app(app)

    from . import routes
    app.register_blueprint(routes.bp)

    return app
