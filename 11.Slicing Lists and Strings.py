
my_list = list(range(10))
# my_list = list(range(-10, 0))

print(my_list[3:-2])

print(my_list[3:])

print(my_list[:])

# 尽可能用index，一切指数化
# 🧠 list[0::2] -> even number
# 🧠 list[1::2] -> even number

print(my_list[0::2])
print(my_list[1::2])

# 🧠 一旦顺序为逆序，step也必须为逆序

print(my_list[-1:2:-2])
print(my_list[-1:2:2])

print(my_list[::-2])
print(my_list[-2::-2])


sample_url = "http://coreyms.com"

print(sample_url)
print(sample_url[-4:])


print(sample_url[7:14])
print(sample_url[7:-4])
print(sample_url[:7])
