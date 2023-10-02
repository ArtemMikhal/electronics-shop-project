import csv
class Item:
    """
    Класс для представления товара в магазине.
    """
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
    def instantiate_from_csv(cls, filename):
        """
        Инициализирует экземпляры класса
        Item данными из файла src / items.csv
        """
        with open(filename, encoding='windows-1251') as f:
            reader = csv.DictReader(f)
            for row in reader:
                name = row['name']
                price = float(row['price'])
                quantity = int(row['quantity'])
                item = cls(name, price, quantity)
                cls.all.append(item)


    @staticmethod
    def string_to_number(value):
        """Возвращает целое число из числа-строки"""
        try:
            number = float(value)
        except ValueError:
            return int(value)

        return int(number)