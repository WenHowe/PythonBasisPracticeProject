# coding = utf-8
# author: wenhowe
# datetime: 2021/6/6 00:05
# software: PyCharm
"""
【名片管理系统】V1.0
根据用户的输入，选择对应的选择
1. 新建名片, 2. 显示名片, 3. 查询名片
0. 退出系统
输入0-3范围外的操作均为错误，需要提示用户
"""
# 无限循环，由用户决定什么时候结束程序
import cards_tools

while True:
    cards_tools.show_menu()
    # 显示系统功能菜单
    action_str = input("请输入您希望执行的操作：")
    # print("您选择的操作是：【%s】" % action_str)
    if action_str in ["1", "2", "3"]:
        # TODO 新增名片
        if action_str == "1":
            print("您选择的操作是：1. 新增名片")
            cards_tools.add_cards()
        # TODO 显示名片
        if action_str == "2":
            print("您选择的操作是：2. 显示名片")
            cards_tools.show_cards()
        # TODO 查询名片
        if action_str == "3":
            print("您选择的操作是：3. 查询名片")
            cards_tools.find_cards()
        pass
    # 如果用户选择0，则跳出循环并结束程序
    elif action_str == "0":
        print("您选择的操作是：0. 退出系统")
        print("欢迎再次使用【名片管理系统】！")
        break
    else:
        print("您输入有误，请在\"0-3\"之内输入")
