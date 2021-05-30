# coding = utf-8
# author: wenhowe
# datetime: 2021/5/31 02:53
# software: PyCharm


def num_sum(num1, num2):
    """两个变量相加的和

    Args:
        num1: 第一个数字
        num2: 第二个数字

    Returns:

    """
    # num1 = 10
    # num2 = 20
    result = num1 + num2
    # print("%d + %d = %d" % (num1, num2, result))
    # 返回结果
    return result


# num_sum(1, 2)
# num_sum(int(input("请输入num1")), int(input("请输入num2")))

sum_result = num_sum(2, 3)
print("相加结果：%d" % sum_result)
