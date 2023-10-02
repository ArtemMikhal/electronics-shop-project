import pytest

from src.keyboard import Keyboard, MixinChange


@pytest.fixture
def testing_class_3():
    """Объект класса для теста"""
    return Keyboard('Dark Project KD87A', 9600, 5)


def test_change_lang(testing_class_3):
    """Тесты для проверки переключения раскладки клавиатуры"""
    assert str(testing_class_3.language) == "EN"
    testing_class_3.change_lang()
    assert str(testing_class_3.language) == "RU"
    # Сделали EN -> RU -> EN
    testing_class_3.change_lang()
    assert str(testing_class_3.language) == "EN"


def test_change_lang_2(testing_class_3):
    """Тесты для проверки переключения раскладки клавиатуры с неизвестным вводом"""
    with pytest.raises(AttributeError) as excpt:
        testing_class_3.language = 'CH'
    assert str(excpt.value) == "property 'language' of 'Keyboard' object has no setter"

