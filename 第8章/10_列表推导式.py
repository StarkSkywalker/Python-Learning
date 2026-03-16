nums = [10,20,30,40]
result = list(map(lambda x:x*2 ,nums))
# print(result)

result1 =[]
for n in nums:
    result1.append(n*2)
# print(result1)

result2 = [n*2 for n in nums]
# print(result2)

result3 = [n*2 for n in nums if n>20]
print(result3)

