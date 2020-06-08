from unittest import TestCase
from unittest.mock import patch
from loginApp import Login


class LoginTest(TestCase):
    def test_login(self):


        with patch('builtins.print') as mock_login:
            Login.login("xxx", "1234")
            #mock_login.assert_called_with("Login Successful")
            mock_login.assert_called_with("Wrong Credentials")



