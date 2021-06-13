from flask import Flask, jsonify, request, redirect, url_for, session
from passlib.hash import pbkdf2_sha256
from bson.json_util import dumps
from __main__ import db
import uuid
import json

class Apartment:

    def VerifyUser(self, user):
        if db.users.find_one({"_id": user}):
            return True
        return False
    
    def VerifyApartment(self, id):
        if db.apartments.find_one({"_id": id}):
            return True
        return False

    def Add(self, user):

        title = request.json['title']
        price = request.json['price']
        rooms = request.json['rooms']
        city = request.json['city']
        country = request.json['country']
        adress = request.json['adress']
        thumbnail = request.json['thumbnail']
        images = request.json['images']
        excerpt = request.json['excerpt']
        
        if self.VerifyUser(user):
            if title and price and city and country and adress and thumbnail and excerpt:
                apartment = {
                '_id': uuid.uuid4().hex,
                'title': title,
                'price': price,
                'rooms': rooms,
                'city': city,
                'country': country,
                'adress': adress,
                'thumbnail': thumbnail,
                'images': images,
                'excerpt': excerpt,
                'admin': user,
                'state': True,
                }

                if db.apartments.insert_one(apartment):
                    return apartment

                return jsonify({'error':'Ups.. Algo Salio Mal'})

            return jsonify({'error':'Debes completar todos los campos antes de enviar'})

        return jsonify({'error':'Ups.. Parece que hay un error de autentificacion'})

    
    def Delete(self, id):

        if self.VerifyApartment(id):
            query = {"_id": id}
            db.apartments.delete_one(query)
            return jsonify({'status':'El Registro ' + id + " fue eliminado correctamente"})

        return jsonify({'error':'Ups.. Parece que este inmueble no existe'})

    
    def Update(self, user, id):

        title = request.json['title']
        price = request.json['price']
        rooms = request.json['rooms']
        city = request.json['city']
        country = request.json['country']
        adress = request.json['adress']
        thumbnail = request.json['thumbnail']
        excerpt = request.json['excerpt']

        if self.VerifyApartment(id) and self.VerifyUser(user):
            query = {"_id": id}
            newvalues = {"$set":{"title":title,"price":price,"rooms":rooms,"city":city,"country":country,"adress":adress,"thumbnail":thumbnail,"excerpt":excerpt}}
            db.apartments.update_one(query,newvalues)

            return  jsonify({'status':'Apartamento actualizado'})

        return jsonify({'error':'Ups.. Algo Salio Mal Con la Autentificacion'})
    
    def ReadAll(self, user):
        if user:
            apartments = dumps(db.apartments.find({"admin": user} ))

            return apartments

        else: 
            apartments = dumps(db.apartments.find()) 
            return apartments

    def ReadOne(self, id):
        apartment = db.apartments.find_one({"_id": id} )
        return jsonify(apartment)
    
    def ReadAvailable(self):
        apartments = dumps(db.apartments.find({"state": True} ))
        return apartments
    
    def Active(self, id):
        query = {"_id": id}
        newvalues = {"$set":{"state": True}}
        db.apartments.update_one(query,newvalues)

        return jsonify({'Status':'Now is activated'})
    
    def Deactivate(self, id):
        query = {"_id": id}
        newvalues = {"$set":{"state": False}}
        db.apartments.update_one(query,newvalues)

        return jsonify({'Status':'Now is Deactivated'})

class Book:
    def VerifyBooking(self, id):
        if db.books.find_one({"_id": id}):
            return True
        return False
        
    def Add(self, user, id):

        ingreso = request.json['ingreso']
        salida = request.json['salida']
        apartment = db.apartments.find_one({"_id": id})
        userData = db.users.find_one({"_id": user})
        adminData = db.users.find_one({"_id": apartment["admin"]})

        if Apartment().VerifyApartment(id) and Apartment().VerifyUser(user):
            book = {
                '_id': uuid.uuid4().hex,
                'ingreso': ingreso,
                'salida': salida,
                'admin': adminData,
                'client': userData,
                'apartment': apartment
            }

            if db.books.insert_one(book):
                Apartment().Deactivate(id)
                return book

            return jsonify({'error':'Ups.. Algo Salio Mal'})

        return jsonify({'Status':'Ups.. Algo Salio Mal Con la Autentificacion'})
    
    def Delete(self, user, id):
        
        if self.VerifyBooking(id):
            book = db.books.find_one({"_id": id})

            if user == book["client"]["_id"]:
                query = {"_id": id}
                db.books.delete_one(query)
                Apartment().Active(id)
                return jsonify({'status':'La Reserva ' + id + " fue eliminada correctamente"})

            return jsonify({'status':"Ups.. Parece que los datos no coinciden"})

        return jsonify({'error':'Ups.. Parece que esta reserva no existe'})
    
    def Get(self, admin):
        book = dumps(db.books.find({"admin._id": admin}))
        return book
    
    def GetMy(self, client):
        book = dumps(db.books.find({"client._id":client}))
        return book