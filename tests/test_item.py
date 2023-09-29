"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item


@pytest.fixture
def my_class():
    """Фикстурный метод my_class используется для создания экземпляра класса Item."""
    return Item("Планшет", 5000, 2)


@pytest.fixture
def discounted_item(my_class):
    """Фикстурный метод применяет скидку к экземпляру класса 'my_class'."""
    my_class.pay_rate = 0.5
    my_class.apply_discount()
    return my_class


@pytest.fixture
def item():
    """Фикстурный метод создает экземпляр класса с заданными параметрами."""
    return Item('Телефон', 10000, 5)


@pytest.fixture
def init_items():
    """Возвращает инициализированные объекты"""
    Item.instantiate_from_csv('C:/Users/79107/PycharmProjects/electronics-shop-project/src/items.csv')


def test_create_item(my_class):
    """Проверяет, что значения атрибутов 'name', 'price' и 'quantity' соответствуют ожидаемым."""
    assert my_class.name == "Планшет"
    assert my_class.price == 5000
    assert my_class.quantity == 2


def test_calculate_total_price(my_class):
    """Проверяет, что метод 'calculate_total_price()' рассчитывает общую стоимость."""
    assert my_class.calculate_total_price() == 10000.0


def test_apply_discount(discounted_item):
    """Проверяет, что метод 'apply_discount' применяет установленную скидку для конкретного товара."""
    assert discounted_item.price == 2500.0


def test_name_getter(item):
    """Проверяет корректность работы геттера 'name'."""
    item.__name = 'Телефон'
    assert item.name == 'Телефон'


def test_name_setter_valid(item):
    """Проверяет корректность работы сеттера 'name'."""
    item.name = 'Смартфон'
    assert item.name == 'Смартфон'


def test_name_setter_long(item):
    """Проверяет корректность сокращения наименования до 10 симфолов."""
    item.name = 'СуперСмартфон'
    assert item.name == 'СуперСмарт'


def test_load_from_real_file(init_items):
    """Проверяет, что после инициализации объектов их количество равно верному значению"""
    assert len(Item.all) == 5


def test_index_from_real_file(init_items):
    """Проверяет, что объект с указанным индексом имеет ожидаемое значение."""
    item1 = Item.all[1]
    assert item1.name == 'Ноутбук'


def test_string_to_int():
    """Проверяет корректность преобразования строки в int."""
    assert Item.string_to_number('5') == 5


def test_string_to_float_whole():
    """Проверяет корректность преобразования float в int"""
    assert Item.string_to_number('5.0') == 5


def test_string_to_float_round():
    """Проверяет округление до целого числа"""
    assert Item.string_to_number('5.5') == 5


def test_repl_in_item(item):
    """
    Тест проверяет, что специальный метод __repl__ возвращает ожидаемый результат
    """
    assert repr(item) == "Item('Телефон', 10000, 5)"


def test_str_in_item(item):
    """
    Тест проверяет, что специальный  метод __str__ возвращает ожидаемый результат
    """
    assert str(item) == 'Телефон'


def test_add_operator(item):
    """Проверяет невозможность сложения с другими объектами"""
    with pytest.raises(TypeError) as excpt:
        result = item + 5
        result_2 = item + 'test'
    assert str(excpt.value) == 'Нельзя сложить Phone или Item с экземплярами не Phone или Item классов.'