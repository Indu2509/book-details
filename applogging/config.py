class Config(object):
    DEBUG = False
    TESTING = False
    MESSAGE = "DEVELOPMENT"


class ProductionConfig(Config):
    MESSAGE = "PRODUCTION"


class StaggingConfig(Config):
    MESSAGE = "STAGGING"

