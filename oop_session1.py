from django.db import models
from ast import Lambda
import os
os.system('cls'if os.name == 'nt' else 'clear')


# def print_type(data):
#     for i in data:
#         print(i, type(i))


# test = [123, 'Emin', [1, 2, 3], (1, 2, 3), {1, 2, 3}, True]
# print_type(test)


# class Person:
#     name = 'Emin'
#     age = 31


# person1 = Person()
# person2 = Person()

# print(person1.name)
# print(person2.name)

# Person.job = 'teacher'

# print(person1.job)

# # Class Attributes vs Instance attributes

# person1.location = 'Turkey'
# # print(person1.location)
# person2.name = 'Aaron'
# print(person2.name)
# print(person1.name)


# Self Keyword

# class Person:
#     name = 'Emin'
#     age = 31

#     def test(self):
#         print('test')

#     def set_details(self, name, age):
#         self.name = name
#         self.age = age

#     def get_details(self):
#         print(self.name, self.age)


# person1 = Person()
# person1.test()
# Person.test(person1)

# person1.get_details()
# person1.set_details('Aaron', 37)
# person1.get_details()


# static method

# class Person:
#     company = 'Clarusway'

#     def set_details(self, name, age):
#         self.name = name
#         self.age = age

#     def get_details(self):
#         print(self.name, self.age)

#     @staticmethod
#     def salute():
#         print('Hi there!')

# # print(Person.name)
# person1 = Person()
# person1.salute()

# special methods

# class Person:
#     company = 'Clarusway'

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __str__(self):
#         return f"{self.name} {self.age}"

#     def get_details(self):
#         print(self.name, self.age)


# person1 = Person('Emin', 31)
# person1.get_details()

# liste = [4, 2, 9, 11, 5]
# print(liste)
# print(person1)
# print(person1.__str__())

#encapsulation and abstraction

# class Person:
#     company = 'Clarusway'

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         self._id = 5000  # privatedir ve degisiklikte duzgun calismaz
#         self.__id2 = 4000  # buna erisilemez

#     def __str__(self):
#         return f"{self.name} {self.age}"

#     def get_details(self):
#         print(self.name, self.age)


# person1 = Person('Aaron', 37)
# print(person1._id)
# # print(person1.__id2)
# print(person1._Person__id2)  # bu sekilde yazarsak erisilebilir
# liste = [4, 2, 9, 11, 5]
# liste.sort()

# print(liste)


#inheritance and polymorphism

class Person:
    company = 'Clarusway'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} {self.age}"

    def get_details(self):
        print(self.name, self.age)


class Lang:
    def __init__(self, langs):
        self.langs = langs

    def display_langs(self):
        print(self.langs)


class Employee(Person, Lang):
    def __init__(self, name, age, path, langs):
        # self.name = name
        # self.age = age
        super().__init__(name, age)  # parentten bu sekilde age ve name i cekecegiz
        self.path = path
        # self.langs = langs
        Lang.__init__(self, langs)
        # override bu ozelligi cok kullanacagiz iyi ogrenmek lazim

    def get_details(self):
        # print(self.name, self.age, self.path)
        # super ile mevcut hali cagirip ilave edebiliriz.
        super().get_details()
        print(self.path)


emp1 = Employee('Emin', 31, 'Fullstack', ['Python', 'Js'])
emp1.get_details()
emp1.display_langs()

# person1 = Person('Aaron', 37)
# person1.get_details()

print(Employee.mro())

# inner class
