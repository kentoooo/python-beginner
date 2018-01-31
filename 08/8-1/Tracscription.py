poem = '''There was a young lady named Bright
Whose speed was far faster than light;
She started one day
In a relative way,
And returned on the previous night.'''

try:
    fout = open('relativity', 'xt')
    fout.write(poem)
except FileExistsError:
    print('relativity already exists!')

bdata = bytes(range(0, 256))

fout = open('bfile', 'wb')
size = len(bdata)
offset = 0
chunk = 100
while True:
    if offset > size:
        break
    fout.write(bdata[offset:offset + chunk])
    offset += chunk
fout.close()

with open('relativity', 'wt') as fout:
    fout.write(poem)
