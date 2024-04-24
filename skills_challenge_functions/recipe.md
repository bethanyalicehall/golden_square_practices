
One
## 1. Describe the Problem
_Put or write the user story here. Add any clarifying notes you might have._

As a user
So that I can manage my time
I want to see an estimate of reading time for a text, assuming that I can read 200 words a minute.

## 2. Design the Function Signature
_Include the name of the function, its parameters, return value, and side effects._
```python
def calculates_reading_time_of_text(text):
    '''Calculates reading time of a text

    Parameters:
        text: a string containing words
    
    Returns:
        the average reading time for a text, as a float to one decimal place

    Side effects:
        This function doesn't have any side effects
    
    '''
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python

'''
Given a text message with 10 words
It returns 3 seconds
'''

test_calculates_reading_time_of_text('One two three four five six seven eight nine ten') => "3 seconds"

"""
Given an empty string
It returns none
"""
test_calculates_reading_time_of_text("") => "0 seconds"

"""
Given a None value
It throws an error
"""
test_calculates_reading_time_of_text(None) throws an error
```


_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._


--------------------------------------------------------------------------

Two
## 1. Describe the Problem
As a user
So that I can improve my grammar
I want to verify that a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark.

## 2. Design the Function Signature
_Include the name of the function, its parameters, return value, and side effects._
```python
def capitalizes_and_adds_full_stop(text, question):
    '''Ensures the text starts with a capital letter and end with a full stop

    Parameters:
        text: a string containing words
        question: a boolean
    
    Returns:
        a new string, containing the capitalized initial text with a full stop or a question mark if question == True

    Side effects:
        This function doesn't have any side effects
    
    '''
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python

'''
Given a text where question = False
it returns a 
capitalized text with a full stop
at the end.
'''

test_capitalizes_and_adds_full_stop("i am happy") => "I am happy."

"""
Given a text where question = True
it returns a capitalized
text with a question mark at the end.
"""
test_calculates_reading_time_of_text("how are you") => "How are you?"


```


_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._


