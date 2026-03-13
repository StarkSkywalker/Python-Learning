from datetime import datetime
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender


class Student(Person):
    count = 0

    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        Student.count += 1
        self.stu_id = f'{datetime.now().year}{Student.count:03d}'
        self.scores ={}

    def add_scores(self,subject,score):
        self.scores[subject] = score

    def calcu_avg(self):
        if self.scores:
            return sum(self.scores.values())
        else:
            return 0

    def __str__(self):
        return f'{self.name}({self.age}-{self.gender})，成绩：{self.scores}，平均分：{self.calcu_avg():.1f}'


class Manager:
    def __init__(self):
        self.stu_list = []

    def add_student(self):
        name = input('请输入姓名：')
        age = int(input('请输入年龄：'))
        gender = input('请输入性别：')

        stu = Student(name,age,gender)

        self.stu_list.append(stu)
        print(f'添加成功！学号是：{stu.stu_id}')

    def del_student(self):
        sid = input('请输入学号：')
        target = None

        for stu in self.stu_list:
            if stu.stu_id == sid:
                target = stu
                break

        if target:
            self.stu_list.remove(target)

