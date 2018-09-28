import re


def validate_username_name(name,username):
    if username == "" or name == "": # check if username or name is empty
        return "Username or Name can not be empty"
    elif len(username)<4: # check if the the length of username is lessthan 4
        return "Username must be atleast 4 characters"
    elif (" " in username) == True or (" " in name) == True: #check for space in username provided
        return "Spaces are not allowed"
    else:
        return True 


def validate_password(password):
    match = re.search('[A-Z]+',password) #search for capital letters
    match2 = re.search('[a-z]+',password) # search for small letters
    match3 = re.search('[0-9]',password) # search for digits
    match4 = re.search('[^a-zA-Z0-9]',password) #search for special characters
    if match != None  and match2 != None and match3 != None and match4 != None:
        return True
    else:
        return False

