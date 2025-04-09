from shopping.shopping import calculate_total_with_tax
import pytest

def test_calculate_total_with_tax():
    items = [10.00, 5.00]
    total = calculate_total_with_tax(items)
    expected = 16.05  # 15.00 + 7% = 16.05
    print(expected, total)
    assert abs(total - expected) < 0.01
