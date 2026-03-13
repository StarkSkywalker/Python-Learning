class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

# print(issubclass(Person,object))

p1 = Person('张三', 18, '男')
# print(isinstance(p1,Person))
# print(isinstance(p1,object))

# for key in object.__dict__:
#     print(key)

print(p1.__dict__)
print(dir(p1))