# coding = utf-8
# author: wenhowe
# datetime: 2021/6/5 23:48
# software: PyCharm
students = [
    {"name": "张三"},
    {"name": "李四"}
]

# 在学生列表中搜索指定的名字
find_name = "王五"
for stu_dict in students:

    # print(stu_dict)
    if stu_dict["name"] == find_name:
        print("找到了 \"%s\"" % find_name)
        break
else:
    print("没有找到 \"%s\"" % find_name)
# print("循环结束")
