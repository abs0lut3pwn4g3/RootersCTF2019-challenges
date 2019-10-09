import os

basedir = os.path.abspath(os.path.dirname(__file__))

class BaseConfig:

    DOMAIN = 'https://notifyxapi.herokuapp.com/api/v1/'

    MARSHMALLOW_STRICT = True
    MARSHMALLOW_DATEFORMAT = 'rfc'

    SECRET_KEY = 'ef6d4044250bb97e3ea5d05bb5229ee8' # os.environ.get('SECRET_KEY')

    WTF_CSRF_ENABLED = False
    MAX_AGE = 86400

    RATELIMIT_DEFAULT = "24000/day;2400/hour;100/minute;6/second"
    RATELIMIT_HEADERS_ENABLED = True
    RATELIMIT_STRATEGY = 'fixed-window'

    JWT_SECRET_KEY = 'veryveryrandomstring'
    JWT_HEADER_NAME = 'authorization'

    JSON_SORT_KEYS = False 


class Config(BaseConfig):
    
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False 
    DEBUG = False # Turn DEBUG OFF before deployment