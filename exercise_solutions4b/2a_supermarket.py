# Create the prices dictionary:
prices={}

# Add prices for each item
prices["banana"]=4
prices["apple"]= 2
prices["orange"]= 1.5
prices["pear"]= 3

# Create the stock dictionary
stock={}
# Add items of stock
stock["banana"]= 6
stock["apple"]= 0
stock["orange"] = 32
stock["pear"]= 15

 #Show all prices and stock

for food in prices:
    print (f"Stock item: {food}")
    print (f"Price: {prices[food]}")
    print (f"Stock: {stock[food]}")
    print()

total=0
for food in prices:
    money= prices[food]*stock[food]
    print(f"{food}: total value of {food} stock: €{money}")
    total=total +money

print (f"The total value of all stock is €{total}")


