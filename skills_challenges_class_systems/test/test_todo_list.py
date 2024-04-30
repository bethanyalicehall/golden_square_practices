import pytest
from lib.todo_list import TodoList

'''
Initially has an empty
list of incomplete tasks
'''
def test_initially_has_empty_list_of_incomplete_tasks():
    todo_list = TodoList()
    assert todo_list.incomplete() == []

'''
Initially has an empty
list of complete tasks
'''
def test_initially_has_empty_list_of_complete_tasks():
    todo_list = TodoList()
    assert todo_list.complete() == []

