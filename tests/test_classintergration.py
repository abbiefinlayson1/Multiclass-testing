from lib.todo import *
from lib.todo_list import *

def test_add_task_to_todo_list():
    todo = Todo("wash my hair")
    todo_list = TodoList()
    todo_list.add(todo)
    assert len(todo_list.todo_list) == 1


def test_add_multiple_task_to_todo_list():
    todo1 = Todo("wash my hair")
    todo2 = Todo("wash my dog")
    todo_list = TodoList()
    todo_list.add(todo1)
    todo_list.add(todo2)
    assert len(todo_list.todo_list) == 2

def test_incomplete():
    todo1 = Todo("wash my hair")
    todo2 = Todo("buy shopping")
    todo3 = Todo("do homework")
    
    todo_list = TodoList()
    todo_list.add(todo1)
    todo_list.add(todo2)
    todo_list.add(todo3)
    
    todo2.mark_complete()  
    incomplete_tasks = todo_list.incomplete()
    
    assert len(incomplete_tasks) == 2 
    assert incomplete_tasks[0].task == "wash my hair"
    assert incomplete_tasks[1].task == "do homework"

def test_complete_list():
    todo1 = Todo("wash my hair")
    todo2 = Todo("buy shopping")
    todo3 = Todo("do homework")
    
    todo_list = TodoList()
    todo_list.add(todo1)
    todo_list.add(todo2)
    todo_list.add(todo3)
    
    todo2.mark_complete()  
    complete_tasks = todo_list.complete()
    
    assert len(complete_tasks) == 1
    assert complete_tasks[0].task == "buy shopping"

def test_give_up():
    todo1 = Todo("wash my hair")
    todo2 = Todo("buy shopping")
    todo3 = Todo("do homework")
    
    todo_list = TodoList()
    todo_list.add(todo1)
    todo_list.add(todo2)
    todo_list.add(todo3)
    todo_list.give_up()
    for todo in todo_list.todo_list:
        assert todo.complete == True
