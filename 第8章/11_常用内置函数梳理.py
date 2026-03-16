# abs() =========> 取绝对值
print(abs(-9))      # 9
print(abs(-2.5))    # 2.5
print(abs(3 - 5))   # 2


# round() =======> 四舍五入
# 注意：round函数的四舍五入，是银行家舍入法：小于5就舍，大于5就入，等于5看奇偶（奇入偶舍）
print(round(3.4))   # 3
print(round(4.6))   # 5
print(round(6.5))   # 6
print(round(7.5))   # 8
print(round(7.543, 2))  # 7.54  第二个参数：保留几位小数

# pow()	=========> 次方
print(pow(2, 3))    # 2的3次方
print(pow(2, -1))   # 2的-1次方
print(pow(2, 0.5))  # 2的开平方
print(pow(2, 3, 5)) # 2的3次方对5取模


# divmod() ======> 商和余数
print(divmod(10, 3)) # （3，1）