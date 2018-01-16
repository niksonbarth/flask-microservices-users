# project/__init__.py


import os
# import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS


# instantiate the app
app = Flask(__name__)


# instantiate the db
db = SQLAlchemy()


def create_app():

    # instantiate the app
    app = Flask(__name__)

    # enable CORS
    CORS(app)

    # set config
    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)

    # set up extensions
    db.init_app(app)

    # register blueprints
    from project.api.views import users_blueprint
    app.register_blueprint(users_blueprint)

    return app

# #### old
# # set config
# app_settings = os.getenv('APP_SETTINGS')
# app.config.from_object(app_settings)

# # instantiate the db
# db = SQLAlchemy(app)

# # model
# class User(db.Model):
#     __tablename__ = "users"
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     username = db.Column(db.String(128), nullable=False)
#     email = db.Column(db.String(128), nullable=False)
#     active = db.Column(db.Boolean(), default=False, nullable=False)
#     created_at = db.Column(db.DateTime, nullable=False)

#     def __init__(self, username, email):
#         self.username = username
#         self.email = email
#         self.created_at = datetime.datetime.utcnow()


# # routes

# @app.route('/ping', methods=['GET'])
# def ping_pong():
#     return jsonify({
#         'status': 'success',
#         'message': 'pong!'
#     })
