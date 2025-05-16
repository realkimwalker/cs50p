from bank import value
import pytest


def test_value():
    assert value("yo") == 100
    assert value("hi") == 20
    assert value("hello") == 0

def test_caps():
    assert value("YO") == 100
    assert value("HELLO") == 0
    assert value("HI") == 20


def test_phrase():
    assert value("yo, David") == 100
    assert value("hi, David") == 20
    assert value("hello, Kramer") == 0
