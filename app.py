from utilities import validate_username_name,validate_password
from validate_email import validate_email


users = []
class User(object):
    def register(self,name,username,age,email,password,gender):
        self.name = name
        self.username = username
        self.age = age
        self.email = email
        self.password = password
        self.gender = gender
        self.status = False
        is_valid_name = validate_username_name(self.name ,self.username)
        is_valid_email = validate_email(self.email)
        is_valid_password = validate_password(self.password)
        if is_valid_password != True:
            return "Password must contain a capital letter, a small letter, a number and a special character!"
        elif len(self.password) <5:
            return "password too short"
        if is_valid_email != True:
            return "Invalid email!"
        elif  type(self.age) != int or self.age < 0:
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
       
    def login(self,email,pass_word):
        self.email = email
        self.password = pass_word
        is_valid_email = validate_email(self.email)
        is_valid_password = validate_password(self.password)
        if is_valid_password != True:
            return "Password must contain a capital letter, a small letter, a number and a special character!"
        if is_valid_email != True:
            return "Invalid email!"
        for user_details in users:
            if self.email == user_details['email'] and self.password == user_details['password']:
                user_details['status'] = True # Capture user login status
                return "You are now loggedin"
        
    def change_email(self,email):
        self.email = email
        is_valid_email = validate_email(self.email)
        if is_valid_email != True:
            return "Invalid email!"
        for user_details in users:
            if user_details['status'] == True: #check if user is loggedin
                user_details['email'] = self.email
                return "Your email was successfuly changed"
            else:
                return "You can't change email while logged out"

    def change_password(self,pass_word):
        self.password = pass_word
        is_valid_password = validate_password(self.password)
        if is_valid_password != True:
            return "Password must contain a capital letter, a small letter, a number and a special character!"
        for user_details in users:
            if user_details['status'] == True: #check if user is loggedin
                user_details['password'] = self.password
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

                
               
               
                        
               
               




    

    

