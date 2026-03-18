# def beauty(char, n):
#     def show_msg(msg):
#         print(char * n + msg + char * n)
#     return show_msg
#
# show1 = beauty('#',6)
# show1('你好呀')
# show1('Conia')


# def outer():
#     nums = []
#
#     def inner(value):
#         nums.append(value)
#         print(nums)
#
#     return inner
#
# # 每次调用 outer() 都创建一个新的 nums
# f1 = outer()
# f1(10)
# f1(20)
# f1(30)
# print('**********************')
# f2 = outer()
# f2(666)

class beauty:
    def __init__(self, char, n):
        self.char = char
        self.n = n

    def show(self, msg):
        print(self.char * self.n + msg + self.char * self.n)

b1 = beauty('*',3)
b1.show('Hello')
b1.show('Conia')
