class Thing:
    pass

example = Thing

class Thing2:
    letters = 'abc'

class Thing3:
    def __init__(self):
        self.letters = 'xyz'


el_dict = {'name': 'Hydrogen', 'symbol': 'H', 'number': 1}



class Element:
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number

        @property
        def name(self):
            return self.__name
        @property
        def symbol(self):
            return self.__symbol
        @property
        def number(self):
            return self.__namber

hydrogen = Element('Hydrogen', 'H', 1)

print(hydrogen.name)
print(hydrogen.symbol)
print(hydrogen.number)