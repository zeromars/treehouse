# make a list to hold onto items
shopping_list = []

def add_to_list(new_item):
    # add new items
    shopping_list.append(new_item)
    print("Added {}. List now has {} items.".format(new_item, len(shopping_list)))

def show_list():
    # print the list
    print("Here is your items:")
    for item in shopping_list:
        print(item)

def show_help():
    # print instructions
    print("What should we pick up at the store")
    print("Enter DONE to stop adding items")

show_help()

while True:
    # ask for new items
    new_item = input("> ")

    # be able to quit the app
    if new_item == 'DONE':
        break
    elif new_item == 'HELP':
        show_help()
        continue
    elif new_item == 'SHOW':
        show_list()
        continue
    add_to_list(new_item)

show_list()