from functools import reduce

nums = [1,2,3,4,5]
result = reduce(lambda a,b : a+b,nums,10)
# print(result)

str_list = ['ab','cd','ef']
result_list = reduce(lambda a,b:a+b,str_list,'00001')
print(result_list)