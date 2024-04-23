from lib.string_builder import *

def test_string_builder_initialize():
    string_builder = StringBuilder()
    assert string_builder.size() == 0
    assert string_builder.output() == ""

def test_string_builder_adds_strings():
    string_builder = StringBuilder()
    string_builder.add("Horse")
    assert string_builder.size() == 5
    assert string_builder.output() == "Horse"

def test_string_builder_adds_multiple():
    string_builder = StringBuilder()
    string_builder.add("Horse")
    string_builder.add(" and ")
    string_builder.add("carriage")
    assert string_builder.size() == 18
    assert string_builder.output() == "Horse and carriage"


