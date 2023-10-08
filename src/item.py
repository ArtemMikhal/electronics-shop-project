import csv
import os
CSV_FILE = os.path.join('..', 'src', 'items.csv')
class Item:
    """
    Класс для представления товара в магазине.
    """
    CSV_FILE = os.path.join('..', 'src', 'items.csv') # Путь к файлу .csv
    pay_rate = 1.0
    all = []


    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        super().__init__()
        self.__name = name
        self.price = price
        self.quantity = quantity


    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {(self.price)}, {self.quantity})"


    def __str__(self):
        return self.__name

    def __add__(self, other):
        if isinstance(other, Item):
            return self.quantity + other.quantity
        else:
            raise TypeError("Нельзя сложить Phone или Item с экземплярами не Phone или Item классов.")

    def calculate_total_price(self) -> float:
        """Рассчитывает общую стоимость конкретного товара в магазине."""
        return self.quantity * self.price


    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * self.pay_rate


    @property
    def name(self):
        """Возвращает наименование."""
        return self.__name


    @name.setter
    def name(self, name):
        """
        Проверяет, что длина наименования товара не больше 10 симвовов.
        В противном случае, обрезает строку (оставляет первые 10 символов)
        """
        if len(name) > 10:
            name = name[:10]
        self.__name = name


    @classmethod
    def instantiate_from_csv(cls):
        try:
            with open(cls.CSV_FILE, encoding='cp1251') as csvfile:
                reader = csv.DictReader(csvfile)
                if reader.fieldnames != ['name', 'price', 'quantity']:
                    raise InstantiateCSVError
                cls.all.clear()
                for row in reader:
                    if any(value is None for value in row.values()):
                        raise InstantiateCSVError
                    cls(row['name'], float(row['price']), int(row['quantity']))
        except FileNotFoundError:
            raise FileNotFoundError('Отсутствует файл item.csv')


    @staticmethod
    def string_to_number(value):
        """Возвращает целое число из числа-строки"""
        try:
            number = float(value)
        except ValueError:
            return int(value)

        return int(number)


class InstantiateCSVError(Exception):
    """
    Класс-исключение
    если файл `item.csv` поврежден (например, отсутствует одна из колонок данных)
    """
    def __init__(self, *args):
        self.message = args[0] if args else 'Файл item.csv поврежден'

    def __str__(self):
        return f'{self.message}'
