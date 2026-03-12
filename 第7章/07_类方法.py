from datetime import datetime
from traceback import print_tb

class Person:
    max_age = 120
    planet = '地球'

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def speak(self, msg):
        print(f'我叫{self.name}， 年龄是{self.age}， 性别是{self.gender}，我想说：{msg}')

    # 自定义方法（给实例添加行为）
    def run(self, distance):
        print(f'{self.name}疯狂的奔跑了{distance}米')

    @classmethod
    def change_planet(cls,value):
        cls.planet =value

    @classmethod
    def create(cls,info_str):
        name,year,gender = info_str.split('-')
        current_year = datetime.now().year
        age = current_year-int(year)
        return cls(name,age,gender)



p1 = Person('张三', 18, '男')
p2 = Person('李四', 22, '女')

print(Person.__dict__)

Person.change_planet('月球')
# print(Person.__dict__)

# print(p1.planet)
# print(p2.planet)

p3 = Person.create('李华-2003-女')
print(p3.__dict__)