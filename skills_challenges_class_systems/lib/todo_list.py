
class TodoList:
    def __init__(self):
        self._tasks = []

    def add(self, todo):
        self._tasks.append(todo)
        # Parameters:
        #   todo: an instance of Todo
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the todo to the list of todos
        

    def incomplete(self):
        return [task for task in self._tasks if not task.complete]
    

    def complete(self):
        return [task for task in self._tasks if task.complete]


    def give_up(self):
        for task in self._tasks:
            task.mark_complete()



