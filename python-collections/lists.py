###########################Lists Extended######################
#range counts from 0 to that number (integers)
our_list = list(range(10))
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

our_list + [10,11,12]
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12]
our_list
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#doesnt actually append it that way

our_list = our_list + [10,11,12]
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12]

list_1 = [1,2,3]
list_2 = [4,5,6]
list_3 = list_1 + list_2
# [0, 1, 2, 3, 4, 5, 6, 7]

#extend is faster than +

our_list = list(range(13))
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12]
our_list.extend(range(13,21))
# we want to end at 20
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

alpha = list('acdf')
alpha.insert(1, 'b')
alpha.insert(4, 'e')
# insert takes the index and the item you want to insert
# ['a','b','c','d','e','f']

a_list = list('abzcd')
a_list.index('z')
# 2
del a_list[2]
a_list
# ['a', 'b', 'c', 'd']

a_string = 'Hello'
del a_string
# a_string is deleted and undefined if referenced

a_num = 1234
del a_num
# a_num is deleted and undefined if referenced

my_list = [1,2,3,1]
my_list.remove(1)
# [2,3,1]
# removes first instance from the list

names = ['koda','erin','landon']
name_1 = names.pop(0)
name_3 = names.pop(2)