# coding = utf-8
# author: wenhowe
# datetime: 2021/6/1 17:37
# software: PyCharm

name_list = ["zhangsan", "lisi", "wangwu", "zhangsan", "lisi", "zhangsan"]

# 统计列表内元素的总数
list_len = len(name_list)
print("列表一共有%d个元素" % list_len)

# 统计列表内某个元素出现的次数
list_count = name_list.count(name_list[0])
print("\"%s\"元素在列表内一共出现了%d次" % (name_list[0], list_count))

# 迭代遍历列表
for my_name in name_list:
    print(my_name)