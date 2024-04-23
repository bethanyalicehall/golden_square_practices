from lib.present import *
import pytest
'''
An error message is displayed if 
the contents is already wrapped
'''
def test_wrap_raises_exception_if_contents_already_wrapped():
    present = Present()
    present.wrap("A football")
    with pytest.raises(Exception) as e:
        present.wrap("A laptop")
    error_message = str(e.value)
    assert error_message == "A contents has already been wrapped."
'''
An alternative more concise way
to do the above test
'''
def test_wrap_raises_if_present_already_contains_contents():
    present = Present()
    present.wrap("A football")
    with pytest.raises(Exception, match=r"A contents has already been wrapped."):
        present.wrap("A Laptop!")

'''
An error message is displayed if 
no contents have been wrapped
'''
def test_wrap_raises_exception_if_nothing_is_wrapped():
    present = Present()
    with pytest.raises(Exception) as e:
        present.unwrap()
    error_message = str(e.value)
    assert error_message == "No contents have been wrapped."

'''
An alternative more concise way
to do the above test
'''
def test_wrap_raises_if_nothing_wrapped():
    present = Present()
    with pytest.raises(Exception, match=r"No contents have been wrapped."):
        present.unwrap()