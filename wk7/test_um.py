from um import count
import pytest

def test_count():
    assert count("um") == 1
    assert count("um?") == 1
    assert count("Um") == 1
    assert count("UM...") == 1


def test_words_spaces():
    assert count("Type Um, thanks for the album.") == 1
    assert count("Hi, um, Cramer.") == 1
    assert count("Ummmmm! I'm telling") == 0


def test_multi_ums():
    assert count("Um, thanks, um...") == 2
    assert count("um, um, Dang! I can't remember...") == 2
    assert count("yum for my, um, tummy") == 1
