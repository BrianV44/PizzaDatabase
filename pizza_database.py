
import databaseio
import csv
import pizza

class PizzaDatabase:
    def __init__(self, pizzas):
        self.database = pizzas

    def addItem(self, pizza):
        '''
        Adds a pizza object to the end of the index, increases count by one

        Arguments:
             pizza(object): Has three attributes:  style(str), size(float), topping(str)

        Returns:
             None 
        '''
        self.database.append(pizza)

    def ValidIndex(self, index):
        '''
        Checks to see if entered index falls within valid range of the self.database list

        Arguments:
            index(int): The index of the pizza object to be checked

        Returns:
            index(bool): true with valid index
        '''
        return 0 <= index < len(self.database)

    def deleteItem(self, index):
        '''
        Removes pizza object from the database utilizing database.pop

        Arguments:
             index(int): The index of the pizza object to be removed

        Returns:
             None 
        '''
        self.database.pop(index)

    def getItem(self, index: int):
        '''
        Retrieves a pizza object by specifying list index 

        Arguments:
             index(int): The index of the pizza object to be retrieved

        Returns:
             pizza object at index
        '''
        return self.database[index]
    

    def displayAll(self):
        '''
        Displays all pizza objects stored in the database 

        Arguments:
             None

        Returns:
             None
        '''
        for index, pizza in enumerate(self.database):
            self.getItem(index).display()
            print()

    def save(self, filename):
        '''
        Saves the database content to a new CSV file

        Arguments:
            filename(str): Name of new CSV file 

        Returns:
             None
        '''
        with open(filename, mode='w', newline='') as myFile:
            writer = csv.writer(myFile)
            for pizza in self.database:
                writer.writerow([pizza.style, pizza.size, pizza.toppings])

    def load(self, filename):
        '''
        Clears current database, loads data from a CSV file, and adds
        each row as a pizza object using self.addItem

        Arguments:
            filename(str): Name of the CSV file 

        Returns:
             None
        '''
        self.database.clear()
        with open(filename, mode='r') as myFile:
            reader = csv.reader(myFile)
            for row in reader:
                style, size, toppings = row
                new_pizza = pizza.pizza(style, float(size), toppings)
                self.addItem(new_pizza)
            
        
