import pytest
from lib.todo import Todo
from lib.todo_list import TodoList

'''
Adds new todo to 
incomplete tasks list
'''
def test_adds_todo_to_incomplete_tasks_list():
    todo_list = TodoList()
    task_1 = Todo("Buy milk")
    todo_list.add(task_1)
    incomplete_tasks = [task.task for task in todo_list.incomplete()]
    assert incomplete_tasks == ["Buy milk"]

'''
Adds complete todo to 
complete tasks list
'''

def test_adds_todo_to_complete_tasks_list():
    todo_list = TodoList()
    task_1 = Todo("Walk dog")
    task_2 = Todo("Clean the house")
    todo_list.add(task_1)
    todo_list.add(task_2)
    task_1.mark_complete()
    complete_tasks = [task.task for task in todo_list.complete()]
    assert complete_tasks == ["Walk dog"]

'''
when #give_up is called all
tasks are marked as complete
'''

def test_marks_all_tasks_as_complete():
    todo_list = TodoList()
    task_1 = Todo("Walk dog")
    task_2 = Todo("Clean the house")
    task_3 = Todo("Mow the lawn")
    todo_list.add(task_1)
    todo_list.add(task_2)
    todo_list.add(task_3)
    todo_list.give_up()
    complete_tasks = [task.task for task in todo_list.complete()]
    assert complete_tasks == ["Walk dog", "Clean the house", "Mow the lawn"]

