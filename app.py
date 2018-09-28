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
            print("Check your password")
            return "Password must contain a capital letter, a small letter, a number and a special character!"
        if is_valid_email != True:
            return "Invalid email!"
        elif age <= 0 or type(age) != int:
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
            print(user_data)
       

    
    def login(self,email,pass_word):
        for user_details in users:
            if email == user_details['email'] and pass_word == user_details['password']:
                user_details['status'] = True # Capture user login status

                
               
               
                        
               
               


sanya = User()
sanya.register("sanya","Kenneth",25,"sanyakenneth@gmail.com","OK1now.","male")
sanya.login("sanyakenneth@gmail.com","k")

    

    

