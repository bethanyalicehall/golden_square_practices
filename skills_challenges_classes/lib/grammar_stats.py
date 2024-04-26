class GrammarStats:
    def __init__(self):
        self.passed_count = 0
        self.total_count = 0

    def check(self, text):
        if text[0].isupper() and text[-1] in [".", "!", "?"]:
            self.passed_count += 1  # Increment passed count if text passes the check
            self.total_count += 1  # Increment total count for each text checked
            return True
        else: 
            self.total_count += 1  # Increment total count for each text checked
            return False
    

    def percentage_good(self):
        if self.total_count == 0:
            return 0  # Handle case when no texts have been entered
        else:
            return (self.passed_count / self.total_count) * 100  # Calculate percentage

        



        