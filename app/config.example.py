import os

# For CSRF protection
# IMPORTANT: Do not push your keys to GitHub!
# Create your own config.py using this file as an example

class Config(object):
    # Get your own CSRF token from here: http://nux.net/secret
    SECRET_KEY = os.environ.get("SECRET_KEY") or 'my-key-eiei'
    # URI Scheme: 'mysql+pymysql://<user>:<password>@<host>/db_test1'
    SQLALCHEMY_DATABASE_URI = 'mysql://'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(object):
    DEBUG = True
    SQLALCHEMY_ECHO = True

class ProductionConfig(object):
    DEBUG = False

app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}