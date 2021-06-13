from flask import Flask, request, redirect, url_for, jsonify
from __main__ import application
from Models.apartmentModel import Apartment
from Models.apartmentModel import Book

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