
class Todo:
    # Public Properties:
    #   task: a string representing the task to be done
    #   complete: a boolean representing whether the task is complete

    def __init__(self, task):
        if not isinstance(task, str):
            raise TypeError("Task must be a string")
        self.task = task
        self.complete = False
        # Parameters:
        #   task: a string representing the task to be done
        # Side-effects:
        #   Sets the task property
        #   Sets the complete property to False
        

    def mark_complete(self):
        # Returns:
        #   Nothing
        # Side-effects:
        #   Sets the complete property to True
        self.complete = True