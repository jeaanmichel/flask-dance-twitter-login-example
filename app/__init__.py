from flask import Flask
from flask_bootstrap import Bootstrap
from flask_dance.contrib.twitter import make_twitter_blueprint
from flask_sqlalchemy import SQLAlchemy
from config import Config
import logging
logging.basicConfig()

app = Flask(__name__)
app.config.from_object(Config)

twitter_blueprint = make_twitter_blueprint()
app.register_blueprint(twitter_blueprint, url_prefix='/login')

Bootstrap(app)

db = SQLAlchemy(app)

from views import *
