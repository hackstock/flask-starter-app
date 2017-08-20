from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_moment import Moment
from config import config

db = SQLAlchemy()
moment = Moment()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    moment.init_app(app)
    db.init_app(app)

    from app.admin import admin as admin_blueprint
    from app.api import api as api_blueprint

    app.register_blueprint(admin_blueprint, url_prefix='/admin')
    app.register_blueprint(api_blueprint, url_prefix='/api')

    return app
