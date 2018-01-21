def do_nothing():
    pass

def make_a_sound():
    print('quack')

make_a_sound()

def agree():
    return True

if agree():
    print('Splendid!')
else:
    print('That was unexpected')

def echo(anything):
    return anything + ' ' + anything

echo('Rumplestiltskin')

def commentary(color):
    if color == 'red':
        return "It's a tomato"
    elif color == 'green':
        return "It's a green pepper."
    elif color == 'bee purple':
        return "I don't know what it is, but only bees can see it."
    else:
        return "I've never heard of the color " + color + "."

print(commentary("green"))
print(do_nothing())

def menu(wine, entree, dessert):
    return {'wine': wine, 'entree':entree, 'dessert': dessert}

print(menu('aa','bb','cc'))
print(menu(entree='beef', dessert='bagel', wine='bordeaux'))

def menu1(wine, entree, dessert='pudding'):
    return {'wine': wine, 'entree': entree, 'dessert': dessert}

def buggy(arg, result=[]):
    result.append(arg)
    print(result)

print(buggy('a'))
print(buggy('b'))

def print_args(*args):
    print('Positional argument tuple:',args)

print(print_args())
print(print_args(3, 2, 1, 'wait!', 'uh...'))

def print_kwargs(**kwargs):
    print('Keyword arguments:', kwargs)

print(print_kwargs(wine='merlot',entree='mutton', dessert='macaroom'))

def echo(anything):
    'echo は、与えられた入力引数を返す '
    return anything

def answer():
    print(42)

def run_something(func):
    func()

print(run_something(answer))

def add_args(arg1, arg2):
    print(arg1 + arg2)

def run_something_with_args(func, arg1, arg2):
    func(arg1,arg2)

run_something_with_args(add_args,5,9)

def sum_args(*args):
    return sum(args)

def run_with_positional_args(func, *args):
    return func(*args)

def outer(a, b):
    def inner(c, d):
        return c + d
    return inner(a, b)

def knights(saying):
    def inner(quote):
        return "We are the knight who say: '%s'" % quote
    return inner(saying)

print(knights('Ni!'))

def knights2(syaing):
    def inner2():
        return "We are the knights who say: '%s' " % saying
    return inner2

def edit_story(words, func):
    for word in words:
        print(func(word))

stairs = ['thud', 'meow', 'thud', 'hiss']

def enliven(word):
    return word.capitalize() + '!'

print(edit_story(stairs,enliven))
print(edit_story(stairs, lambda word: word.capitalize() + '!'))

print(sum(range(1,101)))

