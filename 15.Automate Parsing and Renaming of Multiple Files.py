"""

# 🎯

# 🎯 Create file based on text

"""
import os

planets = ['Earch', 'Jupiter', 'Mars', 'Mercury',
           'Pluto',  'The Sun', 'Uranus', 'Venus']


nums = list(range(1, 9))

# ✅ how to create #1, #2, #3, .... #8
# hashtag sign -> #


hash_nums = []

for num in nums:
    hash_nums.append('#'+str(num))


# ✅ how to create regular expression with certain part fixed
# -> simple apply our old friend f-string! Great!
# Do NOT over think during interview!

list_files = []

for planet, num in zip(planets, hash_nums):

    mn = 'Our Solar System'
    ext = 'mp4'

    list_files.append(f"{planet} - {mn} - {num}.{ext}")

    # print(f"{planet} - {mn} - {num}.{ext}")

print(list_files)


# operating system.change working directory to
# drag & drop from finder in Mac!
# 🧠 os.chdir()

os.chdir('/Users/josephyu/Documents/GitHub/Python-1-Basics/TBD-Planets')

print(os.getcwd())

# Check what's in our current working directory
# 🧠 os.listdir()

# Split extention only -> remain everything else
# 🧠 os.path.splitext()

# ✅ how to replace #8 -> 08 while change #10 to be 10?
# YES - zfill(2) with desired wideth

# ✅ how to replace #8 -> 8?
# YES - strip with [1:]

for file in os.listdir():

    list_items = []

    name, ext = os.path.splitext(file)

    planet, static_tetxt, num = name.split('-')

    # strip away any leading or trailing spaces!
    planet = planet.strip()
    static_tetxt = static_tetxt.strip()

    # fill ALL digits with 0
    # 🧠 zfill(width) # 2 -> 2 digits wide
    num = num.strip()[1:].zfill(3)

    new_name = f'{num}-{planet}{ext}'

    # Finally -> rename each file as you wish!
    # 🧠 os.rename(file, new_name) # (old, new)

    os.rename(file, new_name)
