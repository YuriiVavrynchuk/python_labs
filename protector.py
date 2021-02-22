class Protector:

    static_group = "Electrics"

    @staticmethod
    def advertisement():
        return Protector.static_group

    def __init__(self,max_power = 100,low_level_turning_off = 1,color = "blue",price = "1000$",brand = "",year = 1996):
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
            return ("All information about protector:" + "\n" +
            "Max power : " + str(self.max_power) + "\n" +
            "Low level turning off :" + str(self.low_level_turning_off) + "\n" +
            "Color :" + str(self.color) + "\n" +
            "Price :" + str(self.price) + "\n" +
            "Brand :" + str(self.brand) + "\n" +
            "Year :" + str(self.year) + "\n" + "\n")

        else:
            return ("All information about protector:" + "\n" +
            "Max power : " + str(self.max_power) + "\n" +
            "Low level turning off :" + str(self.low_level_turning_off) + "\n" +
            "Color :" + str(self.color) + "\n" +
            "Price :" + str(self.price) + "\n" +
            "Year :" + str(self.year)+ "\n" + "\n")