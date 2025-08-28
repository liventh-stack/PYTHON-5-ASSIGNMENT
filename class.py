# Base class
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def info(self):
        return f"{self.brand} {self.model}"

# Inherited class (Smartphone)
class Smartphone(Device):
    def __init__(self, brand, model, battery):
        super().__init__(brand, model)   # Inheritance ✅
        self.__battery = battery         # Encapsulation (private attribute)

    # Method to charge
    def charge(self, amount):
        self.__battery += amount
        if self.__battery > 100:
            self.__battery = 100
        print(f"🔋 Battery charged to {self.__battery}%")

    # Method to use phone
    def use(self, hours):
        self.__battery -= hours * 10
        if self.__battery < 0:
            self.__battery = 0
        print(f"📱 Used for {hours}h, battery now {self.__battery}%")

    # Getter for encapsulated battery
    def get_battery(self):
        return self.__battery


# Create objects
phone1 = Smartphone("Samsung", "Galaxy S24", 80)
phone2 = Smartphone("Apple", "iPhone 15", 50)

print(phone1.info())  
phone1.use(3)    
phone1.charge(20)

print(phone2.info())  
print("Battery:", phone2.get_battery(), "%")
