import unittest
import pyperclip
from user import User

class TestUser(unittest.TestCase):
  '''
  Test class that defines test cases for the user class behaviours.

  Args:
    unittest.TestCase: TestCase class that helps in creating user test cases
  '''
  def setUp(self):
    '''
    Set up method to run before each test cases in User
    '''
    self.new_user = User("Nicholas","Ngetich","0725470732","ngetichnicholas903@gmail.com") #creating user object

  def tearDown(self):
    '''
    tearDown method that does clean up after each test case has run.
    '''
    User.user_list = []

  def test_init(self):
    '''
    test_init test case to test if the object is initialized properly
    '''
    self.assertEqual(self.new_user.first_name,"Nicholas")
    self.assertEqual(self.new_user.last_name,"Ngetich")
    self.assertEqual(self.new_user.phone_number,"0725470732")
    self.assertEqual(self.new_user.email,"ngetichnicholas903@gmail.com")
  def test_save_user(self):
    '''
    test_save_user test case to test if the user object is saved into
    the user list
    '''
    self.new_user.save_user() #saving the user
    self.assertEqual(len(User.user_list),1)

  def test_save_multiple_user(self):
    '''
    test_save_multiple_user to check if we can save multiple contact
    objects to our contact list
    '''
    self.new_user.save_user()
    test_user = User("Nick","Korgoren","0714042437","nick@korgoren.com") #new user
    test_user.save_user()
    self.assertEqual(len(User.user_list),2)

  def test_delete_user(self):
    '''
    test_delete_user to test if we can remove a user from our user list
    '''