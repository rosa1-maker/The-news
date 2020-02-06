from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options
# from flask import Blueprint
# main = Blueprint('main', __name__)
# # from app.main import Views,errors


bootstrap = Bootstrap()

def create_app(config_name):
    app = Flask(__name__)

    app.config.from_object(config_options[config_name])

    bootstrap.init_app(app)

    from.main import main as main_blueprint
    app.register_blueprint(main_blueprint)
   
    from.request import configure_request
    configure_request(app)


    return app


