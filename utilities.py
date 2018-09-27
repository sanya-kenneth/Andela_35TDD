def validate_username_name(name,username):
    if username == "" or name == "":
        print("Username or Name can not be empty")
        return "Username or Name can not be empty"
    elif len(username)<4:
        print( "Username must be atleast 4 characters")
        return "Username must be atleast 4 characters"
    elif (" " in username) == True or (" " in name) == True:
        print("Spaces are not allowed")
        return "Spaces are not allowed"
    else:
        return True 
