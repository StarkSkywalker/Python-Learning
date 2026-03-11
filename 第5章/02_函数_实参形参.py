def order():
    num =1
    dish = '猪脚饭'
    print(f'您点的是：{num}份{dish}\n')

order()

def order(num ,dish):
    print(f'您点的是：{num}份，{dish}')
    print(f'{dish}真好吃')
    print(f'您点的{num}份，够吃吗？')
order(1,'猪脚饭')
order(2,'袁记云饺')