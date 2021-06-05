# coding = utf-8
# author: wenhowe
# datetime: 2021/6/5 23:40
# software: PyCharm
num = [1, 2, 3, 4, 5]
# for i in num:
#     print(i, end=", ")
# else:
#     print("列表遍历完毕")
# print("循环结束")

for i in num:
    print(i, end=", ")
    if i == 5:
        break
else:
    print("列表遍历完毕")
print("循环结束")
