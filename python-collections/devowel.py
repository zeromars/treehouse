#pass in a word
#remove all vowels
#capitalize the first letter
#return word

vowels = ['a','e','i','o','u']

word = input("Give me a word to chew on!")

word_list = list(word.lower())

for vowel in vowels:
    while True:
        try:
            word_list.remove(vowel)
        except:
            break
print(word_list)
#for letter in word_list:
#    index = word_list.index(letter)
#    print("Checking......{} at {} and a length".format(letter, index))
    #if letter in vowels:
    #    print("Found {} at index {} removing that now! Invaders must die!".format(letter, index))
    #    del word_list[index]
    #else:
    #    print("Found nothing with {} at {}".format(letter, index))
#print(word_list)