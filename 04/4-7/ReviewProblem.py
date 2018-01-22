guess_me = 7

if guess_me < 7:
    print('too low')
elif guess_me > 7:
    print('too high')
else:
    print('just right')

start = 1

while True:
    if start < guess_me:
        print('too low')
    elif start == guess_me:
        print('found it!')
        break
    else:
        print('oops')
        break
    start += 1

for value in [3,2,1,0]:
    print(value)

even = [number for number in range(10) if number % 2 == 0]
print(even)

squares = {key: key*key for key in range(10)}
print(squares)

odd = {number for number in range(10) if number % 2 == 1}
print(odd)

for thing in ('Got %s' % number for number in range(10)):
    print(thing)

def good():
    return ['Harry', 'Ron', 'Hermione']

def get_odds():
    for number in range(1,10,2):
        yield number

for count, number in enumerate(get_odds(), 1):
    if count == 3:
        print("The third odd number is", number)
        break

def test(func):
    def new_func(*args, **kwargs):
        print('start')
        result = func(*args, **kwargs)
        print('end')
        return result
    return new_func

@test
def greeting():
    print("Greetings, Earthling")
    
titles = ['Creature of Habit','Crewel Fate']
plots = ['A nun turns into a monster','A haunted yarn shop']
movies = dict(zip(titles,plots))
print(movies)