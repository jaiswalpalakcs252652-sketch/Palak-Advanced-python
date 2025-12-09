class Player:
    def __init__(self, name):
        self.name = name
    
    def train(self):
        return f"{self.name} is training"

class Cricketer(Player):
    def bat(self):
        return f"{self.name} is batting "

class Swimmer(Player):
    def swim(self):
        return f"{self.name} is swimming "

class Runner(Player):
    def run(self):
        return f"{self.name} is running "

c = Cricketer("Dhoni")
s = Swimmer("Phelps")
r = Runner("Bolt")

print(c.train())
print(c.bat())

print(s.train())
print(s.swim())

print(r.train())
print(r.run())
