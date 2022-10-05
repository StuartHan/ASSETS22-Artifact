from flask import Flask

from .routes import *
from app.routes.events import socketio

def create_app(ssl_context=None, debug=True, port=443):

    app = Flask(__name__)
    app.debug = debug
    app.port = port
    app.ssl_context = ssl_context
    app.host = '0.0.0.0'
    app.register_blueprint(routes)
    # socketio.init_app(app, cors_allowed_origins="*")

    # TEST CODE
    # try:
	# 	return send_file('/home/ubuntu/backend-healthdata-Yichen/figures/placeholder.jpg', attachment_filename='placeholder.jpg')
	# except Exception as e:
	# 	return str(e)

    app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
    return app

