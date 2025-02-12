from lib.todo import *
def test_todo_class():
    todo = Todo("task")

def test_mark_complete():
    todo = Todo("task")
    result = todo.mark_complete()
    assert result == True