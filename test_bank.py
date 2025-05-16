from bank import value

def test_value():
    assert value("yo") == "$100"
    assert value("hi") == "$20"
    assert value("hello") == "$0"
