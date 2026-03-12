class Person:
    max_age = 120
    planet = '地球'
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

# print(Person.__dict__)

# 创建Person类的实例对象
p1 = Person('张三', 18, '男')
p2 = Person('李四', 22, '女')

# print(p1.__dict__)
# print(p2.__dict__)

print(Person.max_age)
print(p1.max_age)
print(p1.planet)

p1.max_age = 300
print(Person.__dict__)
print(p1.__dict__)
print(p2.__dict__)
print(p1.max_age)
print(p2.max_age)
