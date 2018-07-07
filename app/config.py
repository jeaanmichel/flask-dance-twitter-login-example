import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'chave-super-secreta'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'app.db')

    # Twitter App
    TWITTER_API_KEY = os.environ.get('TWITTER_API_KEY') or 'twitter-api-key'
    TWITTER_API_SECRET = os.environ.get('TWITTER_API_SECRET') or\
                         'twitter-api-secret'
