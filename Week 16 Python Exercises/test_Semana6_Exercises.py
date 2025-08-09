import Semana6_Exercises

# --------------------------
# Exercise 3 tests
# --------------------------
def test_sum_numbers_small_list():
    assert Semana6_Exercises.sum_numbers([1, 2, 3]) == 6

def test_sum_numbers_with_negatives():
    assert Semana6_Exercises.sum_numbers([-5, 10, -5]) == 0

def test_sum_numbers_empty_list():
    assert Semana6_Exercises.sum_numbers([]) == 0

# --------------------------
# Exercise 4 tests
# --------------------------
def test_print_backwards_simple(capfd):
    result = Semana6_Exercises.print_backwards("abc")
    out, _ = capfd.readouterr()
    assert out.strip().split("\n") == ["c", "b", "a"]
    assert result == "abc"

def test_print_backwards_single_letter(capfd):
    result = Semana6_Exercises.print_backwards("A")
    out, _ = capfd.readouterr()
    assert out.strip() == "A"
    assert result == "A"

def test_print_backwards_with_spaces(capfd):
    result = Semana6_Exercises.print_backwards("hi ")
    out, _ = capfd.readouterr()
    lines = out.split("\n")  
    assert lines[0] == " "   
    assert result == "hi "


# --------------------------
# Exercise 5 tests
# --------------------------
def test_count_lower_upper_simple(capfd):
    Semana6_Exercises.count_lower_upper_case_in_String("AbC")
    assert True

def test_count_lower_upper_all_lower(capfd):
    Semana6_Exercises.count_lower_upper_case_in_String("abc")
    assert True

def test_count_lower_upper_mixed(capfd):
    Semana6_Exercises.count_lower_upper_case_in_String("aBcDe")
    assert True

# --------------------------
# Exercise 6 Tests
# --------------------------
def test_order_string_basic(capfd):
    Semana6_Exercises.order_string_alphabetically("banana-apple-carrot")
    out, _ = capfd.readouterr()
    assert out.strip() == "apple-banana-carrot"

def test_order_string_two_words(capfd):
    Semana6_Exercises.order_string_alphabetically("pear-apple")
    out, _ = capfd.readouterr()
    assert out.strip() == "apple-pear"

def test_order_string_already_sorted(capfd):
    Semana6_Exercises.order_string_alphabetically("apple-banana")
    out, _ = capfd.readouterr()
    assert out.strip() == "apple-banana"

# --------------------------
# Exercise 7 tests choose prime numbers function
# --------------------------
def test_choose_prime_numbers_basic():
    assert Semana6_Exercises.choose_prime_numbers([2, 3, 4, 5]) == [2, 3, 5]

def test_choose_prime_numbers_with_non_primes():
    assert Semana6_Exercises.choose_prime_numbers([4, 6, 9, 11]) == [11]

def test_choose_prime_numbers_empty():
    assert Semana6_Exercises.choose_prime_numbers([]) == []

# --------------------------
# Exercise 7 tests Check prime numbers function
# --------------------------
def test_check_prime_two():
    assert Semana6_Exercises.check_prime_numbers(2) is True

def test_check_prime_five():
    assert Semana6_Exercises.check_prime_numbers(5) is True

def test_check_prime_four():
    assert Semana6_Exercises.check_prime_numbers(4) is False
