nums = [10,20,30,40]
result = sorted(nums)
# print(result)

persons = [
    {'name':'张三', 'age':15, 'gender':'男'},
    {'name':'李四', 'age':17, 'gender':'女'},
    {'name':'王五', 'age':19, 'gender':'男'},
    {'name':'李华', 'age':20, 'gender':'女'},
    {'name':'赵六', 'age':18, 'gender':'女'},
    {'name':'孙七', 'age':16, 'gender':'男'}
]
result1 = sorted(persons,key = lambda p:p['age'],reverse=True)
print(result1)

result2 = max(persons,key = lambda p:p['age'])
result3 = min(persons,key = lambda p:p['age'])
print(result2,result3)