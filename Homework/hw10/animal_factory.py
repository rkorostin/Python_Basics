# -*- coding: utf-8 -*-

# Базовый класс
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass


# Dog - класс наследник
class Dog(Animal):
    def speak(self):
        return "growls"


# Cat - класс наследник
class Cat(Animal):
    def speak(self):
        return "purrs"


class AnimalFactory:
    @staticmethod
    def create_animal(animal_type, *args, **kwargs):
        # Проверяем переданный тип животного
        if animal_type == "Dog":
            # Если тип - собака, создаем экземпляр класса Dog с переданными параметрами
            return Dog(*args, **kwargs)
        elif animal_type == "Cat":
            # Если тип - кошка, создаем экземпляр класса Cat с переданными параметрами
            return Cat(*args, **kwargs)


# создаем экземпляр класса AnimalFactory
animal_factory = AnimalFactory()

# Используя метод create_animal() для создания экземпляров классов Dog -
# создаем собаку с именем "Rex"
# создаем кота с именем "Tom"
dog = animal_factory.create_animal("Dog", "Rex")
cat = animal_factory.create_animal("Cat", "Tom")

# Выводим имя и звук для собаки
print(dog.name)
print(dog.speak())

# Выводим имя и звук для кота
print(cat.name)
print(cat.speak())
