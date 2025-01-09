class Toy:
    """
    Базовый класс для игрушек.

    Атрибуты:
        - name: название игрушки
        - age: рекомендуемый возраст для игры с игрушкой
         - in_stock: True если игрушка есть в наличии, False если нет
    """

    def __init__(self, name: str, age: int, in_stock: bool = True) -> None:
        """
        Инициализирует игрушку с названием и рекомендуемым возрастом.

        :param name: название игрушки
        :param age: рекомендуемый возраст для игры с игрушкой
        :param in_stock: True если игрушка есть в наличии, False если нет
        """
        self.name = name
        self.age = age
        self.in_stock = in_stock

    def __str__(self) -> str:
        """
        Возвращает строковое представление игрушки.

        :return: строка с информацией об игрушке
        """
        return f"{self.name}, для детей от {self.age} лет."

    def __repr__(self) -> str:
        """
        Возвращает официальное строковое представление игрушки.

        :return: строка, которая может быть использована для создания нового объекта
        """
        return f"Toy(name='{self.name}', age={self.age}, in_stock={self.in_stock})"

    def play(self) -> str:
        """
        Метод для игры с игрушкой.

        Причина перегрузки в дочерних классах: каждая игрушка имеет свои особенности при игре.

        :return: строка с информацией о том, как играть с игрушкой
        """
        return f"Играй с игрушкой {self.name}!"

    def availability(self) -> str:
        """
        Возвращает информацию о наличии игрушки.

        :return: строка с информацией о наличии игрушки
        """
        if self.in_stock:
            return f"Игрушка '{self.name}' в наличии."
        else:
            return f"Игрушки '{self.name}' нет в наличии."


class Doll(Toy):
    """
    Класс для куклы.

    Атрибуты:
        - name: название игрушки (куклы)
        - age: рекомендуемый возраст для игры
        - accessories: наличие аксессуаров для куклы
    """

    def __init__(self, name: str, age: int, accessories: bool = True, in_stock: bool = True) -> None:
        super().__init__(name, age, in_stock)
        self.accessories = accessories

    def __str__(self) -> str:
        """
        Возвращает строковое представление куклы.

        :return: строка с информацией о кукле
        """
        return f"{self.name} - кукла, для детей от {self.age} лет, аксессуары {'идут в комплекте' if self.accessories else 'не идут в комплекте'}"

    def __repr__(self) -> str:
        """
        Возвращает официальное строковое представление куклы.

        :return: строка, которая может быть использована для создания нового объекта
        """
        return f"Doll(name='{self.name}', age={self.age}, accessories={self.accessories}, in_stock={self.in_stock}))"

    def play(self) -> str:
        """
        Перегруженный метод для игры с куклой.

        :return: строка с информацией о том, как играть с куклой
        """
        return f"Играй с куклой {self.name}, примеряй ей наряды и делай неповторимые прически!"


class Lego(Toy):
    """
    Класс для конструктора Lego.

    Атрибуты:
        - name: название игрушки (конструктор)
        - age: рекомендуемый возраст для игры
        - pieces_count: количество деталей в наборе
    """

    def __init__(self, name: str, age: int, pieces_count: int, in_stock: bool = True) -> None:
        super().__init__(name, age, in_stock)
        self.pieces_count = pieces_count

    def __str__(self) -> str:
        """
        Возвращает строковое представление конструктора Lego.

        :return: строка с информацией о конструкторе Lego
        """
        return f"{self.name} - конструктор, для детей от {self.age} лет, {self.pieces_count} деталей"

    def __repr__(self) -> str:
        """
        Возвращает официальное строковое представление конструктора Lego.

        :return: строка, которая может быть использована для создания нового объекта
        """
        return f"Lego(name='{self.name}', age={self.age}, pieces_count={self.pieces_count}, in_stock={self.in_stock})"

    def play(self) -> str:
        """
        Перегруженный метод для игры с конструктором Lego.

        :return: строка с информацией о том, как играть с конструктором Lego
        """
        return f"Играй с конструктором {self.name}, собирай различные модели и развивай свою фантазию!"


# Пример использования метода availability
doll = Doll("Анабель", 5, accessories=False)
print(doll.availability())  # Вывод: Игрушка 'Анабель' в наличии.
doll = Doll("Барби", 8, accessories=True, in_stock=False)
print(doll.availability())  # Вывод: Игрушки 'Барби' нет в наличии.
