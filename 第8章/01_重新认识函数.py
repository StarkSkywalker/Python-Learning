a1  = 100
a2 = 'hello'
a3 = [10,20,30]

# def welcome():
#     print('你好啊！')

# print(type(a1))
# print(type(a2))
# print(type(a3))
# print(type(welcome))

# welcome.desc= '这是个用于打招呼的函数'
# welcome.version = 1.0
# print(welcome.__dict__)
#
# welcome()

# say_hello = welcome
# say_hello()
# welcome()

def welcome():
    print('你好啊')
    def show_msg(msg):
        print(msg)
    return show_msg

result = welcome()
result('尚硅谷')
# welcome()('尚硅谷')