class Restaurant:
    def __init__(self, name):
        self.name = name

class Ordering(Restaurant):
    def order(self, menu, price):
        self.menu = menu
        self.price = price
        return f"Ordered {menu}"

class Serving(Ordering):
    def serve(self):
        return f"Serving {self.menu}"

class Billing(Serving):
    def bill(self):
        return f"{self.price} for {self.menu}"

r = Billing("Krupal Restaurant")
print(r.order("Chole Bhature", 700))
print(r.order("Mysore Dosa", 300))
print(r.order("Scoop", 200))
print(r.order("Brownie", 400))
print(r.serve())
print(r.bill())
