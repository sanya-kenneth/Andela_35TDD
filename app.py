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

    def login(self,email,pass_word):
        for user_details in users:
            if email == user_details['email'] and pass_word == user_details['password']:
                user_details['status'] = True # Capture user login status
                
               
               
                        
               
               


sanya = User()
sanya.register("sanya","skimo",25,"sanyakenneth@gmail.com","ok","male")
sanya.login("sanyakenneth@gmail.com","ok")
# print(users)

    

    

