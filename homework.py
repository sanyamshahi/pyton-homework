# this will ask the user, item name, price of the item, quantity and print the total bill using the f string.
item=input("what is the name of your item you want to buy?:")
price=int(input("what is the price of the item?:$"))
quantity=int(input("whats the total quantity?:"))
print(f"the name of your item is {item} cost per piece is ${price} total quantity you want to buy is {quantity} therefore the total bill is ${quantity*price}")