"""
1. list comprehension must include [] -> to make it an iterable list
    otherwise it will just be generator wating for the next()
    
2. format: [func* for n in nums if condition*]
    先操作，在哪个范围，何种条件

"""


# Must include list() -> []

nums = list(range(1, 11))

print(nums)

print([n * n for n in nums])

print([n * n for n in nums if n % 2 == 1])
print([n * n for n in nums if n % 2 == 0])


#

my_list = []

for letter in 'abcd':
    for num in range(4):
        my_list.append((letter, num))

print(my_list)

# Topic - how concatenate items in a list to a single string? ⭐️
# Ref - https://stackoverflow.com/a/12453584
# 🧠 ''.join(list)

new_list = [(letter + num)
            for letter in 'abcd' for num in ['1', '2', '3', '4']]

print(new_list)

print(''.join(new_list))


# Intermediate list
names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heros = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']

for a, b in zip(names, heros):
    print(f'{b} is actually acted by {a} in the film.')


"""
# Dictionary Comprehensions
# print zip(names, heros)

# I want a dict{'name': 'hero'} for each name,hero in zip(names, heros)
# my_dict = {}
# for name, hero in zip(names, heros):
#     my_dict[name] = hero
# print my_dict


# If name not equal to Peter

# Set Comprehensions
# nums = [1,1,2,1,3,4,3,4,5,5,6,7,8,7,9,9]
# my_set = set()
# for n in nums:
#     my_set.add(n)
# print my_set


# Generator Expressions
# I want to yield 'n*n' for each 'n' in nums
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# def gen_func(nums):
#     for n in nums:
#         yield n*n

# my_gen = gen_func(nums)

# for i in my_gen:
#     print i
"""
