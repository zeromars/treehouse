# unchangeable lists
my_tuple = (1,2,3)
# (1,2,3)
my_second_tuple = 1,2,3
# (1,2,3)
my_third_tuple = tuple([1,2,3])
# (1,2,3)
my_third_tuple[1]

dir(tuple)
#handy to see properties

#simultanious assignment
a, b = 1,2
# a = 1
# b = 2

#unpacking tuples
c = (3,4)
# (3,4)

d,e = c
d
# 3
e
# 4

#packing
f = d, e
f==c
# True


# same as
a = 1
b = 2
a, b = b, a
# a = 2
# b = 1

#this
a= 1
b=2
c=a
a=b
b=c
# remove c

def my_func():
    return 1,2,3
my_func()
tup = my_func()
x,y,z = my_func()


# Handy functions:
# .upper() - uppercases a string
# .lower() - lowercases a string
# .title() - titlecases a string
# There is no function to reverse a string.
# Maybe you can do it with a slice?

def stringcases(item):
    return item.upper(), item.lower(), item.title(), item[::-1]

my_alphabet_list = list('abcdefghijklmnopqrstuvwxyz')

for index, letter in enumerate(my_alphabet_list):
    print('{}: {}'.format(index, letter))

for step in enumerate(my_alphabet_list):
    print('{}: {}'.format(step[0], step[1]))

## * takes apart tuples or lists
## ** takes apart dictionaries

for step in enumerate(my_alphabet_list):
    print('{}: {}'.format(*step))

my_dict = {'name': 'Landon', 'age': 36, 'state': 'California'}

for key, value in my_dict.items():
    print('{}: {}'.format(key.title(), value))


# combo([1, 2, 3], 'abc')
# Output:
# [(1, 'a'), (2, 'b'), (3, 'c')]
# If you use .append(), you'll want to pass it a tuple of new values.
def combo(first, last):
    items = []
    for index, item in enumerate(first):
        item_1 = item
        item_2 = last[index]
        items.append((item_1, item_2))
    return items