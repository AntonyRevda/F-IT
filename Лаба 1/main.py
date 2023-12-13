# TODO Написать 3 класса с документацией и аннотацией типов
import doctest
class Smartphone():
    def __init__(self, manufacturer: str, year_of_manufacture: int):

        """
        Создание и подготовка к работе объекта "Смартфон"

        :param manufacturer: Производитель
        :param year_of_manufacture: В каком году произведён

        Примеры:
        >>> smartphone = Smartphone('Samsung', 2020)  # инициализация экземпляра класса
        """

        if not isinstance(manufacturer, str):
            raise TypeError("Производитель должен быть типа str")
        self.manufacturer = manufacturer

        if not isinstance(year_of_manufacture, int):
            raise TypeError("Год производства должен быть типа int")
        if year_of_manufacture < 1990:
            raise ValueError("Год производства должен быть позже 1990 года")
        self.year_of_manufacture = year_of_manufacture


    def operation_system(self) -> None:
        """
        Функция проверяет, какая операционная система используется.
        :return: Операционная система

        Примеры:
        >>> smartphone.operation_system()
        """
        if smartphone.manufacturer == 'iPhone':
            return 'IOS'
        else:
            return 'Android'
        ...
    def novelty(self) -> None:
        """
        Функция проверяет, является телефон старым или новым.
        :return: Новизна телефона

        Примеры:
        >>> smartphone.novelty()
        """
        if smartphone.novelty <= 2020:
            return 'Old'
        else:
            return 'New'
        ...

class Pet():
    def __init__(self, name: str, age: int, species: str):
        """
        Создание и подготовка к работе объекта "Питомец"

        :param name: Имя питомца
        :param age: Возраст питомца
        :param species: Биологический вид

        Примеры:
        >>> puppy = Pet('Тузик', 5, 'Собака')  # инициализация экземпляра класса
        """

        if not isinstance(name, str):
            raise TypeError("Имя питомца должно быть типа str")
        self.name = name

        if not isinstance(age, int):
            raise TypeError("Возраст питомца должен быть типа int")
        if age < 0 or age > 20:
            raise ValueError("Питомцы столько не живут")
        self.age = age

        if not isinstance(name, str):
            raise TypeError("Вид питомца должен быть типа str")
        self.species = species

    def cuteness(self) -> None:
        """
        Функция проверяет, является ли питомец милашкой.
        :return: Миловидность

        Примеры:
        >>> puppy.cuteness()
        """
        if puppy.age <= 1:
            return 'Милашка'
        else:
            return 'Уже взрослый'

    def sound(self) -> None:
        """
        Функция проверяет, как питомец напоминает о себе.
        :return: Звук

        Примеры:
        >>> puppy.sound()
        """
        if puppy.species == 'Собака':
            return 'Гав'
        elif puppy.species == 'Кошка':
            return 'Мяу'
        else:
            return 'Sound'
        ...

class Book:
    def __init__(self, page_volume: float, words_volume: float):
        """
        Создание и подготовка к работе объекта "Книга"

        :param page_volume: Обьем листов
        :param words_volume: Обьем слов
        oбщее количество страниц  в книге 500
        общее количество слов в книге 300900080
        Примеры:
        >>>book = Book(500, 0)  # инициализация экземпляра класса
        """

        if not isinstance(page_volume, (int, float)):
           raise TypeError("Объем листов должен быть типа int или float")
        if page_volume <= 500:
           raise ValueError("Обьем листов должен быть положительным числом")
        self.page_volume = page_volume

        if not isinstance(words_volume, (int, float)):
         raise TypeError("Количество слов должно быть int или float")
        if words_volume < 300900080:
         raise ValueError("Количество слов не может быть отрицательным числом")
        self.words_volume = words_volume

   def is_empty_book(self) -> bool:
       """
      Функция которая проверяет является ли книга целой

      :return: Является   ли    книга  целой

      Примеры:
       >>> book = Book(500, 0)
       >>> book.is_empty_book()
       """
       ...
   def add_pages_to_book(self, pages: float) -> None:
       """
       Добавление  страниц   в   книгу.

       :param pages: Количество добавленных страниц

       :raise ValueError: Если количество страниц книги  превышает свободное место в книге, то вызываем ошибку

       Примеры:
       >>> book = Book(500, 0)
       >>> book.add_pages_to_book(200)
       """
       if not isinstance(pages, (int, float)):
           raise TypeError("Добавляемые страницы должны быть типа int или float")
       if pages < 0:
           raise ValueError("Добавляемые страницы должны положительным числом")
        ...



if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()  # тестирование примеров, которые находятся в документации