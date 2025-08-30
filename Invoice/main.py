from Item import Item
from Invoice import Invoice
from Date import Date
def main():
    invoice = Invoice()
    # items = []
    while True:
        item_name = input("Enter name of the item\n")
        item_quantity = int(input("Entery quantity of the item\n"))
        item_price = float(input("Enter price of the item\n"))

        # items.append(Item(item_name,item_quantity,item_price))
        invoice.addItem(Item(item_name,item_quantity,item_price))
        sentinel = input("Add more? (y/n)")
        if(sentinel == 'n'):
            break                    

    print("Enter the date of purchase")
    day = int(input("Enter Day\n"))
    month = int(input("Enter Month\n"))
    year = int(input("Enter year\n"))
    purchase_date = Date(day,month,year)
    invoice.setPurchaseDate(purchase_date)
    # item1 = Item("Potato",5,200)
    # items.append(item1)
    # item2 = Item("Chips", 20, 40)
    # items.append(item2)
    # items.append(Item("Chocolate",100,15))
    invoice.print_invoice()
   

main()