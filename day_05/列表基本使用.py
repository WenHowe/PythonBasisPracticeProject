# coding = utf-8
# author: wenhowe
# datetime: 2021/6/1 17:06
# software: PyCharm


# 定义列表变量
name_list = ["zhangsan", "lisi", 123]

# 取列表值
print(name_list[0])
# 取列表索引
print(name_list.index(123))

# 修改列表的数据
name_list[2] = "wangwu"

# 增加列表数据
# 在列表末尾追加数据
name_list.append(123)
# 在列表指定索引位置插入数据
name_list.insert(0, 13)
# 参数化传递插入数据，可将参数化的列表内容增加到其他列表末尾
temp = [147, 258, "zhangsan"]
name_list.extend(temp)

# 删除列表的数据
name_list.remove(123)
# 默认删除最后一个元素
name_list.pop()
name_list.pop(4)
# 清空列表数据
name_list.clear()
# 关键字删除列表数据,del是从内存中删除变量
name_list = [147, 258, "zhangsan"]
del name_list[0]

print(name_list)
