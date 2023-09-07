"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item

@pytest.fixture
def my_class():
    return Item("Планшет", 5000, 2)

@pytest.fixture
def discounted_item(my_class):
    my_class.pay_rate = 0.5
    my_class.apply_discount()
    return my_class

def test_create_item(my_class):
    assert my_class.name == "Планшет"
    assert my_class.price == 5000
    assert my_class.quantity == 2
def tests_calculate_total_price(my_class):
    assert my_class.calculate_total_price() == 10000.0

def test_apply_discount(discounted_item):
   assert discounted_item.price == 2500.0