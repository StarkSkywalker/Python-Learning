class Person:
    def __init__(self,name,age,gender):
        self.name = name
        self.age  = age
        self.gender = gender

    def speak(self,msg):
        print(f'我叫{self.name}， 年龄是{self.age}， 性别是{self.gender}，我想说：{msg}')

    # 自定义方法（给实例添加行为）
    def run(self, distance):
        print(f'{self.name}疯狂的奔跑了{distance}米')

p1 = Person('张三', 18, '男')
p2 = Person('李四', 22, '女')

print(Person.__dict__)
print(p1.__dict__)
print(p2.__dict__)

p1.speak('ahhahahah')
p1.run(300)

