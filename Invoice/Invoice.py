from Date import Date
class Invoice:
    TAX_RATE = 6.25/100
    def __init__(self):
        self.items = []
        self.__purchase_date = Date()

    def addItem(self,item):
        self.items.append(item)

    def setPurchaseDate(self,date):
        self.__purchase_date = date

    def getPurchaseDate(self):
        return self.__purchase_date

    def print_invoice(self):
        print(f"{'Item Name':<20}{'Item Quanity':<20}{'Price':<20}{'Total':<20}")
        grand_total = 0

        for item in self.items:
            print(item)
            grand_total = grand_total+item.calculate_price()
        print()
        print(f"{'Grand Total':<60}{grand_total}") 
        print((f"{'Total with tax':<60}{grand_total+(grand_total*Invoice.TAX_RATE)}"))
        print(f"{'Purchase Date':<60} {self.getPurchaseDate()}")

    def __str__(self):
        pass
    