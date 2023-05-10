import os

from flask import Flask, jsonify, make_response
from flask_migrate import Migrate
from flask_restful import Api, Resource

from models import db, Profile

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)

api = Api(app)

class Profiles(Resource):

    def get(self):
        profiles = [profile.to_dict() for profile in Profile.query.all()]
        return make_response(jsonify(profiles), 200)

api.add_resource(Profiles, '/profiles')