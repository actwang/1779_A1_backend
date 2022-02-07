from flask import Flask
from config import Config

from app.routes.route_test import test_blueprint

app = Flask(__name__)
app.config.from_object(Config)

app.register_blueprint(test_blueprint)
