import animal
from animal import Animal, Tigers, Lions, Bears

class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name
    def add_lion(self, name):
        self.animals.append(Lions(name))
    def add_tiger(self, name):
        self.animals.append(Tigers(name))
    def add_bear(self, name):
        self.animals.append(Bears(name))
    def feed_all(self, val):
        for animal in self.animals:
            animal.feed(val)
    def play_all(self, val):
        for animal in self.animals:
            animal.play(val)
    def print_all_info(self):
        print("-"*30, self.name, "-"*30)
        for animal in self.animals:
            animal.display()
    # def feed(self, type, val):
    #     if type == "tiger":
      #       tigers.feed_tiger(val)
      #       animal.display()
zoo1 = Zoo("Emilie's Zoo")
zoo1.add_lion("Nala")
zoo1.add_lion("Simba")
zoo1.add_tiger("Rajah")
zoo1.add_tiger("Shere Khan")
zoo1.add_bear("Winnie the pooh")
zoo1.feed_all(10)
zoo1.play_all(10)
zoo1.print_all_info()
zoo1.feed("tiger", "rabbit")
