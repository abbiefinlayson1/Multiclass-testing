class TodoList:
    def __init__(self):
        self.todo_list = []


    def add(self, todo):
        self.todo_list.append(todo)

    def incomplete(self):
        incomplete_list = []
        for todo in self.todo_list:
            if not todo.complete:
                incomplete_list.append(todo)
        return incomplete_list

    def complete(self):
        self.complete_list = []
        for todo in self.todo_list:
            if todo.complete:
                self.complete_list.append(todo)
        return self.complete_list
    

    def give_up(self):
        for todo in self.todo_list:
            todo.mark_complete()