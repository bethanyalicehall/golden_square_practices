from lib.counter import *

def test_counter_initializes_zero():
    counter = Counter()
    assert counter.count == 0

def test_counter_adds_number():
    counter = Counter()
    counter.add(5)
    assert counter.count == 5

def test_counter_report():
    counter = Counter()
    counter.add(10)
    counter.add(40)
    assert counter.report() == "Counted to 50 so far."

def test_counter_minus_numbers():
    counter = Counter()
    counter.add(10)
    counter.add(-5)
    assert counter.report() == "Counted to 5 so far."
