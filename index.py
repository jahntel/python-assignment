class Superhero:
    def __init__(self, name, power, weakness):
        self.name = name
        self.power = power
        self.weakness = weakness
    
    def display_identity(self):
        return f"I'm {self.name}! My superpower is {self.power}."

class FlyingSuperhero(Superhero):
    def __init__(self, name, power, weakness, flight_speed):
        super().__init__(name, power, weakness)
        self.flight_speed = flight_speed

    def display_identity(self):
        return f"I'm {self.name}! My superpower is {self.power}."

# Example usage
hero1 = Superhero("flash", "speed", "lightning")
hero2 = FlyingSuperhero("super man", "strenth", "sunlight",)

print(hero1.display_identity())  # Output: I'm Shadow Flash! My superpower is speed.
print(hero2.display_identity())  # Output: I'm Superman ! My superpower is super strenth.