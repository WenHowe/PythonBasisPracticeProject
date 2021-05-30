# coding = utf-8
# author: Wenhowe
# contact: zengwenhao0710@gmail.com
# datetime: 2021/5/30 16:02
# software: PyCharm

"""
文件说明：

"""
# 定义 计数器 i
i = 0
# while i < 5:
#     print("i = : %d" % i)
#     # i = i + 1
#     i += 1

# 计算0 - 100之间所有整数的和
# 定义最终结果的变量
result = 0
# 循环体
while i <= 100:
    print("i = ： %d" % i)

    # 循环一次，result需要和计数器想加一次
    result += i

    # 处理计数器
    i += 1
print("result = ： %d" % result)
