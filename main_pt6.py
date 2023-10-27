import databaseio
import pizza
import pizza_database

PizzaDatabase = pizza_database.PizzaDatabase([])

def main():
    '''
    Presents a menu that allows the user to: add an item to the pizza database,
    display all pizzas in database, delete a pizza by index, save the database to
    a file, and load a database from a file.

    Returns:
        None
    '''
    userInput = ""
    while (userInput != "e"):
        userInput = databaseio.display_menu()
        print()
        if (userInput == "a"):
            style, size, toppings = databaseio.read_data()
            new_pizza = pizza.pizza(style, size, toppings)
            PizzaDatabase.addItem(new_pizza)

        elif (userInput == "d"):
            PizzaDatabase.displayAll()

        elif (userInput == "r"):
            while True:
                try:   
                    index = int(input("Enter index of item to delete (-1 to quit): "))
                    print()
                    if index == -1:
                        break
                    if PizzaDatabase.ValidIndex(index):
                        PizzaDatabase.deleteItem(index)
                        break
                    else:
                        print("Invalid index. Re-enter index or -1 to quit.")
                        print()
                except ValueError:
                    print("Invalid index. Re-enter index or -1 to quit.")
                    print()
        

        elif (userInput == "s"):
            myfile = input("Enter a filename to save to: ")
            PizzaDatabase.save(myfile)

        elif (userInput =="l"):
            myfile = input("Enter a filename to load from: ")
            PizzaDatabase.load(myfile)

main()

