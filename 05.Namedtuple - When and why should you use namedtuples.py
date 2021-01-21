# Jan 21 2021

"""
✨ Optional - Pythonic way to convert a dictionary into namedtuple or another hashable dict-like?

   Ref - https://stackoverflow.com/a/51653724



"""


from collections import namedtuple


# ✅ print dict with index? - YES -> dict.items(): run the for loop
color = {'red': 55, 'blue': 155, 'green': 255}

# print(color['red'])
# print(color['red'])
# print(color['red'])


for (a, b) in color.items():
    print(a)
    print(b)
    print()

# ✅ Access dict value-ONLY with index
# Ref - https://stackoverflow.com/a/15123364
# key是先包装成list，然后通过下表获得，相对简单
# 🧠 list(dict)[index] -> key ONLY

print(list(color)[0])
print(list(color)[1])
print(list(color)[2])

# value则是先通过dict解析出valiues，然后在rap成为list，最后通过下标获得
# 🧠 list(dict.values())[index] -> value ONLY

print(list(color.values())[0])
print(list(color.values())[1])
print(list(color.values())[2])


# Now let's create namedtuple()
# 通过attribute的形式获得，而不需要向list一样相对繁琐
# 🧠 namedtuple(tuple, [a, b, c])

Color = namedtuple('color', ['red', 'green', 'blue'])

color = Color(100, 200, 300)

print(color.red)
print(color.green)
print(color.blue)

print(color[0])
print(color[1])
print(color[2])
