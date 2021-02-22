import os
class Protector:

    static_group = "Electrics"

    @staticmethod
    def advertisement():
        return Protector.static_group

    def __init__(self,max_power=100,low_level_turning_off=1,color="blue",price=1000,brand="",year=1996):
        self.max_power = max_power
        self.low_level_turning_off = low_level_turning_off
        self.color = color
        self.price = price
        self.brand = brand
        self.year = year

    def __del__(self):
        print("Destructor activated")

    def __str__(self):
        if self.brand:
            return ("All information about protector:" + os.linesep +
            "Max power : " + str(self.max_power) + os.linesep +
            "Low level turning off :" + str(self.low_level_turning_off) + os.linesep +
            "Color :" + str(self.color) + os.linesep +
            "Price :" + str(self.price) + os.linesep +
            "Brand :" + str(self.brand) + os.linesep +
            "Year :" + str(self.year) + os.linesep + os.linesep)

        else:
            return ("All information about protector:" + os.linesep +
            "Max power : " + str(self.max_power) + os.linesep +
            "Low level turning off :" + str(self.low_level_turning_off) + os.linesep +
            "Color :" + str(self.color) + os.linesep +
            "Price :" + str(self.price) + os.linesep +
            "Year :" + str(self.year)+ os.linesep + os.linesep)
