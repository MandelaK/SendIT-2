# This is our models file where we store our temporary storage data and methods
# to manipulate the data. Our parcels list is globally available all classes
# that inherit the Parcel class

# this is where all our parcels will be appended
parcels = [
    {
        "id": 1,
        "sender": "Keith",
        "recipient": "Juma",
        "destination": "Nairobi",
        "weight": "500",
        "pickup": "Ruiru",
        "location": "Ruiru",
        "status": "pending"
    }, {
        "id": 2,
        "sender": "John",
        "recipient": "Steve",
        "destination": "Kiambu",
        "weight": "920",
        "pickup": "Naivasha",
        "location": "Naivasha",
        "status": "pending"
    }, {
        "id": 3,
        "sender": "Kris",
        "recipient": "Peter",
        "destination": "Vihiga",
        "weight": "900",
        "pickup": "Kericho",
        "location": "Vihiga",
        "status": "delivered"
    }
]


class Parcel(object):
    """This is the parcel class"""

    def __init__(self):
        self.db = parcels
        self.status = 'pending'

    def add_parcel(self, sender, recipient, destination, weight, pickup):
        """The method to create a delivery and append
            it to our list"""

        # we check the request object the user sends to
        # validate it has enough information then add to payload

        data = {
            'id': len(parcels) + 1,
            'sender': sender,
            'recipient': recipient,
            'destination': destination,
            'weight': weight,
            'pickup': pickup,
            'location': pickup,
            'status': self.status
        }

        self.db.append(data)
        return 201
