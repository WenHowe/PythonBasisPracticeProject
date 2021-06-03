# coding = utf-8
# author: Wenhowe
# datetime: 2021/6/3 17:26
# software: PyCharm

poems = ["客中行",
             "李白",
             "兰陵美酒郁金香",
             "玉碗盛来琥珀光",
             "但使主人能醉客",
             "不知何处是他乡！"]

for poems_str in poems:
    # print(poems_str.center(10))  # 居中10个空格字符串
    print("|%s|" % poems_str.center(10, "　"))  # 使用中文全角10空格居中显示对齐字符串
    # print("|%s|" % poems_str.ljust(10, "　"))  # 使用中文全角10空格向左显示对齐字符串
    # print("|%s|" % poems_str.rjust(10, "　"))  # 使用中文全角10空格向右显示对齐字符串
