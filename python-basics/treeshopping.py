# make a list to hold onto items
shopping_list = []

# print instructions
print("What should we pick up at the store")
print("Enter DONE to stop adding items")

while True:
    # ask for new items
    new_item = input("> ")

    # be able to quit the app
    if new_item == 'DONE':
        break

    # add new items
    shopping_list.append(new_item)

# print the list
print("Here is your items:")
for item in shopping_list:
    print(item)