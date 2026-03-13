class Dog:
    def speak(self):
        print('汪汪汪！')


class Cat:
    def speak(self):
        print('喵喵喵！')

class Fish:
    def speak(self):
        print('咕噜噜！')

class Pig:
    def speak(self):
        print('哼哼哼！')

def make_sound(animal):
    animal.speak()

d1 = Dog()
c1 = Cat()
f1 = Fish()
p1 = Pig()

make_sound(d1)
make_sound(c1)
make_sound(f1)
make_sound(p1)