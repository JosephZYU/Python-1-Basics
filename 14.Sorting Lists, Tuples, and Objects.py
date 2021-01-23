"""
WARNING: sorting must be based on string/text

list can be better replaced by li - 2 letters ONLY

🧠 sorted() -> the Swiss Army Knife

sorted() 使用与list和tuple，都可排序！超赞！

# 🎯 how to create random integers from 0-9 for 10 times exclusively
# 如何构建0-9，是的0-9个随机出现，且出现一次

"""

# 🧠 import randint
from random import randint

from employee import Employee

# Sort list
li = [9, 1, 8, 2, 7, 3, 6, 4, 5]

s_li = sorted(li)

print(li)
print(s_li)
print(li.sort())
print()

# Sort based on absolute values
li = list(range(-3, 4))

# Use key to apply "absolute" value
# 🧠 sorted(list, key=abs) -> abs

s_li = sorted(li, key=abs)

print(li)
print(s_li)
print()


# Sort tuples
tup = [1, 9, 2, 8, 3, 7, 4, 6, 5]

s_tup = sorted(tup)

print(tup)
print(s_tup)
print(tup.sort())
print()


di = {'name': 'Corey', 'job': 'prograomming', 'age': 'twenty', 'os': 'Mac'}

s_li = sorted(li)


s_di = sorted(di)

# s_di = sorted(list(di.values()))

print(s_di)
print()


e1 = Employee('Carl', 37, 70_000)
e2 = Employee('Sarah', 29, 80_000)
e3 = Employee('John', 43, 90_000)

emp_list = [e1, e2, e3]

#


def emp_sort(e):
    return e.age


s_employees = sorted(emp_list, key=emp_sort, reverse=False)

print(s_employees)
