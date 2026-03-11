def test(args):
    print(f'我是test函数，我收到的参数是:{args},参数类型是：{type(args)}')

list1 = [100,200,300,400]
tuple1 = ('你好','北京','AmAo')

test(list1)
test(tuple1)