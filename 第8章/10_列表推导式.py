nums = [10, 20, 30, 40]
result = list(map(lambda x: x * 2, nums))
# print(result)

result1 = []
for n in nums:
    result1.append(n * 2)
# print(result1)

result2 = [n * 2 for n in nums]
# print(result2)

result3 = [n * 2 for n in nums if n > 20]
# print(result3)

names = ['张三', '李四', '王五']
scores = [60, 70, 80]
result4 = {names[i]:scores[i] for i in range(len(names))}
print(result4)
