import os
from flask import Blueprint, render_template

bp = Blueprint('config', __name__)

class Config:
    pass

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(os.getcwd(), 'jaap.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

config = {
    'development' : DevelopmentConfig,
}