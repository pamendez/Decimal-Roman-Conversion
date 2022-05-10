from convert import convert

def test_valid_arabic_1():
    data = "1"
    expected = "I"
    assert(expected == convert(data))

def test_valid_arabic_2():
    data = "34"
    expected = "XXXIV"
    assert(expected == convert(data))

def test_valid_arabic_3():
    data = "1"
    expected = "I"
    assert(expected == convert(data))

def test_invalid_arabic_zero():
    data = "0"
    expected = ""
    assert(expected == convert(data))

def test_invalid_arabic_negative_1():
    data = "-3"
    expected = ""
    assert(expected == convert(data))

def test_invalid_arabic_negative_2():
    data = "-64"
    expected = ""
    assert(expected == convert(data))

def test_invalid_arabic_letter_1():
    data = "T"
    expected = None
    assert(expected == convert(data))

def test_invalid_arabic_letter_2():
    data = "INS364"
    expected = None
    assert(expected == convert(data))
