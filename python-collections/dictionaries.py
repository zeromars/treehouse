#lists are great but dictionaries are used when you want to access by name and not index
#can consist of integers and strings
my_dict = {'name': 'koda'}
my_dict
# 'koda'

my_dict = {'name': 'koda',0:'stinker'}
my_dict
# {0: 'stinker', 'name': 'koda'}
my_dict[0]
# 'stinker'
my_dict['name']
# 'koda'
my_dict = {'name': 'koda',0:'stinker','another':6}
my_dict['another']
# 6
my_dict = {'name': 'koda',0:'stinker','another':6,'list':[1,2,3,4,5,6,7,8,9]}
my_dict['list']
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
my_dict['list'][4]
# 5

game_dict = {(2,2): True, (12,2): False}
game_dict[(1,2)]
#False

# my_dict = {'apples': 1, 'bananas': 2, 'coconuts': 3}
# my_list = ['apples', 'coconuts', 'grapes', 'strawberries']
# members(my_dict, my_list) => 2

def members(my_dict,my_list):
    answer = 0
    for item in my_list:
        if item in my_dict:
            answer += 1
    return answer

#################Deleting Keys##################
my_dict = {'name': 'koda',0:'stinker','another':6}
del my_dict['another']
#{0: 'stinker', 'name': 'koda'}
#################Adding Keys##################
my_dict['age'] = 33
# {0: 'stinker', 'age': 33, 'name': 'koda'}
my_dict['age'] = 34
# {0: 'stinker', 'age': 34, 'name': 'koda'}

my_dict.update({'job':'teacher','age':33})
#{0: 'stinker', 'age': 33, 'name': 'koda', 'job': 'teacher'}

# E.g. word_count("I am that I am") gets back a dictionary like:
# {'i': 2, 'am': 2, 'that': 1}
# Lowercase the string to make it easier.
# Using .split() on the sentence will give you a list of words.
# In a for loop of that list, you'll have a word that you can
# check for inclusion in the dict (with "if word in dict"-style syntax).
# Or add it to the dict with something like word_dict[word] = 1.

def word_count(phrase):
    answer = {}
    split = phrase.lower().split(" ")
    for word in split:
        if word not in answer:
            answer[word] = 1
        else:
            answer[word] = answer[word] + 1
    return answer

my_string = "Hi! My name is {name} and I live in {state}"
my_string.format(name='Koda', state='Cali')
# 'Hi! My name is Koda and I live in Cali'

my_dict = {'name': 'Landon', 'state': 'California'}
my_string.format(**my_dict)
# 'Hi! My name is Landon and I live in California'

dicts = [
    {'name': 'Michelangelo',
     'food': 'PIZZA'},
    {'name': 'Garfield',
     'food': 'lasanga'},
    {'name': 'Walter',
     'food': 'pancakes'},
    {'name': 'Galactus',
     'food': 'worlds'}
]

string = "Hi, I'm {name} and I love to eat {food}!"

def string_factory(dicts, string):
    answer = []
    x = 0
    for item in dicts:
        answer.insert(x,string.format(**item))
        x+=1
    return answer

my_dict = {'name': 'Landon', 'age': 36, 'state': 'California'}

for key in my_dict:
    print(my_dict[key])

for value in my_dict.values():
    print(value)

#
#  The dictionary will be something like:
# {'Jason Seifer': ['Ruby Foundations', 'Ruby on Rails Forms', 'Technology Foundations'],
#  'Kenneth Love': ['Python Basics', 'Python Collections']}
#
# Often, it's a good idea to hold onto a max_count variable.
# Update it when you find a teacher with more classes than
# the current count. Better hold onto the teacher name somewhere
# too!
#
# Your code goes below here.
def most_classes(teachers):
    max_count = 0
    teacher_name = ''
    for teacher in teachers:
        if len(teachers[teacher]) > max_count:
            max_count = len(teachers[teacher])
            teacher_name = teacher
    return teacher_name
def num_teachers(teachers):
    count = 0
    for teacher in teachers:
        count+=1
    return count
def stats(teachers):
    answers = []
    x=0
    for teacher in teachers:
        answers.insert(x,[teacher, len(teachers[teacher])])
        x+=1
    return answers
