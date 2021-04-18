#import flask AND important modules / extantions

from flask import Flask
from dotenv import load_dotenv
import config
import os

# create app object
app = Flask(__name__)

# Environment Configurations

APP_ROOT = os.path.join(os.path.dirname(__file__), "..")
dotenv_path = os.path.join(APP_ROOT, ".env")
load_dotenv(dotenv_path)

app.config.from_object('config.settings.' + os.environ.get("ENV"))

