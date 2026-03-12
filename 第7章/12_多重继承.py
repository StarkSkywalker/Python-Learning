class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    def speak(self):
        print(f'我叫{self.name}， 年龄是{self.age}， 性别是{self.gender}')

class Worker:
    def __init__(self,company):
        self.company = company
    def do_work(self):
        print(f'我在{self.company}做兼职')

class Student(Person,Worker):
    def __init__(self,name, age, gender,company,stu_id,grade):
        Person.__init__(self, name, age, gender)
        Worker.__init__(self,company)
        self.stu_id = stu_id
        self.grade = grade
    def study(self):
        print(f'我在努力学习，争做{self.grade}第一名')

s1 = Student('张三',18,'男','麦当劳','2025001','初二')
print(s1.__dict__)

s1.speak()
s1.do_work()
s1.study()

print(Student.__mro__)