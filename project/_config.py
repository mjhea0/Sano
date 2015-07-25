class DevelopmentConfig(object):
    DATABASE_URI = "postgresql://localhost:5432/sano"
    DEBUG = True


class TestingConfig(object):
    DATABASE_URI = "postgresql://localhost:5432/sano-test"
    DEBUG = True
