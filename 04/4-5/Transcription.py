rabbits = ['Flopsy','Mopsy','Cottontail','Peter']
for rabbit in rabbits:
    print(rabbit)

word = "cat"
for letter in word:
    print(letter)

accusation = {'room': 'ballroom', 'weapon': 'lead pipe','person':'Col. Mustard'}
for card in accusation:
    print(card)

for value in accusation.values():
    print(value)

for items in accusation.items():
    print(items)

for card, contents in accusation.items():
    print('card',card , 'has the contents', contents)

days = ['Monday','Tuesday','Wednesday']
fruits = ['banana', 'orange', 'peach']
drinks = ['coffee', 'tea', 'beer']
desserts = ['tiramisu', 'ice cream', 'pie', 'pudding']
for day,fluit,drink,dessert in zip(days,fruits,drinks,desserts):
    print(day, ": drink",drink,"- eat",fluit, "- enjoy",dessert)

english = 'Monday', 'Tuesday','Wednesday'
french = 'Lundi', 'Mardi','Mercredi'

list(zip(english,french))
dict(zip(english,french))

for x in range(0,3):
    print(x)

for x in range(2, -1, -1):
    print(x)

number_list = [number for number in range(1,6)]
print(number_list)

number_list2 = [number-1 for number in range(1,6)]
print(number_list2)

a_list = [number for number in range(1,6) if number % 2 == 1]
print(a_list)

rows = range(1,4)
cols = range(1,3)
cells = [(row, col) for row in rows for col in cols]
for cell in cells:
    print(cell)

for row, col in cells:
    print(row,col)

word = 'letters'

letter_counts = {letter: word.count(letter) for letter in word}
print(letter_counts)

letter_counts2 = {letter: word.count(letter) for letter in set(word)}
print(letter_counts2)

number_thing = (number for number in range(1,6))
print(number_thing)
print(type(number_thing))

for number in number_thing:
    print(number)

try_again = list(number_thing)
print(try_again)
