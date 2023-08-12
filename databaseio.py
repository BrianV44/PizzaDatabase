
#Brian Vargas

styleList = ["pan pizza", "thin crust", "deep dish"]
sizeList = [10, 12, 14, 16]
toppingsList = ["pepperoni", "sausage",
"bacon", "ham", "onion", "mushroom", "bell pepper", "jalapeno"]
navlist = ["a", "r", "d", "e", "s", "l"]


def read_data():
    '''
    Will prompt user to specify what type of pizza they want

    Args:
        style(string): Can either choose pan pizza, thin crust, or deep dish

        size(integer): Can either choose 10, 12, 14, or 16

        toppings(string): Can either choose pepperoni, sausage,
                        bacon, ham, onion, mushroom, bell pepper, or jalapeno

    returns:
        style(string)
        
        size(integer)

        toppings(string)
    '''

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
    return style, size, toppings

#Display pizza order no return
def print_data(style, size, toppings):
    print(f"Your Pizza:\n" +
      f"Style: {style}\n" +
      f"Size: {size:.0f} Inch\n" +
      f"Topping: {toppings}")
    
          
        

def display_menu():
    '''
    Will let user decide how they want to use the database

    returns: option(string): Options are: "a" for add, "r" to remove, "d" to display,
             and "e" to exit
    '''

    print("Welcome to my pizza shop!")
    print()
    print("Please select one of the following options:")
    print()
    print("a -- add a pizza to database\n" +
          "r -- remove a pizza from the database\n" +
          "d -- display database of pizzas\n" +
         "e -- exit\n" +
          "s -- save the database to a file\n" +
          "l -- load a saved database")
    print()
    try:
        userInput = str(input("Enter option: "))
    except ValueError:
        userInput = 10
    while userInput not in navlist:
        try:
            print()
            print("Invalid Option")
            print()
            print("Please select one of the following options:")
            print()
            print("a -- add a pizza to database\n" +
                  "r -- remove a pizza from the database\n" +
                  "d -- display database of pizzas\n" +
                  "e -- exit\n" +
                  "s -- save the database to a file\n" +
                  "l -- load a saved database")
            userInput = str(input("Enter option: "))
        except ValueError:
             userInput = 10
        
    return userInput






    

