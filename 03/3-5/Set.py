empty_set = set()
print(empty_set)

even_numbers = {0, 2, 4, 6, 8}
print(even_numbers)

odd_numbers = {1, 3, 5, 7, 9}
print(odd_numbers)

print(set('letters'))

print(set( ['Dasher', 'Dancer', 'Prancer', 'Mason-Dixon'] ))

print(set( ('Ummagumma', 'Echoes', 'Atom Heart Mother') ))

print(set( {'apple': 'red', 'orange': 'orange', 'cherry': 'red'} ))

drinks = {
'martini': {'vodka', 'vermouth'},
'black russian': {'vodka', 'kahlua'},
'white russian': {'cream', 'kahlua', 'vodka'},
'manhattan': {'rye', 'vermouth', 'bitters'},
'screwdriver': {'orange juice', 'vodka'}
}

for name, contents in drinks.items():
    if 'vodka' in contents:
        print(name)

for name, contents in drinks.items():
    if 'vodka' in contents and not ('vermouth' in contents or 'cream' in contents):
        print(name)

for name, contents in drinks.items():
    if contents & {'vermouth', 'orange juice'}:
        print(name)

bruss = drinks['black russian']
wruss = drinks['white russian']

a = {1,2}
b = {2,3}

print(a & b)
print(a.intersection(b))
print(bruss & wruss)

print(a | b)
print(a.union(b))

print(a - b)