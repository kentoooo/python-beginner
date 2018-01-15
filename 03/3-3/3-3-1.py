empty_tuple = ()
print(empty_tuple)

one_marx = 'Groucho',
print(one_marx)

marx_tuple = 'Groucho','Chico','Harpo'
print(marx_tuple)

marx_tuple_2 = ('Groucho','Chico','Harpo')
print(marx_tuple_2)

# タプルアンパック
a,b,c = marx_tuple
print(a)
print(b)
print(c)

password = 'swordfish'
icecream = 'tuttifrutti'
password, icecream = icecream, password
print(password)
print(icecream)

marx_list = ['Groucho', 'Chico', 'Harpo']
print(marx_list)
print(tuple(marx_list))