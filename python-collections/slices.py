##########################Slices######################
my_string = "Hello there"
my_string[1:5]
# 'ello'

my_list = list(range(1,6))
my_list[1:3]
# [2,3]

my_list[2:len(my_list)]
# [3,4,5]

my_list[:2]
# [1,2]

my_list[2:]
# [3,4,5]

my_list[:]
# [1,2,3,4,5]

#useful for when you need to store a copy of the list
my_new_list = [4,2,1,3,5]
my_new_list.sort()
#sorts them smallest to largest
# [1,2,3,4,5]
my_new_list = [4,2,1,3,5]
my_sorted_list = my_new_list[:]
my_sorted_list.sort()
# [1,2,3,4,5]
my_new_list
#[4,2,1,3,5]
##########################Slice Steps######################
my_list = list(range(20))
# go from the beginning to the end and add 2 each time
my_list[::2]
# [0,2,4,6,8,10,12,14,16,18]

"Alaska"[::2]
# 'Aak'

"Alaska"[::-1]
# 'aksalA'

my_list[2:8:-1]
# []
# cannot start at 2 and subtract 1 and get to 1

my_list[8:2:-1]
# [8,6,5,4,3]

def first_and_last_4(item):
    return item[:4] + item[-4:]

first_and_last_4('Oklahoma')
# 'Oklahoma'
##########################Deleting or replacing slices######################
my_list = [1,2,'a','b','c','d',5,6,7,'h']
del my_list[:2]
# ['a','b','c','d',5,6,7,8,'h']
my_list[4:7] = ['e','f']
# ['a','b','c','d','e','f',7,8,'h']
my_list[8:10] = ['g']
# ['a','b','c','d','e','f','g','h']