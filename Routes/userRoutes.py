from flask import Flask, request, redirect, url_for, jsonify
from application import application
from Models.userModel import User

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