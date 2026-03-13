class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def __str__(self):
        return f'姓名：{self.name}，年龄：{self.age}，性别：{self.gender}'

    def __len__(self):
        return len(self.__dict__)

    def __lt__(self, other):
        return self.age < other.age

    def __gt__(self, other):
        return self.age > other.age

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __getattr__(self, item):
        print(f'您访问的{item}属性，不存在！')
p1 = Person('张三', 18, '男')
p2 = Person('张三', 18, '男')
# p2 = Person('李四', 22, '女')

# print(p1)
# print(str(p1))

# print(len(p1))
print(p1 < p2)
print(p1 > p2)
print(p1 == p2)
print(p1.add)
