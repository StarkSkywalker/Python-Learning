class Person:
    def __init__(self,name,age,idcard):
        self.name = name
        self._age = age
        self.__idcard = idcard

    def speak(self):
        print(f'我叫：{self.name}，年龄：{self._age}，身份证：{self.__idcard}')

class Student(Person):
    def hello(self):
        print(f'我是学生，我叫{self.name}，年龄是{self._age}，身份证：{self.__idcard}')

p1 = Person('张三', 18, '110101199001011234')
s1 = Student('李四', 20, '110101188601011234')

print(p1.__dict__)

print(s1.__dict__)
# print(s1.idcard)