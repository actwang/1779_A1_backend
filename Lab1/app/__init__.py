from flask import Flask
from config import Config
from app.routes.route_test import test_blueprint

global memcache  # memcache
global memcache_stat  # statistic of the memcache

backendapp = Flask(__name__)
backendapp._static_folder = Config.IMAGE_PATH
backendapp.config.from_object(Config)

memcache = {}
memcache_stat = {}
memcache_stat['hit'] = 0
memcache_stat['mis'] = 0
memcache_stat['total'] = 0

app.register_blueprint(test_blueprint)
