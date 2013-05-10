#!/usr/bin/env python2
# -*- encoding: utf8 -*-

# Links app
import pymongo
import sys
import bottle 
import os
#from datetime import datetime
import json
import bottle
from bottle import route, run, request, abort
from pymongo import Connection

########################example#####################################
#http://localhost:8080/documents/test@google.com
#python server.py
############################################

# connnecto to the db on standard port
def insert():
    connection = pymongo.Connection("mongodb://localhost", safe=True)
    db = connection.moocdb  # attach to db

    usercollection = db.usercollection  # specify the colllection
    #print usercollection.find({ 'email': 'test@google.com'})
    
    try:
        usercollection.insert({ 'email': 'test12121@google.com'}) 
    # db.usercollection.insert({email:'test1@test.com'})
    except:
        print "Unexpected error:" ,sys.exc_info()[0]

#insert()

@route('/documents/:id', method='GET')
def get_document(id):
  
    connection = pymongo.Connection("mongodb://localhost", safe=True)
    db = connection.moocdb  # attach to db

    usercollection = db.usercollection  # specify the colllection
    #print usercollection.find({ 'email': 'test@google.com'})
    entity = usercollection.find_one({'email':id})
    if not entity:
        abort(404, 'No document with id %s' % id)
    return entity['own']
        
 
run(host='localhost', port=8080)

