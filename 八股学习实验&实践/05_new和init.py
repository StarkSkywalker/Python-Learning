# class Person:
#     def __new__(cls, name):
#         print(f'调用new，正在为{name}开辟内存空间')
#         instance = super().__new__(cls)
#
#         print(f'躯体制造完成，内存地址：{id(instance)}')
#         return instance
#
#     def __init__(self,name):
#         print(f'init正在被调用，接收到示例：{id(self)}')
#         print(f'赋予实例名字{name}')
#         self.name = name
#
# print('开始创建对象')
# p = Person('张三')
# print(f'最终得到的对象：p.name = {p.name}')

########## 创建单例模式
class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            print('new 发现这是第一次实例化，开始造对象')
            cls._instance = super().__new__(cls)
        else:
            print('new 发现已经有对象了，拒绝新建，直接返回旧的')
        return cls._instance

    def __init__(self, name):
        print(f"[__init__] 开始初始化，名字设为: {name}")
        self.name = name

# 测试单例模式
print("--- 尝试创建第一个对象 ---")
obj1 = Singleton("系统配置_1")

print("\n--- 尝试创建第二个对象 ---")
obj2 = Singleton("系统配置_2")

print("\n--- 验证阶段 ---")
print(f"obj1 的名字: {obj1.name}")
print(f"obj2 的名字: {obj2.name}")
print(f"它们是同一个对象吗？ {obj1 is obj2}")
