# Duck Typing and Easier to ask forgiveness than permission (EAFP)
"""
we are NOT asking permission if we can do seomthing!

If we can -> perform the way twe want to handle it

except -> raise error as e


---> we just try to do it! Highly biased towards action! JUST DO IT!
"""


import os


class Duck:

    def quack(self):
        print('Quack, Quack~')

    def fly(self):
        print('Flap, Flap!')


class Person:

    def quack(self):
        print('I am quacking just like a duck')

    def fly(self):
        print('I am flapping my arms')


def quack_and_fly(item):
    # EAFP (Pythonic)
    try:
        item.quack()
        item.fly()
        item.cark()
        item.aark()
        item.bark()

    # if you get an error -> auto print that specific-error!
    except AttributeError as e:
        print(e)


d = Duck()
quack_and_fly(d)
print()

p = Person()
quack_and_fly(p)
print()


person = {'name': 'Corey', 'job': 'prograomming', 'age': 'twenty'}


# 🧠 excep KeyError as e
# 🧠 "".format(**dict)
# 🎯 what's the difference with f"" 🆚 "".format() - can we write in both ways?
# 🎯 when to plainly use except 🆚 when to use except ___Error as e?
# AND what is really about double ** in front of person?

try:
    print(
        "My name is {name} and I'm {age} years old with {job} major.".format(**person))  # 👈👈👈
except KeyError as e:
    print(f"Missing {e} key")


# 🧠 excep IndexError
# 🎯 else IndexError:
my_list = list(range(1, 6))


try:
    print(my_list[5])
except IndexError:
    print('That index does NOT exist')


# OS file

my_file = 'require.txt'

try:
    f = open(my_file)
except IOError as e:
    print('File can NOT be accessed')
else:
    with f:
        print(f.read())
