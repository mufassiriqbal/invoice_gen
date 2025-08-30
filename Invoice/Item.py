class Item:
    def __init__(self,item_name,item_quantity,item_price):
        self.__item_name = item_name
        self.__item_quantity = item_quantity
        self.__item_price = item_price

    def setItemName(self,item_name):
        self.__item_name=item_name
    
    def getItemName(self):
        return self.__item_name
    
    def setItemQuantity(self,item_quantity):
        self.__item_quantity = item_quantity

    def getItemQuantity(self):
        return self.__item_quantity
    
    def setItemPrice(self,item_price):
        self.__item_price = item_price
    
    def getItemPrice(self):
        return self.__item_price
    
    def calculate_price(self):
        return self.__item_quantity * self.__item_price
    
    def __str__(self):
        return f"{self.__item_name:<20}{self.getItemQuantity():<20}{self.getItemPrice():<20}{self.calculate_price():<20}"