# coding = utf-8
# author: wenhowe
# datetime: 2021/5/31 00:12
# software: PyCharm

"""
文件说明：
计算0-100之间所有偶数的和
1、编写循环体，确定要计算的偶数
2、添加结果变量，在循环体内部计算结果
"""
# 计数器
i = 0

# 结果变量
result = 0
while i <= 100:
    # 取余，整除2为0则为偶数
    if i % 2 == 0:
        print("i= : %d " % i)
        # 循环一次，result会跟计数器想加
        result += i
        print("result = : %d" % result)
    i += 1

print("result = : %d " % result)
