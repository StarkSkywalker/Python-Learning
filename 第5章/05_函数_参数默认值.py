def greet(name, gender, age, height,msg='你好'):
    print(f'我叫{name}，性别{gender}，年龄是{age}，体重是{height}cm')
    print(f'我想说：{msg}')

greet('zhangsan','男',18,172)
greet('zhangsan','男',18,172,'hello')
greet('zhangsan','男',18,172,msg='hello')

