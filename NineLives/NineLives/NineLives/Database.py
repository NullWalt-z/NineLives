from flask import Flask
from flask.ext.bcrypt import Bcrypt
from flask_sqlalchemy import *
from flask_sqlalchemy import SQLAlchemy
from NineLives import app
from datetime import date
from datetime import datetime
from datetime import time

app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:0000@localhost/NineLives'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db = SQLAlchemy(app)

class OWNER(db.Model):
    __tablename__ = 'OWNER'

    #primary key
    owner_id = db.Column(db.Integer,primary_key = True)

    #data columns
    email = db.Column(db.String(80))
    #PASSWORD - FIGURE OUT SQLALCHEMY ENCRYPTION 
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    birthday = db.Column(db.Date)
    county = db.Column(db.String(80)) 
    state = db.Column(db.String(80)) #also used for province etc.
    city = db.Column(db.String(80))
    street_add = db.Column(db.String(80))

    #relationships
    db.relationship('OWNER_PETS',backref='OWNER')

    

    #function definitions
    def __repr__(self):
        return '<OWNER %r %r>' %self.first_name %self.last_name
    def __init__(self,first_name,last_name,country,state,city,street_add):
        self.first_name = first_name
        self.last_name = last_name
        self.county = country
        self.state = state
        self.city = city
        self.city = street_add

class PET(db.Model):
    __tablename__ = 'PET'
    
    #primary key
    id = db.Column(db.Integer,primary_key = True,autoincrement = True)

    #foreign key columns
    owner_id = db.Column(db.Integer, db.ForeignKey('OWNER.owner_id'), nullable=False)
    breed = db.Column(db.Integer, db.ForeignKey('BREED.breed_id'), nullable=False)

    #data columns
    name  = db.Column(db.String(80), nullable=False)
    birthday = db.Column(db.Date)
    weight = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(1), nullable = False)

    #relationships
    db.relationship('OWNER_PETS',backref='PET')
    db.relationship('NIGHTLY_SLEEP',backref='PET')
    db.relationship('DAILY_EXERCISE',backref='PET')
    db.relationship('PET_CONDITION',backref='PET')
    db.relationship('BREED',backref='PET')
    db.relationship('MEALS',backref='PET')

    #function definitions
    def __repr__(self):
        return '<PET %r>' % self.name
    def __init__(self,name,birthday,weight,gender):
        self.name = name
        self.birthday = birthday
        self.weight = weight
        self.gender = gender

class OWNER_PETS(db.Model):
    #primary key
    #id = db.Column(db.Integer, autoincrement = True, primary_key = True)
    owner_id = db.Column(db.Integer, unique = True, primary_key = True)
    pet_id = db.Column(db.Integer, primary_key = True)

    #relationshios
    db.relationship('OWNER', backref='OWNER_PETS')

    #function definitions
    def __repr__(self):
        return '<OWNER_PETS %r %r>' %self.owner_id %self.pet_id
    def __init__ (self, owner_id, pet_id):
        self.owner_id = owner_id
        self.pet_id = pet_id

class NIGHTLY_SLEEP(db.Model):
    __tablename__ = 'NIGHTLY_SLEEP'

    #primary key
    pet_id = db.Column(db.Integer, primary_key = True)
    start_datetime = db.Column(db.DateTime, primary_key = True)

    #data columns
    end_datetime = db.Column(db.DateTime)
    hours = db.column(db.Integer)

    #relationships
    db.relationship('PET',backref='NIGHTLY_SLEEP')

    #functions definitions
    def __repr__(self):
        return '<NIGHTLY_SLEEP %r %r>' %self.date %self.hours
    def __init__(self,pet_id,date,state_time,end_time,hours):
        self.pet_id_id = pet_id
        self.date = date
        self.start_time = start_time
        self.end_time = end_time
        self.hours = hours

class DAILY_EXERCISE(db.Model):
    __tablename__ = 'DAILY_EXERCISE'

    #primary key
    pet_id = db.Column(db.Integer, primary_key = True) #foreign key
    datetime = db.Column(db.DateTime)

    #data columns
    heartrate = db.Column(db.Integer)

    #relationships
    db.relationship('PET',backref='DAILY_EXERCISE')

    #function definitions
    def __repr__(self):
        return '<DAILY EXERCISE %r %r %r>' %self.pet_id %self.datetime %self.heartrate
    def __init__(self,pet_id,datetime,heartrate):
        self.pet_id = pet_id
        self.datetime = datetime
        self.heartrate = heartrate

class MEALS(db.Model):
    __tablename__ = 'MEALS'

    #primary key
    pet_id = db.Column(db.Integer, primary_key = True)
    datetime = db.Column(db.DateTime, primary_key = True)
    
    #data columns
    calories = db.Column(db.Integer)

    #function definitions
    def __init__(self, pet_id, datetime):
        self.pet_id = pet_id
        self.datetime = datetime
    
class PET_CONDITION(db.Model):
    __tablename__ = 'PET_CONDITION'

    #primary key
    pet_id = db.Column(db.Integer, primary_key = True) #foreign key
    condition_id = db.Column(db.Integer)

    #relationships
    db.relationship('PET',backref='PET_CONDITION')
    db.relationship('MEDICAL_CONDITION',backref='PET_CONDITION')

    #function definitions
    def __repr__(self):
        return '<PET_CONDITION %r %r>' %self.pet_id %self.condition_id
    def __init__(self,pet_id,condition_id):
        self.pet_id = pet_id
        self.condition_id = condition_id

class MEDICAL_CONDITION(db.Model):
    __tablename__ = 'MEDICAL_CONDITION'

    #primary key
    condition_id = db.Column(db.Integer, primary_key = True) #foreign key
    condition_name = db.Column(db.String(80))

    #relationships
    db.relationship('PET_CONDITION',backref='MEDICAL_CONDITION')

    #function definitions
    def __repr__(self):
        return '<MEDICAL_CONDITION %r>' %self.condition_name
    def __init__(self, condition_id, condition_name):
        self.condition_id = condition_id
        self.condition_name = condition_name

class BREED(db.Model):
    __tablename__ = 'BREED'

    #primary key
    breed_id = db.Column(db.Integer, primary_key = True)
    
    #data column
    breed_name = db.Column(db.String(80))

    #relationships
    db.relationship('PET',backref='BREED')

    #function definitions
    def __repr__(self):
        return '<BREED %r>' %self.breed_name
    def __init__(self, breed_id, breed_name):
        self.breed_id = breed_id
        self.breed_name = breed_name


#FUNCTION TO READ IN BREEDS AND CONDITIONS AND POPULATE TABLES
#def addRawData():
    


def resetDB():
    db.drop_all()
    db.create_all()

