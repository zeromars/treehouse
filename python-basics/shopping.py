shopping_list = []
is_done = True

def take_order():
    return input("What do you want to add to your list? ")

def add_to_cart(item):
    shopping_list.append(item)

print("Lets's start to shop!")
while is_done:
    item = take_order()
    if item == "DONE":
        is_done = False
        print(shopping_list)
        break
    elif item == "SHOW":
        print(shopping_list)
    elif item == "HELP":
        print("""Available commands are:
            HELP: show this message
            SHOW: show items in your list
            DONE: quit this app""")
    else:
        is_done = True
        add_to_cart(item)
        print("added " + item + " to your cart")