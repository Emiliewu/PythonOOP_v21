class Pet:
# implement __init__( name , type , tricks ):
    def __init__(self, name, type, tricks):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 0
        self.energy = 0
  # implement the following methods:
  # sleep() - increases the pets energy by 25
    def sleep(self):
        self.energy += 25
        print(f"take a nap and energy level increased to {self.energy}")
      
  # eat() - increases the pet's energy by 5 & health by 10
    def eat(self):
        self.energy += 5
        self.health += 10
        print(f"after eating the energy level increased to {self.energy} and health increased to {self.health}")

  # play() - increases the pet's health by 5
    def play(self):
        self.health += 5
        print(f"after playing the pet's health increased to {self.health}")
  # noise() - prints out the pet's sound
    def noise(self):
        print(f"the pet makes {self.tricks}")

class Dog(Pet):
    def __init__(self, name, type, tricks):
        super().__init__(name, type, tricks)

    def eat(self):
        self.energy += 15
        self.health +=25
        print(f"after eating the energy level increased to {self.energy} and health increased to {self.health}")  
    