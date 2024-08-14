class Animal:
    def __init__(self, name, sound, drink, food, sleep):
        self.name = name
        self.sound = sound
        self.drink = drink
        self.food = food  # Renamed from eat to food
        self.sleep = sleep
     
    def eat(self):
        return f"{self.name} is eating {self.food}."

class Cat(Animal):
    def __init__(self, name, sound, drink, food, sleep):
        super().__init__(name, sound, drink, food, sleep)

    def meow(self):
        return f"{self.name} says {self.sound}!"

    def eat(self):
        return f"{self.name} is eating {self.food}. Yummy!"

# Create a new Cat object
newCat = Cat(name="Whiskers", sound="Meow", drink="Water", food="Fish", sleep="12 hours")

# Print the sound the cat makes
print(newCat.meow())       # Output: Whiskers says Meow!
print(newCat.eat())        # Output: Whiskers is eating Fish. Yummy!
