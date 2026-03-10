name = 'AmAo'
gender = '男'
weight = 65.2
age = 12

# 写法 1：直接用加号进行拼接，写起来很麻烦，而且只能是字符串之间拼接。
info1 = '我叫' + name + '，我是' + gender + '生'

# 写法 2：使用占位符。
# ● %s占位字符串
# ● %f占位浮点数
# ● %i占位整数
# ● %d占位十进制的整数
# ● %s是万能的（如果我们提供的数据不是字符串，那 Python 就会把数据转成字符串）。
info2 = '我叫%s，我是%s生，我体重是%f，年龄是%d' % (name, gender, weight, age)

# 写法 3：使用 f-string，这是目前 Python 最推荐的方式。
info3 = f'我叫{name}，我是{gender}生，我体重是{weight}，年龄是{age}'
