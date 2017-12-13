# project/config.py


import os


class BaseConfig:
    """Base configuration"""
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'my_precious'


class DevelopmentConfig(BaseConfig):
    """Development configuration"""
    DEBUG = True
    #SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_DATABASE_URI = 'postgres://postgres:postgres@localhost:5432/users_dev'


class TestingConfig(BaseConfig):
    """Testing configuration"""
    DEBUG = True
    TESTING = True
    #SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_TEST_URL')
    SQLALCHEMY_DATABASE_URI = 'postgres://postgres:postgres@localhost:5432/users_test'


class ProductionConfig(BaseConfig):
    """Production configuration"""
    DEBUG = False
    #SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_DATABASE_URI = 'postgres://postgres:postgres@localhost:5432/users_dev'