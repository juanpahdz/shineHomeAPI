from flask import Flask, request, redirect, url_for, jsonify
from __main__ import application
from Models.userModel import User

@application.route('/user/signup')
def usersignup():
    return User().signout()