import pytest

from src.item import Item
from src.phone import Phone

@pytest.fixture
def testing_class():
    """Объект класса для теста"""
    return Phone("iPhone 14", 120_000, 5, 2)


@pytest.fixture
def testing_class_2():
    """Второй объект  класса для теста"""
    return Item("Смартфон", 10000, 20)


def test_str_method(testing_class):
    """Тестирует __str__ метод"""
    assert str(testing_class) == 'iPhone 14'


def test_repr_method(testing_class):
    """Тестирует __repr__ метод"""
    assert repr(testing_class) == "Phone('iPhone 14', 120000, 5, 2)"


def test_object_class_phone(testing_class):
    "Проверяет добавленный атрибут дочернего класса Phone"
    assert testing_class.number_of_sim == 2


def test_summing_objects(testing_class, testing_class_2):
    "Проверяет возможность сложения по количеству товара в магазине экземпляров класса Phone и Item "
    assert testing_class + testing_class_2 == 25
    assert testing_class + testing_class == 10


def test_verify_num_of_sim(testing_class):
    """Тест для проверки ввода некорректных значений"""
    with pytest.raises(ValueError) as excpt:
        testing_class.number_of_sim = 0
    assert str(excpt.value) == 'Количество физических SIM-карт должно быть целым числом больше нуля.'

    testing_class.number_of_sim = 1
    assert testing_class.number_of_sim == 1




