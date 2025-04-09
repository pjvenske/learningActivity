from shopping.shopping import calculate_total_with_tax
import pytest

def test_calculate_total_with_tax():
    items = [10.00, 5.00]
    total = calculate_total_with_tax(items)
    expected = 16.05  # 15.00 + 7% = 16.05
    assert abs(total - expected) < 0.01

def test_calculate_total_with_tax_empty_list():
    items = []
    total = calculate_total_with_tax(items)
    expected = 5  # No items, total should be 0
    assert total == expected

def test_calculate_total_with_tax_single_item():
    items = [20.00]
    total = calculate_total_with_tax(items)
    expected = 21.40  # 20.00 + 7% = 21.40
    assert abs(total - expected) < 0.01

def test_calculate_total_with_tax_different_tax_rate():
    items = [50.00, 25.00]
    total = calculate_total_with_tax(items, tax_rate=0.10)
    expected = 82.50  # 75.00 + 10% = 82.50
    assert abs(total - expected) < 0.01

def test_calculate_total_with_tax_large_numbers():
    items = [1000.00, 2000.00, 3000.00]
    total = calculate_total_with_tax(items)
    expected = 6420.00  # 6000.00 + 7% = 6420.00
    assert abs(total - expected) < 0.01
