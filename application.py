from flask import Flask, request, redirect, url_for, jsonify
from functools import wraps
import pymongo
from Routes.userRoutes import users
from Routes.apartmentRoutes import apartments

application = Flask(__name__)
application.secret_key = "123askldaskfbbaskdkasgjash0120fd17237ajkhafkas"

application.register_blueprint(apartments)
application.register_blueprint(users)

#Database Conection
client = pymongo.MongoClient("mongodb+srv://admin:shine123@cluster0.ymwcw.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.shineApi

@application.route('/')
def init():
    return jsonify({'Status':'Development Server Init'})

# Routes


# Initialize Debug Server
if __name__ == "__main__":
    application.run(debug=True)