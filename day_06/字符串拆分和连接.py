# coding = utf-8
# author: Wenhowe
# datetime: 2021/6/3 17:52
# software: PyCharm
import re

poems = " 客中行\t 李白 \t兰陵美酒郁金香 \t \n 玉碗盛来琥珀光 \t\t但使主人能醉客 \t\n不知何处是他乡！"
print(poems)

# 拆分字符串，去除所有空白字符
# poems_str = [poems.strip()]
# print(poems_str)
poems_str = poems.split()  # split将一个大字符串拆分成一个列表
print(poems_str)

# 连接字符串
str_result = " ".join(poems_str)
print(str_result)

str_list = ["aadbajfojgiowqrng ", "adhgiwjgrnwoingoaabbsada"]

result = ("".join(str_list).replace("a", "").replace("b", "")).split()
print(result)  # 打印去除指定字符后的字符串结果，并以列表展示

result = "".join(str_list).replace("a", "").replace("b", "")
print(result.split())  # 打印去除字符后的字符串结果，并以列表展示
print(result[::-1].split())  # 字符串倒序并以列表打印
print(len(result.split()))  # 打印去除字符后的字符串结果，并以列表展示
