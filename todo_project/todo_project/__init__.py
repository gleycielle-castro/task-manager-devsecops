from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
import logging
import os
from logging.handlers import SysLogHandler

app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get(
    'SECRET_KEY',
    '45cf93c4d41348cd9980674ade9a7356'
)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login' 
login_manager.login_message_category = 'danger'

bcrypt = Bcrypt(app)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

handler = SysLogHandler(address='/dev/log')
handler.setLevel(logging.INFO)

formatter = logging.Formatter(
    '%(asctime)s %(name)s: %(message)s'
)

handler.setFormatter(formatter)

app.logger.addHandler(handler)
app.logger.setLevel(logging.INFO)

# Always put Routes at end
from todo_project import routes
