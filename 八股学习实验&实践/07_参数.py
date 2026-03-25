# 注意严格的顺序：必须先 位置参数(name)，再 *args，最后 **kwargs
def show_user_info(name, *args, **kwargs):
    print(f"主干信息 - 姓名: {name}")

    # args 是一个元组
    if args:
        print(f"附加标签 (元组): {args}")

    # kwargs 是一个字典
    if kwargs:
        print(f"详细档案 (字典): {kwargs}")


# 调用演示：
# "张三" 传给了 name
# "高个子", "老员工" 这种没有名字的，被打包进了 args 元组
# age=28, city="北京" 这种带名字的，被打包进了 kwargs 字典
show_user_info("张三", "高个子", "老员工", age=28, city="北京")