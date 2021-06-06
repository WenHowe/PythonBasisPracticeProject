# coding = utf-8
# author: Wenhowe
# datetime: 2021/6/3 18:20
# software: PyCharm

hello_python_str = "Hello Python String"
print(hello_python_str[2:])  # 从索引2开始切片
print(hello_python_str[1::2])  # 从索引1开始切片，间隔2个字符切一次
print(hello_python_str[:7:])  # 切片到索引为7为止

print(hello_python_str[:])  # 字符串正序切片
print(hello_python_str[-1::-1])  # 字符串倒序切片
print(hello_python_str[::-1])  # 字符串倒序切片

