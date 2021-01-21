"""
because generators don't hold the entire result in memory

it yields one result at a time 🌟

so really this is waiting for us to ask for the
next result so hasn't actually computed anything yet now

"""

# ✅ how to for loop with list comprehension? - YES - [i * i for i in nums]
# 🎯✅ what's the yield vs. return in Python? - return (single item) yield (all items)


def square_num(nums):
    # for num in nums:
    #     yield num * num
    yield [i * i for i in nums]  # 200
    # return [i * i for i in nums]  # 200


new_nums = square_num([11, 12, 13])

print(new_nums)
# print(next(new_nums))
# print(next(new_nums))
# print(next(new_nums))
# print(next(new_nums))  # StopIteration -> we can NOT next outside the range!

for num in new_nums:
    print(num)

my_nums = [i * i for i in [1, 2, 3, 4, 5]]

print(my_nums)
