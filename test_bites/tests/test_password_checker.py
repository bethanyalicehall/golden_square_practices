from lib.password_checker import *
import pytest
'''
True is returned when a password
of 8 characters long is entered
'''
def test_password_8_chars():
    password_checker = PasswordChecker()
    assert password_checker.check("Password") == True

'''
True is returned when a password
of more than 8 characters long is entered
'''
def test_password_longer_than_8():
    password_checker = PasswordChecker()
    assert password_checker.check("Password1234") == True

'''
Error raised when a a shorter than
8 characters password is entered
'''
def test_incorrect_password_raises_error():
    password_checker = PasswordChecker()
    with pytest.raises(Exception, match=r".*Invalid password, must be 8\+ characters\..*"):
        password_checker.check("Dog")
        password_checker.check()

'''
Error raised when an empty string
is entered as a password
'''
def test_empty_password_raises_error():
    password_checker = PasswordChecker()
    with pytest.raises(Exception, match=r".*Invalid password, must be 8\+ characters\..*"):
        password_checker.check("")
        password_checker.check()
