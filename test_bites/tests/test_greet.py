from lib.greet import *

def test_says_hello():
    name = "Bethany"
    result = greet(name)
    assert result == f"Hello, {name}!"
