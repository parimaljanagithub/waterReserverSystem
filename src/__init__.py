
from flask import Flask
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from src.main.Config import Config
from flask_mail import Mail

login_manager = LoginManager()
login_manager.login_view='users.login'
login_manager.login_message_category='info'

bcrypt = Bcrypt()

db = SQLAlchemy()
mail = Mail()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    bcrypt.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    from src.main.routes import main
    from src.users.routes import users
    from src.upload.routes import upload
    app.register_blueprint(main)
    app.register_blueprint(users)
    app.register_blueprint(upload)

    return app


