from lib.counter import *

'''
Initializes a count of zero
'''
def test_counter_initializes_zero():
    counter = Counter()
    assert counter.report() == "Counted to 0 so far."

'''
Counter adds a single number
that is reflected in the final count
'''
def test_counter_adds_number():
    counter = Counter()
    counter.add(5)
    assert counter.report() == "Counted to 5 so far."

'''
Counter adds multiple numbers
and this is reflected in the final count
'''
def test_counter_report():
    counter = Counter()
    counter.add(10)
    counter.add(40)
    assert counter.report() == "Counted to 50 so far."

'''
Counter adds minus numbers
and this is reflected in the final count
'''
def test_counter_minus_numbers():
    counter = Counter()
    counter.add(10)
    counter.add(-5)
    assert counter.report() == "Counted to 5 so far."
