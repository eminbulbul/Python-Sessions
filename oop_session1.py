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

class Person:
    name = 'Emin'
    age = 31

    def test(self):
        print('test')

    def set_details(self, name, age):
        self.name = name
        self.age = age

    def get_details(self):
        print(self.name, self.age)


person1 = Person()
person1.test()
Person.test(person1)

person1.get_details()
person1.set_details('Aaron', 37)
person1.get_details()
