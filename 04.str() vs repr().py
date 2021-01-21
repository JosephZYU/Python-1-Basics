"""
The goal of __repr__ -> unambiguous  # official repersentation -> unambigous
The goal of __str__ -> readable  # string text -> easy for human read

# 🧠 official representation -> __repr__ -> datetime.dateim()
# 🧠 human(end-user) readable -> __str__ -> '2020-01-21'

"""

import pytz
import datetime as dt

a = [1, 2, 3, 4]
b = 'sample string'

print(str(a))
print(repr(a))
print()

print(str(b))
print(repr(b))
print()

c = dt.datetime.now()

d = str(c)

print(repr(c))
print(repr(d))
print()

print(str(c))
print(str(d))
print()
