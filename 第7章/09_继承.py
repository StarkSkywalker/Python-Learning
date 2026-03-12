class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def speak(self, msg):
        print(f'我叫{self.name}， 年龄是{self.age}， 性别是{self.gender}，我想说：{msg}')

class Student(Person):
    def __init__(self,name,age,gender,stu_id,grade):
        super().__init__(name,age,gender)
        self.stu_id = stu_id
        self.grade = grade

s1 = Student('李华',16,'男','2025001','初二')
print(s1.__dict__)
print(type(s1))