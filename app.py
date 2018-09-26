users = []

class User(object):

    def register(self,name,username,age,email,password,gender):
        self.name = name
        self.username = username
        self.age = age
        self.email = email
        self.password = password
        self.gender = gender

        user_data =  {
                        'name': self.name,
                        'username': self.username,
                        'age': self.age,
                        'email': self.email,
                        'password':self.password,
                        'gender':self.gender
                    }

        users.append(user_data)


sanya = User()
sanya.register("sanya","skimo",25,"sanyakenneth@gmail.com","ok","male")
print(users)

    

    

