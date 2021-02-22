'''
This module allows to carry out navigation through any json file.
'''
import json
def read_json_file(path):
    """
    Reads json file and returns it in dictionary format
    """
    json_file = open(path,mode="r",encoding="UTF-8")
    json_data = json_file.read()
    obj = json.loads(json_data)
    return obj


def navigation(obj):
    """
    Goes through json file and shows its structure
    """
    if isinstance(obj,dict):
        print()
        print("This object is dictionary")
        keys = list(obj.keys())
        print()
        print(keys)
        print()
        user_choice = input("Here are keys of this dictionary. \
Please enter name of key you want to see: ")
        next_element = obj[user_choice]
    elif isinstance(obj,list):
        print()
        print("This object is list.")
        print()
        user_choice = input('This list consists of '+str(len(obj))+' elements. \
Please enter number from 0 to '+str(len(obj)-1)+' \
to choose number of element you want to display: ')
        next_element = obj[int(user_choice)]
    else:
        print()
        user_choice = ''
        if isinstance(obj,str):
            user_choice = input('This object is a string. Do you want to display it?\
(Enter yes or no): ')
        elif isinstance(obj,bool):
            user_choice = input('This object is a boolean. Do you want to display it?\
(Enter yes or no): ')
        elif isinstance(obj,int):
            user_choice = input('This object is a integer. Do you want to display it?\
(Enter yes or no): ')
        elif isinstance(obj,float):
            user_choice = input('This object is a float number. Do you want to display it?\
(Enter yes or no): ')
        else:
            print(obj)
        if user_choice == 'yes':
            print(obj)
        print()
        print('This is the end of the file.')
        return 0
    return navigation(next_element)

if __name__ == '__main__':
    path_to_file = input('Enter path to file: ')
    navigation(read_json_file(path_to_file))
