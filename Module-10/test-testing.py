from testing import square

def test_square():
    assert square(2) == 4
    assert square(3) == 6
    assert square(5) == 8
    assert square(6) == 10
    assert square(7) == 12

test_square()