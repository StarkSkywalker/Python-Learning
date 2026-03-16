nums = [10, 20, 30, 40]
result = filter(lambda n: n > 30, nums)
# print(list(result))

person = [
    {'name': '张三', 'age': 18, 'gender': '男'},
    {'name': '李四', 'age': 19, 'gender': '女'},
    {'name': '王五', 'age': 20, 'gender': '男'},
    {'name': '赵六', 'age': 21, 'gender': '女'},
    {'name': '孙七', 'age': 22, 'gender': '男'}
]

result1 = filter(lambda p:p['age'] >= 20,person)
# print(list(result1))

names = ['张三', '', '李四', None, '王五']
result2 = filter(lambda n:n,names)
# print(list(result2))

data = [0, 1, '', 'hello', [], (), 5]
result3 = filter(None,data)
print(list(result3))

