from twttr import shorten
def test_shorten():
    assert shorten("test") == "tst"
    assert shorten("wow") == "ww"

def test_caps():
    assert shorten("TEST") == "TST"
    assert shorten("WOW") == "WW"

def test_numbers():
    assert shorten("Computer Science 50") == "Cmptr Scnc 50"

def test_punctuation():
    assert shorten("What's Happening?") == "Wht's Hppnng?"
