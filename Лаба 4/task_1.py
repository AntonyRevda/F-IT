if __name__ == "__main__":
    # Write your solution here
    class Animal:
        """Базовый класс для животных."""

        def __init__(self, name: str, age: int):
            """
            Конструктор класса Animal.

            Args:
                name (str): Имя животного.
                age (int): Возраст животного.
            """
            self.name = name
            self.age = age

        def make_sound(self) -> str:
            """
            Издать звук.

            Returns:
                str: Строка со звуком, который издает животное.
            """
            return "Некоторый звук"

        def eat(self, food: str) -> str:
            """
            Покушать.

            Args:
                food (str): Еда, которую животное съедает.

            Returns:
                str: Строка с сообщением о том, что животное ест.
            """
            return f"{self.name} eats {food}."

        def __str__(self) -> str:
            """
            Строковое представление объекта.

            Returns:
                str: Строка с информацией об объекте.
            """
            return f"{self.name} is {self.age} years old."

        def __repr__(self) -> str:
            """
            Представление объекта.

            Returns:
                str: Строка, представляющая объект.
            """
            return f"{self.__class__.__name__}: name='{self.name!r}', age={self.age}"


    class Dog(Animal):
        """Дочерний класс для собак."""

        def __init__(self, name: str, age: int, breed: str):
            """
            Конструктор класса Dog.

            Args:
                name (str): Имя собаки.
                age (int): Возраст собаки.
                breed (str): Порода собаки.
            """
            super().__init__(name, age)
            self.breed = breed

        def make_sound(self) -> str:
            """
            Издать звук.

            Returns:
                str: Строка с лаем собаки.
            """
            return "Гав-гав!"

        def fetch(self, item: str) -> str:
            """
            Апорт.

            Args:
                item (str): Предмет, который нужно принести.

            Returns:
                str: Строка с сообщением о том, что собака принесла предмет.
            """
            return f"{self.name} принес: {item}"

        def eat(self, food: str) -> str:
            """
            Покушать.

            Args:
                food (str): Еда, которую собака съедает.

            Returns:
                str: Строка с сообщением о том, что собака ест.
            """
            return super().eat(food)

        def __str__(self) -> str:
            """
            Строковое представление объекта.

            Returns:
                str: Строка с информацией об объекте.
            """
            return f"Dog named {super().__str__()}. It's breed is {self.breed}."

        def __repr__(self) -> str:
            """
            Представление объекта.

            Returns:
                str: Строка, представляющая объект.
            """
            return f"{super().__repr__()}, breed='{self.breed!r}'"


    class Cat(Animal):
        """Дочерний класс для кошек."""

        def __init__(self, name: str, age: int, color: str):
            """
            Конструктор класса Cat.

            Args:
                name (str): Имя кошки.
                age (int): Возраст кошки.
                color (str): Окрас кошки.
            """
            super().__init__(name, age)
            self.color = color

        def make_sound(self) -> str:
            """
            Издать звук.

            Returns:
                str: Строка с мяуканьем кошки.
            """
            return "Мяу!"

        def sleep(self) -> str:
            """
            Уйти спать.

            Returns:
                str: Сообщение о том, что кошка ушла спать.
            """
            return f"{self.name} ушла спать"

        def eat(self, food: str) -> str:
            """
            Покушать.

            Args:
                food (str): Еда, которую кошка съедает.

            Returns:
                str: Строка с сообщением о том, что кошка ест.
            """
            return super().eat(food)

        def __str__(self) -> str:
            """
            Строковое представление объекта.

            Returns:
                str: Строка с информацией об объекте.
            """
            return f"Cat named {super().__str__()}. It's color is {self.color}."

        def __repr__(self) -> str:
            """
            Представление объекта.

            Returns:
                str: Строка, представляющая объект.
            """
            return f"{super().__repr__()}, color='{self.color!r}'"
    pass
