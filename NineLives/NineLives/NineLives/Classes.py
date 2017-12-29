import string

class Pet(object):
    #attributes
    name =''
    birthday = '//'
    weight =''
    gender = ''
    breed = ''

    #initilizer
    def __init__(self,name,birthday,weight,gender,breed):
        self.name = name
        self.birthday = birthday
        self.weight = weight
        self.gender = gender
        self.breed = breed

    #getters/setters
    def getName():
        return self.name
    def getBirthday():
        return self.birthday
    def getWeight():
        return self.weight
    def getGender():
        return self.gender
    def getBreed():
        return self.breed
    def setName(name):
        self.name = name
    def setBirthday(birthday):
        self.birthday = birthday
    def setWeight(weight):
        self.weight = weight
    def setGender(gender):
        self.gender = gender
    def setBreed(breed):
        self.breed = breed

class Owner(object):
    #attributes
    first_name =''
    last_name =''
    birthday =''
    country =''
    state =''
    city =''
    street_add =''

    #initilizer
    def __init__(self,first_name,last_name,birthday,country,state,city,street_add):
        self.first_name = first_name
        self.last_name = last_name
        self.birthday = birthday
        self.country = country
        self.state = state
        self.city = city
        self.street_add = street_add

    #getters/setters
    def getFirstName():
        return self.first_name
    def getLastName():
        return self.last_name
    def getBirthday():
        return self.birthday
    def getCountry():
        return self.country
    def getState():
        return self.state
    def getCity():
        return self.city
    def getStreetAdd():
        return self.street_add
    def setFirstName(first_name):
        self.first_name = first_name
    def setLastName(last_name):
        self.last_name = last_name
    def setBirthday(birthday):
        self.birthday = birthday
    def setCountry(country):
        self.country = country
    def setState(state):
        self.state = state
    def setCity(city):
        self.city = city
    def setStreetAdd(street_add):
        self.street_add = street_add




