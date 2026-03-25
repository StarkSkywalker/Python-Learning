# for i in range(3):
#     temp = "hello"
#
# # 循环结束后，i 和 temp 依然存活，并且可以在外面被随意访问！
# print(temp) # 正常输出 hello
# i=10
# for i in range(9):
#     i+=1
#
# print(i)


def make_counter():
    count = 0  # 这是外层函数的变量 (Enclosing scope)

    def inner():
        # 我们想在这里把外层的 count 加 1
        nonlocal count
        count = count + 1
        return count

    return inner


counter = make_counter()
print(counter())  # ❌ 报错：UnboundLocalError