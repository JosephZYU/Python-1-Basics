# isolated else-statement -> No Break from above

from findIndex import find_index

my_list = [1, 2, 3]

for num in my_list:
    print(num)

else:
    print('You can see this message becuase there is NO Break from above')


i = 1

while i < 5:
    print(i)

    i += 1

    if i == 1:
        break

else:
    print('Your while loop has just finished.')


my_new_list = ['Corey', 'Rick', 'John']

index_location = find_index(my_new_list, 'Steve')

print('Location of target is index: {}'.format(index_location))
