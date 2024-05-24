#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, name="Fido", breed="Pug"):
        self._name = None
        self._breed = None
        self.name = name
        self.breed = breed
    
    def set_name(self, dog_name):
        if isinstance(dog_name, str) and 1 <= len(dog_name) <= 25:
            self._name = dog_name
        else:
            print("Name must be string between 1 and 25 characters.")

    def get_name(self):
        return self._name
    
    def set_breed(self, dog_breed):
        if dog_breed in APPROVED_BREEDS:
            self._breed = dog_breed
        else:
            print("Breed must be in list of approved breeds.")
    
    def get_breed(self):
        return self._breed

    
    name = property(get_name, set_name)
    breed = property(get_breed, set_breed)


