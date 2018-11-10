from flask_restful import Resource
from .models import Parcel
from flask import request

parcel_obj = Parcel()


class GenericParcel(Resource):
    """This class contains generic parcels without
    any specificity."""

    def get(self):
        parcels = parcel_obj.get_all()
        if parcels == []:
            return {"Message": "There seem to be no deliveries."}, 200
        return parcels, 200

    def post(self):
        """This method is for adding a delivery to our database."""

        data = request.get_json()
        sender = data['sender']
        recipient = data['recipient']
        destination = data['destination']
        weight = data['weight']
        pickup = data['pickup']

        # we shall send this oject to the models and await a response
        response = parcel_obj.add_parcel(sender, recipient,
                                         destination, weight, pickup)
        if response == 201:
            return {"Success": "Successfully added your delivery"}, 201
