s1 = {10, 20, 30, 40, 50}
s2 = {30, 40, 50, 60, 70}
s3 = {10, 20, 30}
# result = s1.difference(s2)
# result = s1.difference_update(s2)
# result = s1.union(s2)
# result = s3.issubset(s1)
# result = s1.issuperset(s3)
result = s1.isdisjoint(s2)
print(s1)
print(s2)
print(result)
