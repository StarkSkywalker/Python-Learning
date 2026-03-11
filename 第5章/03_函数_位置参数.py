def order(num, dish):
    print(f'您点的是：{num}份 {dish}')
    print(f'{dish}可是很好吃的！')
    print(f'你只点了{num}份，够吃吗？\n')

# 以下是错误示范
order(3)  # 参数少了
order(4, '宫保鸡丁', 7)  # 参数多了
order('宫保鸡丁', 4)  # 实参顺序没有和形参保持一致，不会报错，但会造成数据错乱。