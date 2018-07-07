from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app.config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)

from app import models
migrate = Migrate(app, models.db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    try:
        manager.run()
    except Exception as e:
        print e.message