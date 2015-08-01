class BaseConfig(object):
    DEBUG = True
    SECRET_KEY = "not-a-good-secret"


class TestingConfig(BaseConfig):
    DATABASE_URI = "postgresql://localhost:5432/sano-test"
    DEBUG = True


class DevelopmentConfig(BaseConfig):
    DATABASE_URI = "postgresql://localhost:5432/sano"
    DEBUG = True
