import pytest
from fuel import convert, gauge

def test_convert():
    assert convert("1/2") == 50
    assert convert("1/4") == 25
    assert convert("1/100") == 1


def test_value_error():
    with pytest.raises(ValueError):
        convert("100/10")

def test_zero_division_error():
     with pytest.raises(ZeroDivisionError):
      convert("1/0")


def test_gauge():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(2) == "2%"
    assert gauge(50) == "50%"
    assert gauge(98) == "98%"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
