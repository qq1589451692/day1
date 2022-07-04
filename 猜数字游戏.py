# 猜数字游
# 1.电脑产生一个(1,100)的随机数，用户进行猜测，知道猜中为止
# 2.如果猜对了，输出：恭喜你猜对了，数字是xx
# 3.如果猜测的数字比随机数大，输出：猜测的数字太大了，继续加油
# 4.如果猜测的数字比随机数小，输出：猜测的数字有点小，请再来一次

# import random
# num=random.randint(1,100)
# while True:
#     user_num=int(input("请输入一个1到100的随机数："))
#     if num > user_num:
#         print("猜测的数字有点小，请再来一次！")
#     else:
#         print("猜测的数字太大了，继续加油！")
#         if num == user_num:
#             print(f"恭喜你猜对了，数字是：{user_num}")
#             break
#


# 打印九九乘法表
row=1
while row<=9:
    col=1
    while col<=row:
        print("%d*%d=%d"%(row,col,row*col),end=" ")
        col+=1
    print()
    row+=1