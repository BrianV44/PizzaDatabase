import databaseio


class pizza():
    def __init__(self, style, size, toppings):
        '''
        Creates a new object of the pizza class with its attributes

        Arguments:
        style(string): Pizza style.

        size(float): Size of pizza.

        toppings(string): Pizza toppings.

        Returns:
        None
        '''
        self.style = style
        self.size = size
        self.toppings = toppings
        return
    def display(self):
        '''
        Utilizes the databaseio.print_data function to print the object's arguments

        Arguments:
        style(string): Pizza style.

        size(float): Size of pizza.

        toppings(string): Pizza toppings.

        Returns:
        None
        '''
        databaseio.print_data(self.style, self.size, self.toppings)
        return 
