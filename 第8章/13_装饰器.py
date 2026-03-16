def say_hello(func):
    def wrapper(*args, **kwargs):
        print('你好，我要开始计算了！')
        return func(*args, **kwargs)
    return wrapper

@say_hello
def add(x, y):
    res = x + y
    print(f'{x}和{y}相加的结果是：{res}')
    return res

# add = say_hello(add)
# result = add(10, 20)
# print(result)


result = add(10, 20)
print(result)