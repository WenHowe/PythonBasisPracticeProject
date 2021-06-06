# coding = utf-8
# author: wenhowe
# datetime: 2021/6/5 23:59
# software: PyCharm

# 记录所有名片的字典列表
card_list = []


def show_menu():
    """
    显示系统菜单
    """

    print("*" * 50)
    print("欢迎使用【名片管理系统v1.0】")
    print("1. 新增名片")
    print("2. 显示名片")
    print("3. 查询名片")
    print("0. 退出系统")
    print("*" * 50)


def add_cards():
    """
    新增名片
    """

    # print("新增名片")
    # 提示用户输入名片信息
    name_str = input("请输入姓名：")
    phone_str = input("请输入电话号码：")
    email_str = input("请输入email：")
    # 将用户输入的信息结合成一个字典
    card_dict = {"name": name_str,
                 "phone": phone_str,
                 "email": email_str}
    # 将名片字典添加到列表中
    card_list.append(card_dict)
    # print("添加成功；", card_list)

    # 提示用户添加成功
    print("名片 \"%s\" 添加成功" % name_str)


def show_cards():
    """
    显示名片
    """

    print("-" * 50)
    # 判断是否存在名片数据，如果没有提示用户返回
    if len(card_list) == 0:
        print("没有名片信息，请先添加名片！")
    else:
        # 打印表头
        table_title = ["姓名", "电话", "邮箱"]
        for title in table_title:
            print(title, end="\t\t")
        print("")
        # 打印分割线
        print("=" * 50)
        # 遍历名片列表，展示所有名片信息
        for card_dict in card_list:
            print("%s\t\t%s\t\t%s" % (card_dict["name"],
                                      card_dict["phone"],
                                      card_dict["email"]))


def find_cards():
    """
    查找名片的基本操作
    """

    # 提示用户要查找的姓名
    find_name = input("请输入要查找的姓名：")
    # 遍历列表，查询要查找的姓名
    for card_dict in card_list:
        if card_dict["name"] == find_name:
            print("姓名\t\t电话\t\t邮箱")
            print("=" * 50)
            print("%s\t\t%s\t\t%s" % (card_dict["name"],
                                      card_dict["phone"],
                                      card_dict["email"]))
            # 对找到的名片执行修改或删除的操作
            deal_card(card_dict)
            break

    else:
        print("没有找到%s：" % find_name)
        # return find_cards()


def deal_card(find_dict):
    """选择查找名片后的操作：处理名片
    Args:
        find_dict: 查找到的名片
    Returns:返回本步骤
    """

    action_str = input("请输入你需要的操作：1.修改名片；2.删除名片；0.返回主菜单")
    if action_str == "1":
        print("请输入需要修改的信息")
        find_dict["name"] = input_card_info(find_dict["name"], "请输入姓名：（回车不修改）")
        find_dict["phone"] = input_card_info(find_dict["phone"], "请输入电话：（回车不修改）")
        find_dict["email"] = input_card_info(find_dict["email"], "请输入邮箱：（回车不修改）")
        print("修改名片成功！")
    elif action_str == "2":
        card_list.remove(find_dict)
        print("删除名片成功！")
    else:
        print("你输入有误，请按要求输入：")
        return deal_card(find_dict)


def input_card_info(dict_value, tip_message):
    """选择修改名片后的操作
    Args:
        dict_value: 字典中原有的值
        tip_message: 输入提示
    Returns: 如果用户有输入则返回结果，没有则返回原有的值
    """

    # 提示用户输入内容
    result_str = input(tip_message)
    # 如果用户输入了内容，直接返回结果
    if len(result_str) > 0:
        return result_str
    # 如果用户没有输入内容，返回列表原有的值
    else:
        return dict_value
