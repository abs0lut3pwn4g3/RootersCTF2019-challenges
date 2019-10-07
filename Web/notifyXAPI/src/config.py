import os

basedir = os.path.abspath(os.path.dirname(__file__))

''' Flask related Configurations. Note: DO NOT FORGET TO CHANGE SECRET_KEY ! '''

class BaseConfig:

    DOMAIN = 'http://127.0.0.1:5000/api/v1/'

    MARSHMALLOW_STRICT = True
    MARSHMALLOW_DATEFORMAT = 'rfc'

    SECRET_KEY = 'you-will-never-guess' # os.environ.get('SECRET_KEY')
    SECURITY_PASSWORD_SALT = 'test'

    WTF_CSRF_ENABLED = False
    MAX_AGE = 86400

    RATELIMIT_DEFAULT = "24000/day;2400/hour;100/minute;6/second"
    RATELIMIT_HEADERS_ENABLED = True
    RATELIMIT_STRATEGY = 'fixed-window'

    JWT_SECRET_KEY = 'secret'
    JWT_HEADER_NAME = 'authorization'

    JSON_SORT_KEYS = False 


class Config(BaseConfig):
    
    SQLALCHEMY_DATABASE_URI = 'postgres://zoai-eshaan:eshaan@localhost/jwt-api-testing'
    SQLALCHEMY_TRACK_MODIFICATIONS = False 
    DEBUG = True # Turn DEBUG OFF before deployment