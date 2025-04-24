class Animal:
    def move(self):
        pass  # To be implemented by subclasses

class Dog(Animal):
    def move(self):
        return "Running on four legs 🐾"

class Bird(Animal):
    def move(self):
        return "Flying in the sky 🕊️"

class Fish(Animal):
    def move(self):
        return "Swimming in water 🐟"

# Example usage
animals = [Dog(), Bird(), Fish()]

for animal in animals:
    print(animal.move())