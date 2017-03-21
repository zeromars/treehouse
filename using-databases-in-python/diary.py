from collections import OrderedDict
import datetime
import sys
import os

from peewee import *

db = SqliteDatabase('diary.db')

#always use singular names (it represents one item in the db)
class Entry(Model):
    content = TextField()
    timestamp = DateTimeField(default=datetime.datetime.now)
    # now vs now() because it will run the () and set it to when the script was run not the entry was created

    #defines what db this class belongs to
    class Meta:
        database = db

def menu_loop():
    choice = None
    while choice != 'q':
        clear()
        print("Enter q to quit")
        for key, value in menu.items():
            print('{}) {}'.format(key, value.__doc__))
        choice = input('Action: ').lower().strip()
        if choice in menu:
            clear()
            menu[choice]()

def add_entry():
    """Add an Entry"""
    print("Enter your darkest secrets. Press control + m when finished")
    data = sys.stdin.read().strip()
    if data:
        if input('Save this? [Y]es or [N]o').lower() != 'n':
            Entry.create(content=data)            
            print("Saved successfully")

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def search_entries():
    """search entries"""
    view_entries(input('Search Query: '))

def view_entries(search_query=None):
    """View previous Entries"""
    entries = Entry.select().order_by(Entry.timestamp.desc())
    if search_query:
        entries = entries.where(Entry.content.contains(search_query))
    for entry in entries:
        timestamp = entry.timestamp.strftime('%A %B %d, %Y %I:%M%p')
        # %A = weekday name
        # %B = month
        # %d = day
        # %Y = year
        # %I = hour (12 hour clock)
        # %M = minute
        # %p = am/pm
        clear()
        print(timestamp)
        print('='*len(timestamp))
        print(entry.content)
        print('\n\n' + '='*len(timestamp))
        print('n) for next entry')
        print('d) delete current entry')
        print('q) return to next menu')

        next_action = input('Action: [N]ext Entry / [Q]uit to main menu ').lower().strip()

        if next_action == 'q':
            break
        elif next_action == 'd':
            delete_entries(entry)

def delete_entries(entry):
    """Delete an Entry"""
    if input('Are you Sure? [Y]es or [N]o').lower() == 'y':
        entry.delete_instance()
        print("Deleted Successfully")

def init():
    db.connect()
    db.create_tables([Entry], safe=True)

menu = OrderedDict([
    ('a', add_entry),
    ('v', view_entries),
    ('s', search_entries),    
])

#if the file is load directly and not imported
if __name__ == '__main__':
    init()
    menu_loop()