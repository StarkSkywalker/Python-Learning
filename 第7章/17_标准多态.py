class Animal:
    def speak(self):
        print('动物正在发出声音')


class Dog(Animal):
    def speak(self):
        print('汪汪汪！')


class Cat(Animal):
    def speak(self):
        print('喵喵喵！')


def make_sound(animal: Animal):
    animal.speak()


a1 = Animal()
d1 = Dog()
c1 = Cat()

make_sound(a1)
make_sound(d1)
make_sound(c1)