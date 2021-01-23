# Duck Typing and Easier to ask forgiveness than permission (EAFP)


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
        item.bark()

    except AttributeError as e:
        print(e)


d = Duck()
quack_and_fly(d)
print()

p = Person()
quack_and_fly(p)

"""
class Duck:

    def quack(self):
        print('Quack, quack')

    def fly(self):
        print('Flap, Flap!')


class Person:

    def quack(self):
        print("I'm Quacking Like a Duck!")

    def fly(self):
        print("I'm Flapping my Arms!")


def quack_and_fly(thing):
    pass
    # Not Duck-Typed (Non-Pythonic)
    # if isinstance(thing, Duck):
    #     thing.quack()
    #     thing.fly()
    # else:
    #     print('This has to be a Duck!')

    # LBYL (Non-Pythonic)
    # if hasattr(thing, 'quack'):
    #     if callable(thing.quack):
    #         thing.quack()

    # if hasattr(thing, 'fly'):
    #     if callable(thing.fly):
    #         thing.fly()

    #     try:
    #         thing.quack()
    #         thing.fly()
    #         thing.bark()
    #     except AttributeError as e:
    #         print(e)


d = Duck()

print(type(dir(d)))
"""