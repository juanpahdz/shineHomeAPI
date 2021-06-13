from flask import Flask, jsonify, request, redirect, url_for, session
from passlib.hash import pbkdf2_sha256
from __main__ import db
import uuid

class Apartment:

    def add(self):
        return jsonify({'Status':'Apartment Working'})