import os

class Config(object):
    DEBUG                   = False
    CSRF_ENABLED            = True
    SECRET                  = os.getenv('SECRET')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING                 = True
    DEBUG                   = True
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_TEST_URL')

class StagingConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG   = False
    TESTING = False

app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'staging': StagingConfig,
    'production': ProductionConfig,
}