# 🎯

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

print(list_files)

# 🎯 Create file based on text

[print()]
