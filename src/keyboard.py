from src.item import Item

class MixinChange:
    """Класс-миксин по хранению и изменению раскладки клавиатуры"""
    en_lang = 'EN'
    ru_lang = 'RU'

    def __init__(self):
        """Инициализатор класса. Значение EN по умолчанию"""
        self.__language = self.en_lang

    @property
    def language(self):
        """Геттер для значения раскладки"""
        return self.__language

    def change_lang(self):
        """Метод для изменения языка раскладки клавиатуры"""
        if self.__language == self.en_lang:
            self.__language = self.ru_lang
            return self.__language
        else:
            self.__language = self.en_lang
            return self.__language


class Keyboard(Item, MixinChange):
    """Класс для товара клавиатура. Наследуется от двух классов Item и MixinLang"""
    pass





