from lib.string_builder import *

'''
The initial output is an empty string
'''
def test_string_builder_initialize():
    string_builder = StringBuilder()
    assert string_builder.size() == 0
    assert string_builder.output() == ""

'''
When a single string is added
the output is that string
'''
def test_string_builder_adds_string():
    string_builder = StringBuilder()
    string_builder.add("Horse")
    assert string_builder.output() == "Horse"

'''
When a single string is added
the size reflects the size of the added string
'''
def test_string_builder_sizes_string():
    string_builder = StringBuilder()
    string_builder.add("Horse")
    assert string_builder.size() == 5


'''
When multiple strings are added
the output is the combination of those strings
'''
def test_string_builder_adds_multiple():
    string_builder = StringBuilder()
    string_builder.add("Horse")
    string_builder.add(" and ")
    string_builder.add("carriage")
    assert string_builder.output() == "Horse and carriage"

'''
When multiple strings are added
the size reflects the combination of those strings
'''
def test_string_builder_sizes_multiple_strings():
    string_builder = StringBuilder()
    string_builder.add("Horse")
    string_builder.add(" and ")
    string_builder.add("carriage")
    assert string_builder.size() == 18

