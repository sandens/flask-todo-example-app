from flask import Flask
import os
from logging.config import dictConfig
from app.views import frontend
from flask_bootstrap import Bootstrap
from .nav import nav
from flask_appconfig import AppConfig
from flask_sqlalchemy import SQLAlchemy
from .db import init_db
from .models import db

def create_app():
    app = Flask(__name__)

    ## Init logging level
    LOG_LEVEL=os.environ.get("LOG_LEVEL","INFO")

    dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'stdout': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://sys.stdout',
        'formatter': 'default'
    }},
    'root': {
        'level': LOG_LEVEL,
        'handlers': ['stdout']
    }
    })

    AppConfig(app)

    project_dir = os.path.dirname(os.path.abspath(__file__))
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///{}".format(os.path.join(project_dir, "todos.db"))
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Install our Bootstrap extension
    Bootstrap(app)
    app.register_blueprint(frontend)
     
    db.init_app(app) 
    init_db()

    with app.app_context():
        db.create_all()

    nav.init_app(app)
    return app


    #app.run("localhost",debug=True)