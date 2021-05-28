# 坐高铁，买车票，过安检
# 1. 是否购买了车票
has_ticket = True
# 2. 是否携带了违禁品
has_contraband = True

if has_ticket:
    print("车票检验通过，请前往安检门")
    if has_contraband:
        print("安检通过，请前往候车点")
        # 3. 成功上车
        print("祝您旅途愉快！")
    else:
        print("您携带了违禁品，不能通过安检")
else:
    print("请购买车票")
