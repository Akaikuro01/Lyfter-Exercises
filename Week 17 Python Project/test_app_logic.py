import pytest
from datetime import datetime
from app_logic import AppManager  # Replace with your actual filename
import Logic

@pytest.fixture
def app():
    return AppManager()

# Test update_balance (Income)
def test_update_balance_income(app):
    result = app.update_balance(1000, 500, True)  # Income
    assert result == 1500

# Test update_balance (Expense)
def test_update_balance_expense(app):
    result = app.update_balance(1000, 300, False)  # Expense
    assert result == 700

# Test get_new_amount
def test_get_new_amount(app):
    entries = [["Income", "01-01-2025", "Salary", "Salary", "2000.5"]]
    assert app.get_new_amount(entries) == 2000.5

# Test check_date_format (valid)
def test_check_date_format_valid(app):
    assert app.check_date_format("05-08-2025") is True

# Test check_date_format (invalid)
def test_check_date_format_invalid(app):
    assert app.check_date_format("2025/08/05") is False

# Test filter_data_dates
def test_filter_data_dates(app):
    start = datetime.strptime("01-08-2025", "%d-%m-%Y").date()
    end = datetime.strptime("10-08-2025", "%d-%m-%Y").date()
    entries = [["Income", "05-08-2025", "Salary", "Salary", "2000"]]
    result = app.filter_data_dates(start, end, entries)
    assert len(result) == 1
    assert result[0][2] == "Salary"

# Test check_amount_is_number
def test_check_amount_is_number(app):
    assert app.check_amount_is_number("1500.5") is True
    assert app.check_amount_is_number("abc") is False

# Test color_rows
def test_color_rows(app):
    all_entries = [
        ["Income", "01-08-2025", "Salary", "Salary", "2000"],
        ["Expense", "02-08-2025", "Gas", "Car", "500"]
    ]
    all_categories = [
        ["Salary", "#FF0000"],
        ["Car", "#00FF00"]
    ]
    rows_colored = app.color_rows(all_entries, all_categories)
    assert (0, "white", "#FF0000") in rows_colored
    assert (1, "white", "#00FF00") in rows_colored
