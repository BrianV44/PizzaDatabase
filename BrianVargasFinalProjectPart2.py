
#Brian Vargas

'''
I will build a database of different pizza styles.
For each pizza in the database, I will store the
pizza style (string), the size (integer), and
the toppings (string).

Legal values for the pizza style are: pan pizza,
thin crust, or deep dish.

Legal values for size are: 10, 12, 14, or 16.

legal values for toppings are: pepperoni, sausage,
bacon, ham, onion, mushroom, bell pepper, jalapeno,
'''

styleList = ["pan pizza", "thin crust", "deep dish"]
#could be error here if its float instead of string
sizeList = [10, 12, 14, 16]
toppingsList = ["pepperoni", "sausage",
"bacon", "ham", "onion", "mushroom", "bell pepper", "jalapeno"]

#pizza style
try:
    style = input("Available pizza styles are: pan pizza, thin crust, or deep dish\n" +
                  "What style would you like: ")
except ValueError:
    style = 10
    
while style not in styleList:
    try:
        style = input("Incorrect style. Available pizza styles are: pan pizza, thin crust, or deep dish\n" +
              "What style would you like: ")
    except ValueError:
        style = 10
print()
#pizza size
#should give error message for negative numbers
try:
    size = float(input("Available sizes in inches are: 10, 12, 14, 16\n" +
                       "What size would you like: "))
except (ValueError):
    size = 18

while size not in sizeList:
    try:
        size = float(input("Unavailable size. Available sizes in inches are: 10, 12, 14, 16\n" +
                       "What size would you like: "))
    except ValueError:
        size = 18
print()
#pizza toppings
try:
    toppings = input("Available toppings are: pepperoni, sausage,\n" +
"bacon, ham, onion, mushroom, bell pepper, jalapeno\n" + "\n" + "Please choose one topping: ")
except ValueError:
    toppings = 10
    
while toppings not in toppingsList:
    try:
        toppings = input("Unavailable topping. Available toppings are: pepperoni, sausage,\n" +
"bacon, ham, onion, mushroom, bell pepper, jalapeno\n " + "\n" + "Please choose one topping: ")
    except ValueError:
        toppings = 10
print()
#Display Message
print(f"Your Pizza:\n" +
      f"Style: {style}\n" +
      f"Size: {size:.0f} Inch\n" +
      f"Topping: {toppings}")
        
    

