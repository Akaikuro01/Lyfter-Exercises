import Semana16_Extra1

# --------------------------
# Sum tests
# --------------------------
def test_sum_with_positive_numbers():
    a = 5
    b = 3000
    result = Semana16_Extra1.add_numbers(a, b)
    assert result == 3005


def test_sum_with_negative_numbers():
    a = -5
    b = -3000
    result = Semana16_Extra1.add_numbers(a, b)
    assert result == -3005


def test_sum_with_zeroes():
    a = 0
    b = 0
    result = Semana16_Extra1.add_numbers(a, b)
    assert result == 0


# --------------------------
# Average tests
# --------------------------
def test_average_with_positive_numbers():
    numbers = [25, 25, 25]
    result = Semana16_Extra1.average(numbers)
    assert result == 25


def test_average_with_negative_numbers():
    numbers = [-25, -25, -25]
    result = Semana16_Extra1.average(numbers)
    assert result == -25


def test_average_with_zeroes():
    numbers = [0, 0, 0]
    result = Semana16_Extra1.average(numbers)
    assert result == 0


# --------------------------s
# Convertion tests
# --------------------------
def test_celsius_to_fahrenheit_with_positive_numbers():
    celsius = 100
    result = Semana16_Extra1.celsius_to_fahrenheit(celsius)
    assert result == 212  

def test_celsius_to_fahrenheit_with_negative_numbers():
    celsius = -40
    result = Semana16_Extra1.celsius_to_fahrenheit(celsius)
    assert result == -40  

def test_celsius_to_fahrenheit_with_zeroes():
    celsius = 0
    result = Semana16_Extra1.celsius_to_fahrenheit(celsius)
    assert result == 32  