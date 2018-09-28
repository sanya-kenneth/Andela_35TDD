import unittest
from utilities import validate_password,validate_username_name
from app import User,users


class TDDTestcase(unittest.TestCase):
    def test_user_can_sign_up(self):
        user = User()
        register = user.register("sanya","Kenneth",25,"sanyakenneth@gmail.com","K1n.","male")
        self.assertEqual("Your account has been successfuly created",register)
        user.empty_db()
        
    def test_user_can_login(self):
        user = User()
        user.register("sanya","Kenneth",25,"sanyakenneth@gmail.com","K1n.","male")
        login = user.login("sanyakenneth@gmail.com","K1n.")
        self.assertIn("You are now loggedin",login)
        user.empty_db()
    
    def test_user_can_change_email(self):
        user = User()
        user.register("sanya","Kenneth",25,"sanyakenneth@gmail.com","K1n.","male")
        user.login("sanyakenneth@gmail.com","K1n.")
        change_email = user.change_email("zen@gmail.com")
        self.assertEqual("Your email was successfuly changed",change_email)

    def test_user_can_change_password(self):
        user = User()
        user.register("sanya","Kenneth",25,"sanyakenneth@gmail.com","K1n.","male")
        user.login("sanyakenneth@gmail.com","K1n.")
        change_password = user.change_password("Gh4|")
        self.assertEqual("your password was successfuly changed",change_password)


