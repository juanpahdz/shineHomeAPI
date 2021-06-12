from flask import Flask, request, redirect, url_for, jsonify
from functools import wraps
import pymongo

application = Flask(__name__)
application.secret_key = "123askldaskfbbaskdkasgjash0120fd17237ajkhafkas"

#Database Conection
client = pymongo.MongoClient('mongodb://admin:shine123@cluster0.ymwcw.mongodb.net/')
db = client.shineApi

@application.route('/')
def home():
    return jsonify({'Status':'Development Server Init'})

if __name__ == "__main__":
    application.run(debug=True)