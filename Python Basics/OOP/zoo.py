from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def __init__(self, name, species, mass):
        self.name = name
        self.species = species
        self.mass = mass

    @staticmethod
    @abstractmethod
    def create(name, species, mass, line_generator):
        pass


class Mammal(Animal):
    def __init__(self, name, species, mass, litter):
        super().__init__(name, species, mass)
        self.litter = litter

    @staticmethod
    def create(line_generator, name, species, mass):
        litter = next(line_generator)[0]
        return line_generator, Mammal(name, species, int(mass), int(litter))


class Reptile(Animal):
    def __init__(self, name, species, mass, venomous):
        super().__init__(name, species, mass)
        self.venomous = venomous

    @staticmethod
    def create(line_generator, name, species, mass):
        venomous = next(line_generator)[0]
        return line_generator, Reptile(name, species, int(mass), venomous)


class Bird(Animal):
    def __init__(self, name, species, mass, wingspan, talks, phrase=None):
        super().__init__(name, species, mass)
        self.wingspan = wingspan
        self.talks = talks
        self.phrase = phrase

    @staticmethod
    def create(line_generator, name, species, mass):
        phrase = None
        next_line = next(line_generator)
        wingspan, talks = int(next_line[0]), next_line[1]
        if talks == 'Talks':
            phrase = ' '.join(next(line_generator))
        return line_generator, Bird(name, species, int(mass), int(wingspan), talks, phrase)


class Parser:
    class_dict = {'Mammal': Mammal, 'Reptile': Reptile, 'Bird': Bird}

    def __init__(self):
        self.catalog = {}

    def line_generator(self, file_path):
        with open(file_path, 'r') as zoo_file:
            for line in zoo_file:
                yield line.strip().split()

    def parse_file(self, file_path):
        line_gen = self.line_generator(file_path)

        while line_gen:
            try:
                line = next(line_gen)
                name, animal_type, species, weight = line[0], line[1], line[2], line[3]
                line_gen, self.catalog[name] = self.class_dict[animal_type].create(line_gen, name, species, weight)
            except StopIteration:
                line_gen = False

    def get_catalog(self):
        return self.catalog


class Zoo:

    def __init__(self):
        self.catalog = {}

    def load_from_file(self, path_to_file):
        parser = Parser()
        parser.parse_file(path_to_file)
        self.catalog = parser.get_catalog()

    def get_animal_property(self, name, property):
        animal = self.catalog[name]
        try:
            answer = getattr(animal, property)
            return answer
        except AttributeError:
            print(f"{animal.name} hasn't such attribute...")
            raise AttributeError


zoo = Zoo()
file_path = 'D:\Projects\ExperisAcademy\Exercises\OOP\zoo_db.txt'
zoo.load_from_file(file_path)

queries = {'s': 'species', 'm': 'mass', 'l': 'litter', 'v': 'venomous', 'w': 'wingspan', 't': 'talks'}
proposal = 'Query animal species[s], mass[m], litter[l], venom[v], wingspan[w], talk[t] or exit session[e]?'
run = True

while run:
    user_answer = input(proposal)
    if user_answer == 'e':
        print('Goodbye!')
        run = False
    elif user_answer in queries.keys():
        property = queries[user_answer]
        name = input('Animal Name?')
        try:
            answer = zoo.get_animal_property(name, property)
            print(f"{name} {property} is {answer}")
        except AttributeError:
            print(f"{name} has no such quality")
        except KeyError:
            print(f"There is no animal called {name}")
