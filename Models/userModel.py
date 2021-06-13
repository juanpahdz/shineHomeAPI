from flask import Flask, jsonify, request, redirect, url_for, session
from passlib.hash import pbkdf2_sha256
from __main__ import db
import uuid

class User:

    def Register(self):
        name = request.json['name']
        email = request.json['email']
        country = request.json['country']
        city = request.json['city']
        password = request.json['password']
        description = request.json['description']

        if name and email and country and city and password:

            user = {
                '_id': uuid.uuid4().hex,
                'name': name,
                'email': email,
                'country': country,
                'city': city,
                'password': password,
                'description': description,
                }

            user["password"] = pbkdf2_sha256.encrypt(user['password'])

            if db.users.find_one({"email": user["email"]}):
                return jsonify({"error": "Ese email ya esta registrado"}), 400

            if db.users.insert_one(user):
                del user["password"]
                return user
    
            return jsonify({'error':'El registro fallo, por favor intenta mas tarde'}), 400

        return jsonify({'error':'necesitas llenar todos los datos antes de enviar'}), 400


    def Login(self):
        user = db.users.find_one({"email": request.json['email'] })
        if user and pbkdf2_sha256.verify(request.json['password'], user['password']):
            del user["password"]
            return jsonify(user)

        return jsonify({ "error": "Usuario o contraseña incorrectas" }), 401

    def ReadOne(self, id):
        query = {"_id": id}
        user = db.users.find_one(query)
        del user["password"]
        return jsonify(user)
    
    def Update(self, id):
        name = request.json['name']
        country = request.json['country']
        city = request.json['city']
        password = request.json['password']
        description = request.json['description']

        if db.users.find_one({"_id": id}):
            if name and country and city and password:

                query = {"_id": id}
                newvalues = {"$set":{"name":name,"country":country,"city":city,"description":description}}
                db.users.update_one(query,newvalues)

                return jsonify({'status':'Usuario Actualizado Con Exito'})

            return jsonify({'Status':'Ups... Algo salio mal'})

        return jsonify({'Status':'Ups... Parece que el usuario no existe'})