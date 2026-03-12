class Person:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

p1 = Person('张三',18,'男')
p2 = Person('李四',20,'女')

# print(p1)
# print(p2)
#
# print(p1.name)
# print(p1.age)
# print(p1.gender)
# print('*'*20)
# print(p2.name)
# print(p2.age)
# print(p2.gender)
p1.name = '阿三'

p1.address = '广东'

print(p1.__dict__)
print(p2.__dict__)

print(type(p1))
print(type(p2))