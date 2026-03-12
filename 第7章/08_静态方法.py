from datetime import datetime


class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    @staticmethod
    def is_adult(year):
        current_year = datetime.now().year
        age = current_year - year
        return age >= 18

    @staticmethod
    def mask_idcard(idcard):
        return idcard[:6]+'*'*6+idcard[-4:]

p1 = Person('张三', 18, '男')

# print(Person.__dict__)
# result = Person.is_adult(2015)
# print(result)

result = Person.mask_idcard('212101198802030028')
print(result)