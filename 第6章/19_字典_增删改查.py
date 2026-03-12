d1 = {'张三':72,'李四':60,'王五':85}
# d1['赵六']=100
# print(d1)

# del d1['张三']
# print(d1)

# result = d1.pop('张三')
# result = d1.pop('赵六','删除失败')
# print(d1)
# print(result)

# d1.clear()
result = d1['张三']
print(d1)
print(result)

result = d1.get('赵六','没这个人')
print(result)