import copy

a = [1, 2, [3, 4]]

# 1. 赋值：同生共死
b = a
# 2. 浅拷贝：顶层分家，底层共享
c = a.copy()
# 3. 深拷贝：彻底分家
d = copy.deepcopy(a)

# 开始搞破坏：
a.append(5)        # 修改顶层元素
a[2][0] = 'X'      # 修改底层嵌套元素

print(f"原列表 a: {a}")
print(f"赋值 b  : {b}")
print(f"浅拷贝 c: {c}")
print(f"深拷贝 d: {d}")