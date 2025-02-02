import doctest


class Coworking:
    def __init__(self, name: str, capacity: int):
        """
        Инициализирует коворкинг.

        :param name: Название коворкинга
        :param capacity: Вместимость коворкинга (количество человек)

        Примеры:
        >>> coworking = Coworking("Просто", 50)
        """
        if not isinstance(name, str):
            raise TypeError("Название коворкинга должно быть типа str")

        if not isinstance(capacity, int):
            raise TypeError("Вместимость коворкинга должна быть типа int")
        if capacity <= 0:
            raise ValueError("Вместимость коворкинга должна быть больше 0")

        self.name = name
        self.capacity = capacity

    def is_full(self, current_occupants: int) -> bool:
        """
        Проверяет, заполнен ли коворкинг.

        :param current_occupants: Текущее количество человек в коворкинге
        :return: True, если коворкинг заполнен, иначе False
        :raise ValueError: Если текущее количество человек больше вместимости

        >>> coworking = Coworking("Просто", 50)
        >>> coworking.is_full(50)
        True
        >>> coworking.is_full(30)
        False
        """
        if not isinstance(current_occupants, int):
            raise TypeError("Количество человек в коворкинге должно быть типа int")
        if current_occupants < 0:
            raise ValueError("Количество человек в коворкинге должно быть положительным числом")
        if current_occupants > self.capacity:
            raise ValueError("Количество человек превышает вместимость коворкинга")
        return current_occupants == self.capacity

    def describe(self) -> str:
        """
        Возвращает описание коворкинга.

        :return: Описание коворкинга

        >>> coworking = Coworking("Просто", 50)
        >>> coworking.describe()
        'Коворкинг Просто вмещает 50 человек.'
        """
        return f"Коворкинг {self.name} вмещает {self.capacity} человек."


class Boat:
    def __init__(self, name: str, max_speed: float, capacity: int):
        """
        Инициализирует лодку.

        :param name: Название лодки
        :param max_speed: Максимальная скорость лодки в км/ч
        :param capacity: Вместимость лодки (количество человек)

        Примеры:
        >>> boat = Boat("Чижик", 20.0, 4)
        """

        if not isinstance(name, str):
            raise TypeError("Название лодки должно быть типа str")

        if not isinstance(max_speed, (int, float)):
            raise TypeError("Максимальная скорость лодки должна быть типа int или float")
        if max_speed <= 0:
            raise ValueError("Максимальная скорость должна быть больше 0")

        if not isinstance(capacity, int):
            raise TypeError("Вместимость лодки должна быть типа int")
        if capacity <= 0:
            raise ValueError("Вместимость лодки должна быть больше 0")

        self.name = name
        self.max_speed = max_speed
        self.capacity = capacity

    def set_speed(self, speed: float) -> None:
        """
        Устанавливает скорость лодки.

        :param speed: Новая скорость лодки
        :raise ValueError: Если скорость меньше или равна 0

        >>> boat = Boat("Чижик", 20.0, 4)
        >>> boat.set_speed(25.0)
        >>> boat.max_speed
        25.0
        """
        if not isinstance(speed, (int, float)):
            raise TypeError("Скорость лодки должна быть типа int или float")
        if speed <= 0:
            raise ValueError("Скорость должна быть больше 0")
        self.max_speed = speed

    def distance(self, hours: int = 1) -> float:
        """
        Рассчитывает расстояние, которое лодка проплывет за заданное количество часов.

        :param hours: Время в часах. По умолчанию 1
        :return: Расстояние в километрах

        >>> boat = Boat("Чижик", 30.0, 4)
        >>> boat.distance(2)
        60.0
        >>> boat.distance()
        30.0
        """
        if not isinstance(hours, int):
            raise TypeError("Время должно быть типа int")
        if hours < 0:
            raise ValueError("Время не может быть отрицательным числом")
        return self.max_speed * hours


class Puzzle:
    def __init__(self, title: str, pieces: int):
        """
        Инициализирует объект пазла.

        :param title: Название пазла
        :param pieces: Количество кусочков

        Примеры:
        >>> puzzle = Puzzle("Котята в корзинке", 300)
        """
        if not isinstance(title, str):
            raise TypeError("Название пазла должно быть типа str")

        if not isinstance(pieces, int):
            raise TypeError("Количество кусочков должно быть типа int")
        if pieces <= 0:
            raise ValueError("Количество кусочков должно быть положительным числом")
        self.title = title
        self.pieces = pieces

    def is_completed(self, assembled_pieces: int) -> bool:
        """
        Проверяет, собран ли пазл.

        :param assembled_pieces: Количество собранных кусочков
        :return: True, если пазл собран, иначе False
        :raise ValueError: Если количество собранных кусочков больше общего количества

        >>> puzzle = Puzzle("Котята в корзинке", 300)
        >>> puzzle.is_completed(300)
        True
        >>> puzzle.is_completed(240)
        False
        >>> puzzle.is_completed(500)
        Traceback (most recent call last):
            ...
        ValueError: Количество собранных кусочков не может превышать общее количество
        """
        if not isinstance(assembled_pieces, int):
            raise TypeError("Количество собранных кусочков должно быть типа int")
        if assembled_pieces > self.pieces:
            raise ValueError("Количество собранных кусочков не может превышать общее количество")
        return assembled_pieces == self.pieces

    def get_puzzle_info(self) -> str:
        """
        Возвращает информацию о пазле.

        return: Строка, содержащая информацию о пазле

        >>> puzzle = Puzzle("Котята в корзинке", 300)
        >>> puzzle.get_puzzle_info()
        'Пазл: Котята в корзинке, Количество кусочков: 300'
        """
        return f"Пазл: {self.title}, Количество кусочков: {self.pieces}"

    def get_progress(self, assembled_pieces: int = 0) -> float:
        """
        Возвращает процент собранности пазла.

        :param assembled_pieces: Количество собранных кусочков. По умолчанию 0
        :raise ValueError: Если количество собранных кусочков отрицательное
        :raise ValueError: Если количество собранных кусочков превышает количество кусочков в пазле

        return: Процент собранности пазла
        """
        if not isinstance(assembled_pieces, int):
            raise TypeError("Количество собранных кусочков должно быть типа int")
        if assembled_pieces < 0:
            raise ValueError("Количество собранных кусочков должно быть неотрицательным числом")
        if assembled_pieces > self.pieces:
            raise ValueError("Количество собранных кусочков превышает количество кусочков в пазле")
        return assembled_pieces / self.pieces * 100


if __name__ == "__main__":
    doctest.testmod()
