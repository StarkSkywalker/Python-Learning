class SayHello:
    def __call__(self, func):
        def wrapper(*args, **kwargs):
            print('你好，我要开始计算了')
            return func(*args, **kwargs)

        return wrapper


# def add(x, y):
#     res = x + y
#     print(f'{x}和{y}相加的结果是{res}')
#     return res
#
#
# say = SayHello()
# add = say(add)
#
# result = add(10, 20)
# print(result)

# @SayHello()
# def add(x, y):
#     res = x + y
#     print(f'{x}和{y}相加的结果是{res}')
#     return res
#
#
# result = add(10, 20)
# print(result)
#
# class SayHello:
#     def __init__(self,msg):
#         self.msg = msg
#
#     def __call__(self,func):
#         def wrapper(*args,**kwargs):
#             print(f'你好，我要开始{self.msg}计算了')
#             return func(*args,**kwargs)
#         return wrapper
#
# @SayHello('加法')
# def add(x,y):
#     res = x+y
#     print(f'{x}和{y}相加的结果是{res}')
#     return res
#
# result = add(1,2)
#
