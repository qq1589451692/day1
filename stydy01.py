print("hello,world!")


# 从键盘获取用户名密码并打印
# name=input("我的用户名是：")
# password=input("我的密码是：")
# # print(f'用户名是：{name},密码是：{password}')

# num1=input("请输入数字：")
# num2=input("请再输入一个数字：")
# num3=int(num1) + int(num2)
#
# print(num3)

# name=input("请输入姓名")
# if name=="admin":
#     print(name)
# else:
#     print("用户名输入错误！")

username=input("请输入姓名：")
password=input("请输入密码：")
if username=="admin" and password=="123456":
    print('登录成功！')
else:
    print("账户密码错误！")