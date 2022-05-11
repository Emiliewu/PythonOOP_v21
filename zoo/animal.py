class Animal:
    def __init__(self, name, weight = 0, age = 0, health = 0, happiness = 0):
        self.name = name
        self.weight = weight
        self.age = age
        self.health = health
        self.happiness = happiness

    def feed(self, val):
        self.weight += 10
        self.health += val
        return self
        
    def play(self, val):
        self.happiness += val
        return self

    def display(self):
        print("Name:{} Weight:{} Age:{} Health:{} Happiness:{} ". format(self.name, self.weight, self.age, self.health, self.happiness))

class Tigers(Animal):
    def __init__(self, name, weight = 0, age = 0, health = 0, happiness = 0):
        super().__init__(name, weight, age, health, happiness)
    def feed(self, val):
        if val == "rabbit":
            val = 100
        else:
            val = 10
        super().feed(val)
        return self
    def play(self, val):
        if val == "ball":
            val = 100
        else:
            val = 10
        super().play(val)
        return self

class Lions(Animal):
    def __init__(self, name, weight = 0, age = 0, health = 0, happiness = 0):
        super().__init__(name, weight, age, health, happiness)
    def feed(self, val):
        if val == "beef":
            val = 100
        else:
            val = 10
        super().feed(val)
        return self
    def play(self, val):
        if val == "water":
            val = 100
        else:
            val = 10
        super().play(val)
        return self

class Bears(Animal):
    def __init__(self, name,  weight = 0, age = 0, health = 0, happiness = 0):
        super().__init__(name, weight, age, health, happiness)
    def feed(self, val):
        if val == "honey":
            val = 100
        else:
            val = 10
        super().feed(val)
        return self
    def play(self, val):
        if val == "piglet":
            val = 100
        else:
            val = 10
        super().play(val)
        return self

# tiger1 = Tigers("TT", 1, 10)
# lion1 = Lions("Simba", 10, 1, 10, 10)
# bear1 = Bears("Winnie", 10, 1, 10, 10)

# tiger1.feed("something").play("something").display()