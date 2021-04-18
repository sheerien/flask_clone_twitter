import os

class Config:
    """ Basic Configurations """
    DEBUG = False
    PORT = os.environ.get('PORT') or 5000
    ENV = os.environ.get('ENV')

class development(Config):
    """ development configurations mod"""
    DEBUG = True

class production(Config):
    """ production configurations mod"""
    PORT = os.environ.get('PORT') or 8080