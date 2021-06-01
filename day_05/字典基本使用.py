# coding = utf-8
# author: wenhowe
# datetime: 2021/6/1 19:21
# software: PyCharm

mayun = {"name": "马云",
         "age": 18,
         "height": 1.65,
         "weight": 60,
         "savor": "唱K"}

# 取值
print(mayun["name"])

# 增加
print(mayun)

# 修改
mayun["age"] = 28
print(mayun)

# 删除
mayun.pop("age")

print(mayun)

# 统计字典的键值对总数
mayun_len = "字典键值对元素的总数是：%d 个" % len(mayun)
print(mayun_len)

# 合并字典
temp_dict = {"bent": "开演唱会"}
mayun.update(temp_dict)
print(mayun)

# 清空字典
mayun.clear()
print(mayun)