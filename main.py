'''
    Main code thats executed
'''

import classes

standard_tuning = ['E','A','D','G','B','E']


guitar = classes.Guitar(standard_tuning)
guitar.show_all_notes()

key_input = input('KEY  : ')
key = classes.String(key_input)
key.check()
guitar.find_notes(key_input)


user_input = '000'

while user_input != '0':
    user_input = input('Enter the numbers in the key (0 to exit and 000 for all notes in the key)')
    guitar.show_key(user_input)