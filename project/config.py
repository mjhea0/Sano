class BaseConfig(object):
    DEBUG = True
    SECRET_KEY = "not-a-good-secret"


class TestingConfig(BaseConfig):
    DATABASE_URI = "postgresql://localhost/sano-test"
    DEBUG = True


class DevelopmentConfig(BaseConfig):
    DATABASE_URI = "postgresql://localhost/sano"
    DEBUG = True
