# class Person:
#     def __init__(self, name, age, gender, address):
#         self.name = name
#         self.age = age
#         self.gender = gender
#         self.address = address
#         self.__attr = [name, age, gender, address]
#
#     def __iter__(self):
#         # yield self.name
#         # yield self.age
#         # yield self.gender
#         # yield self.address
#         yield from self.__attr
#
# p1 = Person('张三', 18, '男', '北京昌平')
# # 目标：
# for attr in p1:
#     print(attr)


def create_car(total):
    for index in range(1, total + 1):
        yield f'我是第{index}台车'

# cars是生成器对象
cars = create_car(5)

c1 = next(cars)
print(c1)
c2 = next(cars)
print(c2)
c3 = next(cars)
print(c3)
c4 = next(cars)
print(c4)
c5 = next(cars)
print(c5)

