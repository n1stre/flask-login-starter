from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bootstrap import Bootstrap

from instance.config import app_config

app = Flask(__name__, instance_relative_config=True)
db = SQLAlchemy()
login_manager = LoginManager()


def create_app(config_name):
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

    Bootstrap(app)

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_message = "You must be logged in to access this page."
    login_manager.login_view = "auth.login"
    migrate = Migrate(app, db)

    from app.mod_auth.models import User
    from app.mod_commands.models import Command
    from app.mod_auth.controllers import mod_auth
    from app.mod_home.controllers import mod_home
    # from app.mod_auth.controllers import mod_commands

    app.register_blueprint(mod_home)
    app.register_blueprint(mod_auth)
    # app.register_blueprint(mod_commands)

    # Sample HTTP error handling
    @app.errorhandler(404)
    def not_found(error):
      return render_template('404.html'), 404

    return app