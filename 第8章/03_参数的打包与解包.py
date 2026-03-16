def show_info(*args, **kwargs):
    print(args)
    print(kwargs)


nums = (10, 20, 30)
person = {'name': '张三','age' : 18 }

show_info(nums, person)

