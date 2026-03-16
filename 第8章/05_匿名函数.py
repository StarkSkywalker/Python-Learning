add1 = lambda x, y: x + y
add2 = lambda x: x + x
add3 = lambda: print('ahhahaah')

res1 = add1(1, 2)
res2 = add2(1)
res3 = add3()


# print(res1,res2,res3)

def calculate(func, x, y):
    print(f'计算结果为{func(x, y)}')

#
# calculate(lambda x, y: x + y, 10, 20)
# calculate(lambda x, y: x - y, 30, 20)

is_adult = lambda age : '成年' if age>=18 else '未成年'
print(is_adult(18))
print(is_adult(1))
