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
def test_calculate_total_price(my_class):
    assert my_class.calculate_total_price() == 10000.0

def test_apply_discount(discounted_item):
   assert discounted_item.price == 2500.0


@pytest.fixture
def item():
  return Item('Телефон', 10000, 5)

def test_name_getter(item):
  item.__name = 'Телефон'
  assert item.name == 'Телефон'


def test_name_setter_valid(item):
  item.name = 'Смартфон'
  assert item.name == 'Смартфон'

def test_name_setter_long(item):
  item.name = 'СуперСмартфон'
  assert item.name == 'СуперСмарт'

@pytest.fixture
def init_items():
  Item.instantiate_from_csv('C:/Users/79107/PycharmProjects/electronics-shop-project/src/items.csv')

def test_load_from_real_file(init_items):
  assert len(Item.all) == 5

def test_index_from_real_file(init_items):
    item1 = Item.all[1]
    assert item1.name == 'Ноутбук'

def test_string_to_int():
    assert Item.string_to_number('5') == 5


def test_string_to_float_whole():
    assert Item.string_to_number('5.0') == 5


def test_string_to_float_round():
    assert Item.string_to_number('5.5') == 5