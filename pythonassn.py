Python 3.11.1 (v3.11.1:a7a450f84a, Dec  6 2022, 15:24:06) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Sebastian Torres, Try More Treats!, Ver 1.0, 4/30/23
... # This program automates a discount program
>>> #Get the original price.
>>> original_price = int(input("Original price before discount: "))
Original price before discount: 20
>>> # Determine the number of items purchased.
>>> item_num = float(input("Number of items purchased? "))
Number of items purchased? 5
>>> #Determine discount rate based on items purchased.
>>> if item_num == 1:
...     print("No discount for purchasing a single item.")
... elif item_num == 2:
...     discount_rate = 0.1
...     print("total amount owed after 10% discount is. ")
... elif item_num == 3:
...     discount_rate = 0.15
...     print("total amount owed after 15% discount is. ")
... elif item_num == 4:
...     discount_rate = 0.2
...     print("total amount owed after 20% discount is. ")
... elif item_num > 4:
...     discount_rate = 0.2
...     print("You receive 20% off each item and a coupon for 20% off another item at a later date.")
... else:
...     print("Thank you for shopping with us")
... 
...     
You receive 20% off each item and a coupon for 20% off another item at a later date.
>>> #Determine total price of items
>>> total = original_price * item_num
>>> print(total)
100.0
>>> #Determine how much is being discounted
>>> discountedprice = discount_rate * total
>>> print(discountedprice)
20.0
#Determine total amount owed
amount_owed = total - discountedprice
print(amount_owed)
80.0
