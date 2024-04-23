from lib.high_value import HighValue

def test_first_value_is_higher():
    value_first = 10
    value_second = 2
    self = HighValue(value_first, value_second )
    result = HighValue.get_highest(self)
    assert result == "First value is higher"

def test_second_value_is_higher():
    value_first = 2
    value_second = 10
    self = HighValue(value_first, value_second )
    result = HighValue.get_highest(self)
    assert result == "Second value is higher"

def test_values_are_equal():
    value_first = 10
    value_second = 10
    self = HighValue(value_first, value_second )
    result = HighValue.get_highest(self)
    assert result == "Values are equal"

def test_add_first_value():
    value_first = 10
    value_second = 2
    selection = "first"
    increase_by = 5
    self = HighValue(value_first, value_second)
    HighValue.add(self, increase_by, selection)
    assert self.value_first == 15

def test_add_second_value():
    value_first = 10
    value_second = 2
    selection = "second"
    increase_by = 5
    self = HighValue(value_first, value_second)
    HighValue.add(self, increase_by, selection)
    assert self.value_second == 7
