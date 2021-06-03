# coding = utf-8
# author: Wenhowe
# datetime: 2021/6/3 17:00
# software: PyCharm

hello_python_str = "Hello Python String"

# 判断是否以指定字符串开始
print(hello_python_str.startswith("Hello"))
print(hello_python_str.startswith("hello"))  # 字符串严格区别大小写

# 判断是否以指定字符串结束
print(hello_python_str.endswith("ing"))

# 查找指定字符串
print(hello_python_str.find("P"))  # find查找的字符串如果不存在则返回-1
# print(hello_python_str.index("p"))  # index查找的字符串如果不存在会报错
print(hello_python_str.rfind("i"))  # rfind从右边开始查找字符串的索引
print(hello_python_str.rindex("g"))  # 从右边开始查找字符串的索引

# 替换指定字符串
print(hello_python_str.replace("String", ""))

print(hello_python_str)
