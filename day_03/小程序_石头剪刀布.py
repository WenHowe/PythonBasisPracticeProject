# coding = utf-8
import random
"""
需求
1.从控制台输入要出的拳--石头(1) /剪刀(2) /布(3)
2.电脑随机出拳--先假定电脑只会出石头，完成整体代码功能
3.比较胜负
"""

# 1.从控制台输入要出的拳--石头(1) /剪刀(2) /布(3)

player = int(input("请输入你要出的  石头(1) /剪刀(2) /布(3)：  ", ))

# 2.电脑随机出拳
computer = random.randint(1, 3)

print("玩家出的是：%d  , 电脑出的是：%d  " % (player, computer))

# 比较胜负
# 石头 胜 剪刀
# 剪刀 胜 布
# 布 胜 石头

# 玩家赢
if ((player == 1 and computer == 2)
        or (player == 2 and computer == 3)
        or (player == 3 and computer == 1)):
    print("玩家赢了。。。")
# 平局
elif player == computer:
    print("哈哈，平局了，再来！")

# 电脑赢
else:
    print("电脑赢了，玩家输了。。。")
