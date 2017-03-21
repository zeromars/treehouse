######################################General Notes##########################################
# python variables don't have to be created before used they are on demand
# python everything is a object
# functions assigned to objects are called methods
"""
Rules of Python (Syntax)
1.) Code inside a function is called a block and is indented 4 spaces by default
2.) Variables and functions should be lowercase with underscores
3.) Using dashes in variables and function names python will try and subtract things
4.) Single and double quotes are ok
5.) Cannot start a var a function with a number
"""
# REPL = read evaluate print loop
# exit() or quit() to leave shell
# help(print) - help about print function , q to get out of help
# when a vars reference count becomes 0 GC removes it
# del to remove var (not common)
######################################Numbers##########################################
# Addition , Subtraction, Multiplication gives you integers unless you are using floats
# Division gives you back floats always.
0.1 + 0.1 + 0.1 - 0.3
#5.55e-17
round(5.55e-17)
#0
int(5.2)
# 5
int(5.9)
# 5
int('5')
# 5 Strings to ints
float(5)
#5.0
age = 34
age += 7
age -= 9
#same as in javascript
######################################Strings##########################################
"""He's Right"""
# "He's Right"
'''He's Right'''
# "He's Right"
# triple quotes same as escaping strings with \ , also triple equals holds newlines and tabs
str(5)
# '5'
name = 'Koda '
name += 'Stinker'
print(name)
'=' * 20
# =====================
# You can ADD and MULTIPLY strings but cant subtract or divide them
status = "Hey there are {} visitors here"
status.format(7)
# Hey there are 7 visitors here
status = "Hey there are {} {} visitors here"
status.format(7, 'dogs')
# Hey there are 7 dogs visitors here
######################################Lists##########################################
# comma sep list in [ ]
my_list = [1,2,3]
my_list + [4,5]
# [1,2,3,4,5]
my_list
#[1,2,3] since there was no assignment
my_list = my_list + [4,5]
# [1,2,3,4,5]
my_list += [6,7]
# [1,2,3,4,5,6,7]
# Addition and Multiplication can be used but not division or subtraction
my_list * 2
#[1,2,3,4,5,6,7,1,2,3,4,5,6,7]
my_list.append(8)
# [1,2,3,4,5,6,7,8]
my_list.append([9,10])
# [1,2,3,4,5,6,7,8, [9,10]]
my_list.extend([11,12,13])
# [1,2,3,4,5,6,7,8,[9,10],11,12,13]
my_list.remove(13)
# [1,2,3,4,5,6,7,8,[9,10],11,12]
list('hello')
# ['h','e','l','l','o']
# list(5)
# int object not iterable
# split default is on spaces and whitespace
'hello:there'.split(':')
# ['hello','there']
flavors = ['chocolate','mint','strawberry']
', '.join(flavors)
# 'chocolate, mint, strawberry'
"My favorite flavors are: {}".format(', '.join(flavors))
#My favorite flavors are: chocolate, mint, strawberry
# only works on strings
######################################Indexes##########################################
alpha = 'abcde'
alpha.index('a')
# 0
alpha[2]
# c
alpha[-1]
# e
######################################Deletion#########################################
alpha_list = list('abcde')
del alpha_list[2]
# ['a','b','d','e']
# Strings are immutable, cant change part of it without changing it to a new string
# list are mutatable, you can add and remove items from the list and get back the same list object
######################################Ternary Operator#########################################
# True and False with capital letters

# (falseValue, trueValue)[bool(<expression>)]  == Tuple
# Expression has to return True or False
rawr = True
('nay', 'yay')[bool(rawr)]
# 'yay'

'yay' if rawr else 'nay'
# 'yay'
######################################Bool#########################################
bool("Treehouse")
# True
bool('')
# False (anything that is empty , 0 or none
bool(None)
# False
# Operator	Comparison
# ==	A is equal to B
# !=	A is not equal to B
# <	A is less than B
# >	A is greater than B
# <=	A is less than, or equal to, B
# >=	A is greater than, or equal to, B
# is	A has the same memory address as B
a = 5
b = 5
a is b
# True
c = []
d = []
c == d
# True
c is d
# False
e = None
e is None
# True
e == None
# True
######################################If Statements#########################################
# () are optional
age = 34 * 365
if age > 10000:
    print('yay')
elif age > 5000:
    print('meh')
else:
    print('nay')
if not age > 25000:
    print('nay')
######################################Containment#########################################
# Returns a bool
"java" in "javascript"
days_open = ['Monday', 'Tuesday']
today = 'Tuesday'
if today in days_open:
    print('come on in')
today = 'Wednesday'
if today not in days_open:
    print("were closed")
if not today in days_open:
    print("were closed")
######################################Loops#########################################
my_list = ['hello','how', 'are', 'you']
for word in my_list:
    print(word)
for letter in 'abcdefghijklmnopqrstuvwxyz':
    print(letter.upper())
for num in [1,2,3,4]:
    if num % 2 == 0:
        print(num)
start = 10
while start:
    print(start)
    start -= 1
names = ['Erin','Landon','Koda','Sheila','Dad','Tony','Kathy']
for name in names:
    if name == "Sheila":
        break
    print(name)
for name in names:
    if name == "Sheila" or name == "Tony":
        continue
    print(name)
######################################Inputs#########################################
# returns a str
age = int(input("What's your age? "))
year = int(age+1)
print("Next year you will be {}".format(year))
# "Next year you will be {}".format(year) works
# "Next year you will be " + (age+1) doesnt!
######################################Functions#########################################
def hows_the_parrot():
    print("He's pining for the fjords!")
hows_the_parrot()
def lumberjack(name = "Erin"):
    if name.lower() == 'koda':
        print(name + " is a lumberjack and he's OK!")
    else:
        print(name + " is not a lumberjack!")
hows_the_parrot()
lumberjack("Landon")
lumberjack("koda")
lumberjack()
######################################Trycatch#########################################
try:
    count = int(input("Give me a number: "))
except ValueError:
    print("Not a Number")
else:
    print("Your number is {}".format(count))
######################################AND/OR#########################################
    while 5 < 7 and 6 > 7:
        print('yay')
    while 5 < 7 or 6 > 7:
        print('yay')
######################################END#########################################
    print("letter", end='')
    #end allows python to print multiple things on the same line

    items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    for num in items:
        print(num, end='')
    # 1234567890
######################################isalpha#########################################
    '213f34t345g'.isalpha()
    # False
######################################os#########################################
#let you look and do things at the os level
import os
def clear():
    if os.name == 'nt':
        #windows
        os.system('cls')
    else:
        #mac
        os.system('clear')
######################################sys#########################################
#python itself
import sys
sys.exit()