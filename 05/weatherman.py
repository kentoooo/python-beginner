from report import get_description as do_it
import sys

description = do_it()
print("Today's weather:",description)

for place in sys.path:
    print(place)