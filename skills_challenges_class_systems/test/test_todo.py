import pytest
from lib.todo import Todo

'''
Initially has an empty
list of incomplete tasks
'''
def test_initially_task_complete_is_false():
    todo = Todo("task")
    assert not todo.complete

'''
Initialisation of object
with correct task
'''
def test_returns_task():
    todo = Todo("Walk dog")
    assert todo.task == "Walk dog"

'''
Raises an error when
a non-string type is entered
'''
def test_raises_error_if_not_string():
    with pytest.raises(TypeError, match=r"Task must be a string"):
        todo = Todo(7)

