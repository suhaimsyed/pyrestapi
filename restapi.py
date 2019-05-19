from flask import Flask

from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

addresses = [
    {
        "id": "1",
        "streetName": "Pirates Street",
        "streetNumber": "1",
        "postalCode": "12345",
        "city": "sea",
    },
    {
        "id": "2",
        "streetName": "Corleone, Street",
        "streetNumber": "100",
        "postalCode": "22222",
        "city": "Sicily,",
    },
    {
        "id": "3",
        "streetName": "Washington Street",
        "streetNumber": "999",
        "postalCode": "323232",
        "city": "Philadelphia",
    }
]

def getAddress(id):
    for address in addresses:
        if (id == address["id"]):
            return address



users = [
    {
        "id": "1",
        "name": "Jack Sparrow",
        "billingAddress": getAddress("1"),
        "shippingAddress": getAddress("1")
    },
    {
        "id": "2",
        "name": "Vito Corleone",
        "billingAddress": getAddress("2"),
        "shippingAddress": getAddress("2")
    },
    {
        "id": "3",
        "name": "Rocky",
        "billingAddress": getAddress("3"),
        "shippingAddress": getAddress("3")
    }
]

class Addresses(Resource):
    def get(self):
        return addresses

class Address(Resource):
    def get(self, id):
        for address in addresses:
            if (id == address["id"]):
                return address, 200
        return "Address not found", 404
    def post(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument("streetName")
        parser.add_argument("streetNo")
        parser.add_argument("city")
        parser.add_argument("postalCode")
        args = parser.parse_args()

        for address in addresses:
            if (id == address["id"]):
                return "Address with id {} already exists".format(id), 400

        address = {
            "id": id,
            "streetName": args["streetName"],
            "streetNo": args["streetName"],
            "city": args["city"],
            "postalCode": args["postalCode"]
        }
        addresses.append(address)
        return address, 201
    def delete(self, id):
        global addresses
        addresses = [address for address in addresses if addresses["id"] != id]
        return "{} is deleted. or is not present".format(id), 200

class Users(Resource):
    def get(self):
        return users

class User(Resource):
    def get(self, id):
        for user in users:
            if (id == user["id"]):
                return user, 200
        return "User not found", 404

    def post(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument("name")
        parser.add_argument("billingAddress")
        parser.add_argument("shippingAddress")
        args = parser.parse_args()

        for user in users:
            if (id == user["id"]):
                return "User with name {} already exists".format(id), 400

        user = {
            "id": id,
            "name": args["name"],
            "billingAddress": getAddress(args["billingAddress"]),
            "shippingAddress": getAddress(args["shippingAddress"]),
        }
        users.append(user)
        return user, 201


    def delete(self, id):
        global users
        users = [user for user in users if user["id"] != id]
        return "{} is deleted. or is not present".format(id), 200


api.add_resource(User, "/user/<string:id>")

api.add_resource(Users,"/users")

api.add_resource(Address,"/address/<string:id>")

api.add_resource(Addresses,"/addresses")

app.run(host='0.0.0.0')
