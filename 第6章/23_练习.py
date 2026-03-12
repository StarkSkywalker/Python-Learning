# 练习一：水果清单
from os import name

fruits = {
    '苹果': 4.5,
    '香蕉': 3.2,
    '橙子': 5.8,
    '草莓': 12.0,
    '哈密瓜': 8.8
}
#
# # 需求1：打印所有的水果
# for item in fruits:
#     print(f'{item}:{fruits[item]} 元/斤')
#
# # 需求2：找到最贵水果
# key = max(fruits,key = fruits.get)
# print(f'最贵的是{key}为{fruits[key]} 元/斤')

# 练习二：学生成绩表
students = [
    {
        'name': '张三',
        'scores': {'语文': 88, '数学': 92, '英语': 95}
    },
    {
        'name': '李四',
        'scores': {'语文': 75, '数学': 83, '英语': 80}
    },
    {
        'name': '王五',
        'scores': {'语文': 92, '数学': 95, '英语': 88}
    }
]

# 需求1：计算每位学生的平均分
# for stu in students:
#     score_list = stu['scores'].values()
#     avg = sum(score_list) / len(score_list)
#     print(f'{stu['name']}的平均成绩为：{avg:.1f}')

# 需求2：找到总分最高的学生
# def find_best():
#     best_students = []
#     best_score = 0
#     for stu in students:
#         total = sum(stu['scores'].values())
#         if total > best_score:
#             best_students= [stu['name']]
#             best_score = total
#         elif total == best_score:
#             best_students.append(stu['name'])
#
#     print(f'最高分为{best_score}，取得最高分的学生是{best_students}')
#
# find_best()

# 练习三：评论内容
comment = '这家奶茶真好喝，环境也不错，就是价格有点贵，好喝好喝好喝！强烈推荐！'

# 需求1：统计“好喝”出现次数
print(comment.count('好喝'))
# 需求2：将字符串中的“贵”替换为“略高”
comment1 = comment.replace('贵','略高')
print(comment1)
# 需求3：是否包含“推荐”两个字
print('推荐' in comment)