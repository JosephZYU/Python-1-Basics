"""
because generators don't hold the entire result in memory

it yields one result at a time 🌟

so really this is waiting for us to ask for the
next result so hasn't actually computed anything yet now

😎 In most cases, we will use return () for coding interview~

🧠 return: sends a specified value back to its caller
    
🧠 yield: can produce a sequence of values.

We should use yield when we want to iterate over a sequence 
but don’t want to store the entire sequence in memory.

Ref - https://dzone.com/articles/when-to-use-yield-instead-of-return-in-python#:~:text=return%20sends%20a%20specified%20value,is%20used%20in%20Python%20generators.

"""

# ✅ how to for loop with list comprehension? - YES - [i * i for i in nums]
# ✅ what's the yield vs. return in Python? - return (single item) yield (all items)


def square_num(nums):
    # for num in nums:
    #     yield num * num
    # yield [i * i for i in nums]  # 200
    return [i * i for i in nums]  # 200


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
