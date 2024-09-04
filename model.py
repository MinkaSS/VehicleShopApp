from enum import Enum

class Vehicle:
    # TODO Vehicle implementation
    def __init__(self, id, manufacturer, model,horsePower, mileage ,price, productionYear, color, fuelType, transmission):
        self.id = id
        self.manufacturer = manufacturer
        self.model = model
        self.horsePower = horsePower
        self.mileage = mileage
        self.price = price
        self.productionYear = productionYear
        self.color = color
        self.fuelType = fuelType
        self.transmission = transmission


	# TODO add attributes and Getters / Setters
    def set_id(self, id):
        self.id = id
    def get_id(self):
        return self.id
    
    def set_manufacturer(self, manufacturer):
        self.manufacturer = manufacturer
    def get_manufacturer(self):
        return self.manufacturer
    
    def set_model(self, model):
        self.model = model
    def get_model(self):
        return self.model
    
    def set_horsePower(self, horsePower):
        self.horsePower = horsePower
    def get_horsePower(self):
        return self.horsePower
    
    
    def set_mileage(self, mileage):
        self.mileage = mileage
    def get_mileage(self):
        return self.mileage
    
    def set_price(self, price):
        self.price = price
    def get_price(self):
        return self.price
    
    
    def set_productionYear(self, productionYear):
        self.productionYear = productionYear
    def get_productionYear(self):
        return self.productionYear
    
    def set_transmission(self, transmission):
        self.transmission = transmission
    def get_transmission(self):
        return self.transmission
    
    def set_color(self, color):
        self.color = color
    def get_color(self):
        return self.color
    
    def set_fuelType(self, fuelType):
        self.fuelType = fuelType
    def get_fuelType(self):
        return self.fuelType
    
    
    

class Color(Enum):
    # TODO define color enumeration literals 
    BLACK =1
    GREY = 2
    WHITE = 3
    BLUE = 4
    RED = 5
    BROWN = 6
    YELLOW = 7

class FuelType(Enum):
    # TODO define fuel type enumeraition literals
    GASOLINE = 1
    DIESEL_FUEL = 2

class Manufacturer(Enum):
    # TODO define manufacturer enumeraition literals
    AUDI = 1
    BMW = 2
    VW = 3
    HONDA = 4
    SKODA =5

class Transmission(Enum):
    # TODO define transmission enumeraition literals 
    AUTOMATIC =1
    MANUAL = 2