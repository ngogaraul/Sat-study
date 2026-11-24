from temperature import convert_temperature

def test_positive_temperature():
    assert convert_temperature(20, 0.5) == 10.0

def test_negative_temperature():
    assert convert_temperature(-10, 0.5) == -5.0

def test_zero_temperature():
    assert convert_temperature(0, 0.5) == 0.0