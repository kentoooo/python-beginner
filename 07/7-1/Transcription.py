import re


def unicode_test(value):
    import unicodedata
    name = unicodedata.name(value)
    value2 = unicodedata.lookup(name)
    print('value="%s", name="%s",value2="%s"' % (value, name, value2))

print(unicode_test('A'))
print(unicode_test('\u2603'))

place = 'caf\u00e9'
print(place)

actor = 'Richard Gere'
cat = 'Chester'
weight = 28

print("My wife's favorite actor is %s" % actor)
print("Our cat %s weighs %s pounds" % (cat, weight))

n = 42
f = 7.03
s = 'string cheese'

print('%d %f %s' % (n, f, s))

print('{} {} {}'.format(n, f, s))
print('{2} {0} {1}'.format(f, s, n))

result = re.match('You', 'Young Frankenstein')
print(result)