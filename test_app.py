import unittest
from utilities import validate_password,validate_username_name
from app import User,users


class TDDTestcase(unittest.TestCase):
    def setUp(self):
        self.user = User("sanya","Kenneth",24,"sanyakenneth@gmail.com","K1n.lll","male")
        self.check_age_is_int = User("sanya","Kenneth","24","sanyakenneth@gmail.com","K1n.lll","male")
        self.check_age_is_less_than_zero = User("sanya","Kenneth",-9,"sanyakenneth@gmail.com","K1n.lll","male")
        self.check_email_is_valid = User("sanya","Kenneth",24,"sanyakennethgmail.com","K1n.lll","male")
        self.check_password_short = User("sanya","Kenneth",24,"sanyakenneth@gmail.com","K1.l","male")
        self.check_password_special_characters = User("sanya","Kenneth",24,"sanyakenneth@gmail.com","K1NinLLL","male")
        

    def test_user_can_sign_up(self):
        register = self.user.register()
        self.assertEqual("Your account has been successfuly created",register)
        self.user.empty_db()
        
    def test_user_can_login(self):
        self.user.register()
        login = self.user.login("sanyakenneth@gmail.com","K1n.lll")
        self.assertEqual("You are now loggedin",login)
        self.user.empty_db()
    
    def test_user_can_change_email(self):
        self.user.register()
        self.user.login("sanyakenneth@gmail.com","K1n.lll")
        change_email = self.user.change_email("zen@gmail.com")
        self.assertEqual("Your email was successfuly changed",change_email)
        self.user.empty_db()

    def test_user_can_change_password(self):
        self.user.register()
        self.user.login("sanyakenneth@gmail.com","K1n.lll")
        change_password = self.user.change_password("Gh4|l")
        self.assertEqual("your password was successfuly changed",change_password)
        self.user.empty_db()

    def test_loggedin_user_can_view_their_info(self):
        self.user.register()
        self.user.login("sanyakenneth@gmail.com","K1n.lll")
        info = self.user.my_info()
        self.assertIsInstance(info,dict)

    def test_app_can_empty_db(self):
        self.user.register()
        empty_db = self.user.empty_db()
        self.assertEqual("Database has been emptied",empty_db)
        self.assertEqual(users,[])

    def test_returns_error_if_user_inputs_an_empty_name_or_username_on_signup(self):
        validateusername_name = validate_username_name("","sanya")
        self.assertEqual("Username or Name can not be empty",validateusername_name)
        validateusername_name = validate_username_name("sanya","")
        self.assertEqual("Username or Name can not be empty",validateusername_name)

    def test_returns_error_if_user_inputs_a_short_username_on_signup(self):
        validateusername_name = validate_username_name("sanya","s")
        self.assertEqual("Username must be atleast 4 characters",validateusername_name)

    def test_returns_error_if_user_inputs_a_space_witnin_name_or_username_on_signup(self):
        validateusername_name = validate_username_name("sa  nya","skimogreen")
        self.assertEqual("Spaces are not allowed",validateusername_name)
        validateusername_name = validate_username_name("sanya"," skimogreen")
        self.assertEqual("Spaces are not allowed",validateusername_name)

    def test_returns_true_if_username_and_name_credentials_are_valid(self):
        validateusername_name = validate_username_name("sanya","skimogreen")
        self.assertEqual(True,validateusername_name)

    def test_validate_password_returns_false_if_password_provided_has_no_capital_letter(self):
        validateuserpassword = validate_password("sany1@a")
        self.assertEqual(False,validateuserpassword)

    def test_validate_password_returns_false_if_password_provided_has_no_small_letter(self):
        validateuserpassword = validate_password("SANY1@A")
        self.assertEqual(False,validateuserpassword)

    def test_validate_password_returns_false_if_password_provided_has_no_number_or_digit(self):
        validateuserpassword = validate_password("sanY@a")
        self.assertEqual(False,validateuserpassword)

    def test_validate_password_returns_false_if_password_provided_has_no_special_character(self):
        validateuserpassword = validate_password("sany1A")
        self.assertEqual(False,validateuserpassword)

    def test_validate_password_returns_True_if_password_provided_is_valid(self):
        validateuserpassword = validate_password("sany1@A")
        self.assertEqual(True,validateuserpassword)

    def test_signup_returns_error_if_age_is_not_of_type_int(self):
        register = self.check_age_is_int.register()
        self.assertEqual( "Age provided is not valid!",register)

    
    def test_signup_returns_error_if_age_is_less_than_zero(self):
        register = self.check_age_is_less_than_zero.register()
        self.assertEqual( "Age provided is not valid!",register)

    def test_signup_returns_error_if_email_is_invalid(self):
        register = self.check_email_is_valid.register()
        self.assertEqual( "Invalid email!",register)

    def test_signup_returns_error_if_password_lacks_capital_letter_small_letter_a_digit_or_special_character(self):
        register = self.check_password_special_characters.register()
        self.assertEqual( "Password must contain a capital letter, a small letter, a number and a special character!",register)

    def test_signup_returns_error_if_password_is_short(self):
        register = self.check_password_short.register()
        self.assertEqual( "password too short",register)










