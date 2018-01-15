pythons = {
    'Chapman' : 'Graham',
    'Cleese': 'John',
    'Gilliam': 'Terry',
    'Idle': 'Eric',
    'Jones': 'Terry',
    'Palin': 'Michael',
}
print(pythons)

others = { 'Marx': 'Groucho', 'Howard': 'Moe' }

pythons.update(others)

print(pythons)

first = {'a': 1, 'b': 2}

print(first)

second = {'b': 'platypus'}

first.update(second)

print(second)