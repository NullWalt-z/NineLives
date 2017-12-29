import pdb
import unittest
import random
from NineLives.Database import app
from NineLives.Database import db
from NineLives.Classes import *

testPet = Pet('Spot', '10/10/2015', '45', 'M', 'Lab')
testOwner = Owner('Walter', 'Lozier', '06/04/1988', 'United States', 'Missouri', 'Kansas City', '3808 Wyandotte St')

class TestParticipant(unittest.TestCase):
    def setUp(self):
        app.config.from_object('NineLives.config.Testing')
        db.session.close()
        db.reset

    def test_pet_insert(self):
        #Test insert by checking original count and count after attempting an insert
        pet = testPet
        orig_count = session.query(db.PET).count()
        db.session.add(pet)
        new_count = session.query(db.PET).count()
        db.reset()
        assert new_count == (orig_count + 1)

    def test_pet_lookup(self):
        #Test lookup by adding a 'Pet' and checking if 'Pet' is in a query.all()
        pet = testPet
        db.session.add(pet)
        db.session.commit()
        pets = Pet.query.all()
        db.reset()
        assert pet in pets

    def test_owner_insert(self):
        #Test insert by checking original count and count after attempting an insert
        owner = testOwner
        orig_count = session.query(db.OWNER).count()
        db.session.add(owner)
        new_count = session.query(db.PET).count()
        db.reset()
        assert new_count == (orig_count + 1)

    def test_pet_lookup(self):
        #Test lookup by adding a 'Owner' and checking if 'Owner' is in a query.all()
        owner = testOwner
        db.session.add(owner)
        db.session.commit()
        owners = OWNER.query.all()
        db.reset()
        assert owner in owners

    #def test_owner_pet_lookup(self):


        

