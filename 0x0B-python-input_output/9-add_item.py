#!/usr/bin/python3
'''
Write a script that adds all arguments to a Python list
'''
from sys import argv

save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

try:
    list2add = load_from_json_file('add_item.json')
except:
    list2add = []

for arg in argv[1:]:
    list2add.append(arg)
save_to_json_file(list2add, 'add_item.json')
