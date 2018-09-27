from utilities import validate_username_name


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
sanya.register("sanya","Kenneth",25,"sanyakenneth@gmail.com","ok","male")
# print(users)
sanya.login("sanyakenneth@gmail.com","ok")
# print(users)

    

    

