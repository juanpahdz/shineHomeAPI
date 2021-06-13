from flask import Flask, request, redirect, url_for, jsonify
from __main__ import application
from Models.apartmentModel import Apartment

@application.route('/apartmenst/get')
def apartmentsget():
    return Apartment().add()