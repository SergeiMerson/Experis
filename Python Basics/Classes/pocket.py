from abc import ABC, abstractclassmethod

class Animal(ABC):
    @classmethod(abstractclassmethod)
    def __init__(self, name, mass):
        self.name = name
        self.mass = mass


class Mammal(Animal):
    def __init__(self,name, mass, litter):
        super().__init__(name, mass)
        self.litter = litter


class Reptile(Animal):
    def __init__(self, name, mass, venomous):
        super().__init__(name, mass)
        self.venomous = venomous


class Bird(Animal):
    def __init__(self, name, mass, wingspan, talks, phrase):
        super().__init__(name, mass)
        self.wingspan = wingspan
        self.talks = talks
        self.phrase = phrase


class Parser:
    def __init__(self, file_path):
        with open(file_path, 'r') as zoo_file:
            zoo_db = zoo_file


file_path = 'Exercises/Classes/zoo_db.txt'
def get_db_generator(file_path):
    with open(file_path, 'r') as zoo_file:
        return zoo_file.readlines()

fff = get_db_generator(file_path)