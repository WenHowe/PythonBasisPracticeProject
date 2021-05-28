#*.*--encoding:utf-8
# 定义整数变量，判断年龄是否正确
age = 120

# 要求年龄在0-120
"""
and, or, 
age >=0,<= 120
age >= 0 and age <= 120
"""
if age >= 0 and age <= 120:
	print("这是人类的年龄")
else:
	print("天呐，这是古树吗")


# #################################
# 定义整数变量，判断成绩是否合格
python_score = 90
java_score =  60

# 大于60分，成绩就合格
if not python_score < 60 and java_score < 60:
	print("Python成绩合格")
	print("Java成绩合格")

else:
	print("成绩不合格")

# #################################
is_employee = F
if not is_employee:
	print("非本公司员工")



