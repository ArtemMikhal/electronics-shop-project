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
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)
    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
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
        objects = []

        with open(filename) as f:
            reader = csv.reader(f)

            for row in reader:
                name = row[0]
                price = float(row[1])
                quantity = int(row[2])

                item = Item(name, price, quantity)

                if item not in objects:
                    objects.append(item)
                    cls.all.append(item)

        return objects
    @classmethod
    def instantiate_from_csv(cls, filename):
        """Инициализирует экземпляры класса Item данными из файла src / items.csv"""
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
        """ Возвращающает число из числа-строки"""
        try:
            return float(value)
        except ValueError:
            return int(value)