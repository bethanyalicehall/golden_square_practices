from lib.gratitudes import *


'''
Initializes an empty
list
'''
def test_gratitudes_empty_list():
    gratitudes = Gratitudes()
    assert gratitudes.gratitudes == []

'''
When a gratitude is added
it is added to the list
'''
def test_add_gratitude():
    gratitudes = Gratitudes()
    gratitudes.add("good health")
    assert gratitudes.gratitudes == ["good health"]

'''
When multiple gratitudes are added
they are added to the formatted output
'''
def test_format_gratitude():
    gratitudes = Gratitudes()
    gratitudes.add("good health")
    gratitudes.add("good friends")
    assert gratitudes.format() == "Be grateful for: good health, good friends"


