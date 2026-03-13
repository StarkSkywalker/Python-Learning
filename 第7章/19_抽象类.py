from abc import ABC,abstractmethod
class MustRun(ABC):
    @abstractmethod
    def run(self):
        pass

class Person(MustRun):
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender


    def run(self):
        print(f'我叫{self.name}，我在努力的奔跑！')

p1  = Person('张三',18,'男')
p1.run()