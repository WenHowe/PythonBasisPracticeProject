# coding = utf-8
# author: wenhowe
# datetime: 2021/5/31 00:51
# software: PyCharm

"""
文件说明：

"""
# i = 0
# while i <= 100:
#     # 如果i==10，跳出循环体
#     if i == 10:
#         print("i = %d" % i)
#         break
#     i += 1


i = 0
while i <= 100:
    if i == 10:
        print("i = %d" % i)
        # break
        i += 1
        # continue 之前必须要让条件改变，否则会死循环
        continue
    i += 1
    print("i = %d" % i)
