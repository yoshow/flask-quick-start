# -*- coding: utf-8 -*-

import logging
from logging.handlers import RotatingFileHandler

from flask import Flask, make_response, redirect, session, Response, json
from flask_restful import Api
from flask_cors import CORS
from flask_cas import CAS, login_required
import requests

from packages.membership.models.account import db
from packages.membership.apis.account_api import AccountAPI
from packages.membership.apis.role_api import RoleAPI


app = Flask(__name__, static_url_path='', instance_relative_config=True)
# load config from config.py
app.config.from_pyfile('config.py')

# 处理跨域问题
CORS(app)

# only init db at first time
#@app.before_first_request
#def create_database():
#    db.create_all()


# db initialization
db.init_app(app)
# db.create_all(app=app)

cas = CAS(app, '/cas')


@app.route('/')
def index():
    return app.send_static_file('index.html')

# API routing
api = Api(app)

api.add_resource(AccountAPI, 
    '/api/membership/account',
    '/api/membership/account/<string:id>')

api.add_resource(RoleAPI, 
    '/api/membership/role',
    '/api/membership/role/<string:id>')

from .app.applications import blueprint as api_blueprint
app.register_blueprint(api_blueprint, url_prefix='/api/v1')

if __name__ == '__main__':
    host = app.config.get('APP_HOST', '127.0.0.1')
    port = app.config.get('APP_PORT', 10000)

    # set web access log
    access = logging.getLogger('werkzeug')
    access_handler = RotatingFileHandler("logs/access.log", maxBytes=500000, backupCount=2)
    access.addHandler(access_handler)
    app.run(host=host, port=port, threaded=True)
