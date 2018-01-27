def hours():
    return 'Open 9-5 daily'

plain = {'a':1,'b':2,'c':3}
print(plain)

from collections import OrderedDict,defaultdict
fancy = OrderedDict(('a',1),('b',2),('c',3))

dict_of_lists = defaultdict(list)
dict_of_lists['a'].append('something for a')
print(dict_of_lists['a'])

