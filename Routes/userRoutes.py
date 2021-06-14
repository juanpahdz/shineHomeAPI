from flask import Flask, request, redirect, url_for, jsonify, Blueprint
from Models.userModel import User

users = Blueprint("users", __name__)

@users.route('/user/login', methods=["POST"])
def userLogin():
    return User().Login()

@users.route('/user/register', methods=["POST"])
def userRegister():
    return User().Register()

@users.route('/user/<string:id>', methods=["GET"])
def userReadOne(id):
    return User().ReadOne(id)

@users.route('/user/update/<string:id>', methods=["POST","GET"])
def userUpdate(id):
    return User().Update(id)