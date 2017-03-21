import re

names_file = open("names.txt", encoding="utf-8")
data = names_file.read()
names_file.close()
# print(data)

print(re.match(r'Love', data))
#match starts at the beginning

#search - searches the entire string
print(re.search(r'Kenneth', data))

# \w - matches an Unicode word character. That's any letter, uppercase or lowercase, numbers, and the underscore character. In "new-releases-204", \w would match each of the letters in "new" and "releases" and the numbers 2, 0, and 4. It wouldn't match the hyphens.
# \W - is the opposite to \w and matches anything that isn't an Unicode word character. In "new-releases-204", \W would only match the hyphens.
# \s - matches whitespace, so spaces, tabs, newlines, etc.
# \S - matches everything that isn't whitespace.
# \d - is how we match any number from 0 to 9
# \D - matches anything that isn't a number.
# \b - matches word boundaries. What's a word boundary? It's the edges of word, defined by white space or the edges of the string.
# \B - matches anything that isn't the edges of a word.
# Two other escape characters that we didn't cover in the video are \A and \Z. These match the beginning and the end of the string, respectively. As we'll learn later, though, ^ and $ are more commonly used and usually what you actually want.

# \( to get a () since parenthesis has a special meaning in python
print(re.search(r'\(\d\d\d\) \d\d\d-\d\d\d\d', data))

#Now, write a function named numbers() that takes two arguments: a count as an integer and a string. Return an re.search for exactly count numbers in the string. Remember, you can multiply strings and integers to create your pattern.

#For example: r"\w" * 5 would create r"\w\w\w\w\w".

#import re

def first_number(item):
    return  re.search(r'\d', item)

def numbers(count, item):
    return re.search(r'\d'*count, item)

# \w{3} - matches any three word characters in a row.
# \w{,3} - matches 0, 1, 2, or 3 word characters in a row.
# \w{3,} - matches 3 or more word characters in a row. There's no upper limit.
# \w{3, 5} - matches 3, 4, or 5 word characters in a row.
# \w? - matches 0 or 1 word characters.
# \w* - matches 0 or more word characters. Since there is no upper limit, this is, effectively, infinite word characters.
# \w+ - matches 1 or more word characters. Like *, it has no upper limit, but it has to occur at least once.
# .findall(pattern, text, flags) - Finds all non-overlapping occurrences of the pattern in the text.

print(re.findall(r'\(?\d{3}\)?-?\s?\d{3}-\d{4}', data))
# findalls in all the text
# \)? optional open paren
# \d{3} 3 digits
# \)? optional closing parens
# -? optional hyphen
# \s? optional space
# \d{3} 3 digits
# -
# \d{4} 4 digits

print(re.search(r'\w+, \w+', data))
# will get last_name, first_name 
print(re.search(r'\w*, \w+', data))
#will get , first_name #no last name

# Create a function named phone_numbers that takes a string and returns all of the phone numbers in the string using re.findall(). The phone numbers will all be in the format 555-555-5555.

# import re

def phone_numbers(item):
    return re.findall(r'\d{3}-\d{3}-\d{4}', item)

#Create a function named find_words that takes a count and a string. Return a list of all of the words in the string that are count word characters long or longer.

#import re

# EXAMPLE:
# >>> find_words(4, "dog, cat, baby, balloon, me")
# ['baby', 'balloon']

def find_words(count, item):
    return re.findall(r'\w{'+str(count)+'}', item)

# [abc] - this is a set of the characters 'a', 'b', and 'c'. It'll match any of those characters, in any order, but only once each.
# [a-z], [A-Z], or [a-zA-Z] - ranges that'll match any/all letters in the English alphabet in lowercase, uppercase, or both upper and lowercases.
# [0-9] - range that'll match any number from 0 to 9. You can change the ends to restrict the set.
# ^ = ignore

print(re.findall(r'[-\w\d+.]+@[-\w\d.]+', data))
# [-\w\d+.]+ = they can have letters, numbers, periods, hyphens, and plus signs
    # [ = opening group
    # [- =  add hyphen
    # [-\w =  letters
    # [-\w\d =  digits
    # [-\w\d+ =  plus sign
    # [-\w\d+. =  periods
    # [-\w\d+.] = close group
    # [-\w\d+.]+ = group can happen more than once
# @ = @ sign
# [-\w\d.]+ = all the same minus plus signs

print(re.findall(r'\b[trehous]{9}\b', data, re.IGNORECASE))
# re.IGNORECASE = re.I
print(re.findall(r'\b[trehous]{9}\b', data, re.I))
# \b = word boundry
# [trehous] = find any of these letters
# {9} = there has to be 9 of those letters to count
# \b word boundry

