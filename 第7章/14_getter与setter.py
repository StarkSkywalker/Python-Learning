class Person:
    def __init__(self, name, age, idcard):
        self.name = name
        self._age = age
        self.__idcard = idcard

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value <= 120:
            self._age = value
        else:
            print('年龄非法，已将年龄修改为最大值')
            self._age = 120

    @property
    def idcard(self):
        return self.__idcard[:6]+'*'*20+self.__idcard[-4:]

    @idcard.setter
    def idcard(self,value):
        print('不允许修改身份证号！！！')

p1 = Person('张三', 18, '110101199001011234')
print(p1.age)

p1.age = 199
print(p1.age)

print(p1.idcard)
p1.idcard = '111111'
