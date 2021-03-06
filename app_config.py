class Config(object):
    DEBUG = False
    TESTING = False
    HOST = '0.0.0.0'
    PORT = 5000

class DevConfig(Config):
    DEBUG = True
    SEND_FILE_MAX_AGE_DEFAULT = 0 
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class TestConfig(Config):
    TESTING = True
