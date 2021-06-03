# coding = utf-8
# author: Wenhowe
# datetime: 2021/6/3 17:41
# software: PyCharm

poems = ["客中行",
             "\t\n李白",
             "兰陵美酒郁金香",
             "玉碗盛来琥珀光\t\n",
             "但使主人能醉客",
             "不知何处是他乡！"]
for poems_str in poems:
    print("|%s|" % poems_str.strip().center(10, "　"))
