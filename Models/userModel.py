from flask import Flask, jsonify, request, redirect, url_for, session
from passlib.hash import pbkdf2_sha256
from __main__ import db
import uuid

class User:

    def signout(self):
        return jsonify({'Status':'User SignOut'})