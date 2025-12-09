class Sarees:
    def __init__(self, fabric, color, price, discount):
        self.fabric = fabric
        self.color = color
        self.price = price
        self.discount = discount
    def details(self):
        print(f"Fabric : {self.fabric}")
        print(f"Color : {self.color}")
        print(f"Price : {self.price}")
        print(f"Discount : {self.discount}")

class Collection(Sarees):
    def __init__(self, fabric, color, price, discount, designer, types):
        super().__init__(fabric, color, price, discount)
        self.designer = designer
        self.types = types
    def details_Sarees(self):
        super().details()
        print(f"Types : {self.types}")

Sarees1 = Collection("Moonbeam Chiffon", "Starry Midnight Blue", 12500, 15, "Luna Weavers", "Celestial Evening Wear")
Sarees1.details_Sarees()
Sarees2 = Collection("Dragon Scale Brocade", "Imperial Jade with Gold Threads", 35999, 20, "Regal Heritage", "Wedding & Bridal")
Sarees2.details_Sarees()        
Sarees3 = Collection("Phoenix Feather Silk", "Sunset Ombre {Orange to Purple}", 18999, 12, "Earthloom Studios", "Fusion Wear")
Sarees3.details_Sarees()
Sarees4 = Collection("Vintage Kanjivaram Revival", "Indigo Resist Dyed with Silver Zari", 27500, 10, "TimeWarp Textiles", "Heritage Modern")
Sarees4.details_Sarees()

print("--------Krupal Regular Sarees--------")
regular = Sarees("Cotton", "Blue", 6000, 15)
regular.details()
