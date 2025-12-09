class Person:
    def __init__(self, name):
        self.name = name
    
    def greet(self):
        return f"Hello, I'm {self.name}"

class Doctor(Person):
    def treat(self):
        return f"Treating patients"

class Admin(Person):
    def manage(self):
        return f"Managing hospital"

class HeadDoctor(Doctor, Admin):
    def lead(self):
        return f"Leading the team"

print("HOSPITAL\n")


d = Doctor("Dr. Manoj")
print("DOCTOR:")
print(d.greet())
print(d.treat())

print("\n" + "-" * 30)

hd = HeadDoctor("Dr. Kunal")
print("\nHEAD DOCTOR:")
print(hd.greet())
print(hd.treat())  
print(hd.manage())  
print(hd.lead())    
