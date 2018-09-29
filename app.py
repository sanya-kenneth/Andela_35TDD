from utilities import validate_username_name,validate_password
from validate_email import validate_email


users = []
class User(object):
    def __init__(self,*args,**kwargs):
        self.name = args[0]
        self.username = args[1]
        self.age = args[2]
        self.email = args[3]
        self.password = args[4]
        self.gender = args[5]
        self.status = False

    def register(self):
        is_valid_name = validate_username_name(self.name ,self.username)
        is_valid_email = validate_email(self.email)
        is_valid_password = validate_password(self.password)
        if is_valid_password != True or is_valid_email != True:
            return "Invalid email or Password!"
        elif len(self.password) <5:
            return "password too short"
        if  type(self.age) != int or self.age < 0:
            return "Age provided is not valid!"
        if is_valid_name == True:
            user_data =  {
                        'name': self.name,
                        'username': self.username,
                        'age': self.age,
                        'email': self.email,
                        'password':self.password,
                        'gender':self.gender,
                        'status': self.status
                        }

            users.append(user_data)
            return "Your account has been successfuly created"
       
    def login(self,email,password):
        is_valid_email = validate_email(email)
        is_valid_password = validate_password(password)
        if is_valid_password != True:
            return "Password must contain a capital letter, a small letter, a number and a special character!"
        if is_valid_email != True:
            return "Invalid email!"
        for user_details in users:
            if email == user_details['email'] and password == user_details['password']:
                user_details['status'] = True # Capture user login status
                return "You are now loggedin"
            else:
                return "Failed to login"
        
    def change_email(self,email):
        is_valid_email = validate_email(email)
        if is_valid_email == True:
            for data in users:
                if data['status'] == True: 
                    data['email'] = email
                    return "Your email was successfuly changed"
                else:
                    return "You can't change email while logged out"
        else:
            return "Invalid email"

    def change_password(self,password):
        is_valid_password = validate_password(password)
        if is_valid_password != True:
            return "Password must contain a capital letter, a small letter, a number and a special character!"
        for user_details in users:
            if user_details['status'] == True: #check if user is loggedin
                user_details['password'] = password
                return "your password was successfuly changed"
            else:
                return "You can't change password while logged out"

    def my_info(self):
        for user_details in users:
            if user_details['status'] == True:
                print(user_details)
                return user_details
            else:
                return "Nothing to show"

    def empty_db(self):
        users.clear()
        return "Database has been emptied"

                

               
               




    

    

