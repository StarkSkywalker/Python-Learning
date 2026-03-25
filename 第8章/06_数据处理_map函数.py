# nums = [10, 20, 30, 40]
# result = map(lambda x: x * 2, nums)
# print(result)
# print(list(result))
# print(list(result))


# 统一数据处理
nums = [10, 20, 30, 40]
# map函数的返回值是一个迭代器对象，需要我们自己去手动遍历，或者手动类型转换
result = map(lambda x: x * 2, nums)
print(list(result))
print(nums)

# 字符串转换
names = ('python', 'java', 'js')
result = map(lambda x: x.upper(), names)
print(tuple(result))
print(names)

# 类型转换
str_number = {'1', '2', '3'}
result = map(int, str_number)
print(set(result))
print(str_number)

# 注意点：
# 1.延迟执行：map 不会立刻计算，只有在“需要结果”时才执行计算。
# 2.返回的是迭代器对象，且一旦遍历完成，就会被“耗尽”。
# 3.map不会影响元素数量。不管怎么加工，原本多少个就多少个

nums = [10, 20, 30, 40]
result = list(map(lambda x: x * 2, nums))# 及时用一个变量去接收保存才不会被“耗尽”
print(result)
print(result)
print(result)
print(result)