from flask import Flask, request, redirect, url_for, jsonify
from functools import wraps
import pymongo
from Models.apartmentModel import Apartment
from Models.apartmentModel import Book
from Models.userModel import User

application = Flask(__name__)
application.secret_key = "123askldaskfbbaskdkasgjash0120fd17237ajkhafkas"

#Database Conection
client = pymongo.MongoClient("mongodb+srv://admin:shine123@cluster0.ymwcw.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.shineApi

@application.route('/')
def init():
    return jsonify({'Status':'Development Server Init'})

# Routes

@application.route('/user/<string:user>/add-apartment', methods=["POST","GET"])
def apartmentAdd(user):
    return Apartment().Add(user)
    
@application.route('/apartmenst/delete/<string:id>', methods=["GET"])
def apartmentsDelete(id):
    return Apartment().Delete(id)

@application.route('/user/<string:user>/update/<string:id>', methods=["POST","GET"])
def apartmentsUpdate(user, id):
    return Apartment().Update(user, id)


@application.route('/apartment/get-all', methods=["GET"])
def apartmentsReadAll():
    return Apartment().ReadAll()

@application.route('/user/<string:user>/get-apartments', methods=["GET"])
def apartmentsReadUserAll(user):
    return Apartment().ReadAll(user)

@application.route('/apartment/get/<string:id>', methods=["GET"])
def apartmentsReadOne(id):
    return Apartment().ReadOne(id)


@application.route('/apartments/get-available', methods=["GET"])
def apartmentsReadAvailable():
    return Apartment().ReadAvailable()

@application.route('/apartment/active/<string:id>', methods=["GET"])
def apartmentsActive(id):
    return Apartment().Active(id)

@application.route('/apartment/deactivate/<string:id>', methods=["GET"])
def apartmentsDeactivate(id):
    return Apartment().Deactivate(id)


# # Booking routes

@application.route('/user/<string:user>/add-booking/<string:id>', methods=["POST","GET"])
def booksAdd(user, id):
    return Book().Add(user, id)

@application.route('/user/<string:user>/delete-booking/<string:id>', methods=["POST","GET"])
def booksDelete(user, id):
    return Book().Delete(user, id)

@application.route('/user/<string:admin>/my-booked-apartments', methods=["GET"])
def booksGet(admin):
    return Book().Get(admin)

@application.route('/user/<string:client>/mis-reservas', methods=["GET"])
def booksGetMy(client):
    return Book().GetMy(client)


@application.route('/user/login', methods=["POST"])
def userLogin():
    return User().Login()

@application.route('/user/register', methods=["POST"])
def userRegister():
    return User().Register()

@application.route('/user/<string:id>', methods=["GET"])
def userReadOne(id):
    return User().ReadOne(id)

@application.route('/user/update/<string:id>', methods=["POST","GET"])
def userUpdate(id):
    return User().Update(id)


# Initialize Debug Server
if __name__ == "__main__":
    application.run(debug=True)