# Find a word boundry , a @ and then any number of letters
#ignore one or more instance of gov and a tab
print(re.findall(r'''
    \b@[-\w\d.]*
    [^gov\t]+
    \b
''', data, re.VERBOSE|re.I))
# re.VERBOSE = re.X
# ''' multi line string start
# \b = word boundry
# @ = @ sign
# [-\w\d.]* = they can have any amount of letters, numbers, periods, hyphens, and plus signs
# [^gov\t]+ = ignore gov and tab
# \b = word boundry end
# ''' end multiline string
# re.VERBOSE has to be used when using multiline strings
# | is used when adding more than one flags

print(re.findall(r'''
    \b[-\w]+, # Find a word boundry, 1+ hyphens or chars and a comma 
    \s # Find 1 whitespace
    [-\w ]+ # 1+ hyphens and a char with a EXPLICIT space
    [^\t\n] # ignore newlines and tabs
''', data, re.X))

# Create a variable named good_numbers that is an re.findall() where the pattern matches anything in string except the numbers 5, 6, and 7.

#import re

string = '1234567890'
good_numbers = re.findall(r'\[^567]', string)

print(re.findall(r'''
    ^(?P<name>[-\w ]+,\s[-\w ]+)\t # first and last names_file
    (?P<email>[-\w\d+.]+@[-\w\d.]+)\t #email
    (?P<phone>\(?\d{3}\)?-?\s?\d{3}-\d{4})?\t #phone number
    (?P<job>[\w\s]+,\s[\w\s.]+)\t? #job and company
    (?P<twitter>@[\w\d]+)?$ #twitter
''', data, re.X|re.M))

line = re.search(r'''
    ^(?P<name>[-\w ]+,\s[-\w ]+)\t # first and last names_file
    (?P<email>[-\w\d+.]+@[-\w\d.]+)\t #email
    (?P<phone>\(?\d{3}\)?-?\s?\d{3}-\d{4})?\t #phone number
    (?P<job>[\w\s]+,\s[\w\s.]+)\t? #job and company
    (?P<twitter>@[\w\d]+)?$ #twitter
''', data, re.X|re.M)

line.groupdict()

# Create a variable names that is an re.match() against string. The pattern should provide two groups, one for a last name match and one for a first name match. The name parts are separated by a comma and a space.

# import re

string = 'Perotto, Pier Giorgio'

names = re.match(r'([\w]+),\s([\w]+\s[\w]+)',string)


#Create a new variable named contacts that is an re.search() where the pattern catches the email address and phone number from string. Name the email pattern email and the phone number pattern phone. The comma and spaces * should not* be part of the groups.
#import re

string = '''Love, Kenneth, kenneth+challenge@teamtreehouse.com, 555-555-5555, @kennethlove
Chalkley, Andrew, andrew@teamtreehouse.co.uk, 555-555-5556, @chalkers
McFarland, Dave, dave.mcfarland@teamtreehouse.com, 555-555-5557, @davemcfarland
Kesten, Joy, joy@teamtreehouse.com, 555-555-5558, @joykesten'''

contacts = re.search(r'(?P<email>[-\w\d+.]+@[-\w\d.]+), (?P<phone>\d{3}-\d{3}-\d{4})', string)
print(contacts)

print(re.search(r'(?P<em1ail>[-\w\d+.]+@[-\w\d.]+)(?P<phone>\d{3}-\d{3}-\d{4})', string, re.X|re.M))

# re.compile(pattern, flags) - method to pre-compile and save a regular expression pattern, and any associated flags, for later use.
# .groupdict() - method to generate a dictionary from a Match object's groups. The keys will be the group names. The values will be the results of the patterns in the group.
# re.finditer() - method to generate an iterable from the non-overlapping matches of a regular expression. Very handy for for loops.
# .group() - method to access the content of a group. 0 or none is the entire match. 1 through how ever many groups you have will get that group. Or use a group's name to get it if you're using named groups.


print(re.search(line, data).groupdict())
print(line.search(data).groupdict())


line = re.compile(r'''
    ^(?P<name>(?P<first>[-\w ]*),\s(?P<last>[-\w ]+))\t # first and last names_file
    (?P<email>[-\w\d+.]+@[-\w\d.]+)\t #email
    (?P<phone>\(?\d{3}\)?-?\s?\d{3}-\d{4})?\t #phone number
    (?P<job>[\w\s]+,\s[\w\s.]+)\t? #job and company
    (?P<twitter>@[\w\d]+)?$ #twitter
''', re.X|re.M)

for match in line.search(data):
    print(match.value)

for match in line.finditer(data):
    print('{first} {last} <{email}>'.format(**match.groupdict()))

class Player:
    last_name = ''
    first_name = ''
    score = ''
    def __init__(self, last_name, first_name, score):
        self.last_name = last_name
        self.first_name = first_name
        self.score = score

