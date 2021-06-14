from flask import Blueprint, Flask, request, redirect, url_for, jsonify
from Models.apartmentModel import Apartment
from Models.apartmentModel import Book

apartments = Blueprint("apartmentRoutes", __name__)

@apartments.route('/user/<string:user>/add-apartment', methods=["POST","GET"])
def apartmentAdd(user):
    return Apartment().Add(user)
    
@apartments.route('/apartmenst/delete/<string:id>', methods=["GET"])
def apartmentsDelete(id):
    return Apartment().Delete(id)

@apartments.route('/user/<string:user>/update/<string:id>', methods=["POST","GET"])
def apartmentsUpdate(user, id):
    return Apartment().Update(user, id)


@apartments.route('/apartment/get-all', methods=["GET"])
def apartmentsReadAll():
    return Apartment().ReadAll()

@apartments.route('/user/<string:user>/get-apartments', methods=["GET"])
def apartmentsReadUserAll(user):
    return Apartment().ReadAll(user)

@apartments.route('/apartment/get/<string:id>', methods=["GET"])
def apartmentsReadOne(id):
    return Apartment().ReadOne(id)


@apartments.route('/apartments/get-available', methods=["GET"])
def apartmentsReadAvailable():
    return Apartment().ReadAvailable()

@apartments.route('/apartment/active/<string:id>', methods=["GET"])
def apartmentsActive(id):
    return Apartment().Active(id)

@apartments.route('/apartment/deactivate/<string:id>', methods=["GET"])
def apartmentsDeactivate(id):
    return Apartment().Deactivate(id)


# # Booking routes

@apartments.route('/user/<string:user>/add-booking/<string:id>', methods=["POST","GET"])
def booksAdd(user, id):
    return Book().Add(user, id)

@apartments.route('/user/<string:user>/delete-booking/<string:id>', methods=["POST","GET"])
def booksDelete(user, id):
    return Book().Delete(user, id)

@apartments.route('/user/<string:admin>/my-booked-apartments', methods=["GET"])
def booksGet(admin):
    return Book().Get(admin)

@apartments.route('/user/<string:client>/mis-reservas', methods=["GET"])
def booksGetMy(client):
    return Book().GetMy(client)