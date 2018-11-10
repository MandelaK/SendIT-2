from .views import GenericParcel, User, SpecificParcel, Admin, Cancel
from flask import Blueprint
from flask_restful import Api

version1 = Blueprint('v1', __name__, url_prefix='/api/v1')
api = Api(version1)

api.add_resource(GenericParcel, '/parcels')
api.add_resource(User, '/users/<string:id>/parcels')
api.add_resource(SpecificParcel, '/parcels/<int:id>')
api.add_resource(Admin, '/admin/location/<int:id>')
api.add_resource(Cancel, '/parcels/<int:id>/cancel')
