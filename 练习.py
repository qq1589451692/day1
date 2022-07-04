# 猜年龄小游戏，有三点需求
# 1.允许用户最多尝试三次
# 2.每尝试三次后，如果还没猜对，就问用户是否还想继续玩，如果回答Y或者y，就继续让其猜三次，以此往复，如果回答N或者n，就推出程序
# 3.如果猜对了，就直接退出
times=0
while times<=3:
    age=int(input("请输入您要猜的年龄："))
    if age==25:
        print("恭喜您猜对了！")
        break
    elif age<25:
        print("猜小了，请再试试！")
    else :
        print("猜大了，请再试试！")
    times+=1
    if times==3:
        choose=input("是否还想继续玩Y/N:")
        if choose=='Y' or choose=="y":
            times=0  #次数重置
        elif choose=='N' or choose=='n':
            times=4
        else:
            print("输入错误")
            break



#
# 小王身高1.75，体重80.5kg，请根据BMI公式（体重除以身高的平方）帮小王计算他的BMI指数，并根据BMI指数：
# 低于18.5，过轻
# 18.5-25，正常
# 25-28，过重
# 28-32，肥胖
# 高于32，严重肥胖
# 用if，else判断并打印结果
# height=float(input("请输入你的身高（M）:"))
# weight=float(input("请输入你的体重（KG）："))
# if weight/(height**2) < 18.5:
#     print("您的体重过轻！请增强营养摄入和锻炼！")
# elif weight/(height**2)>=18.5 and weight/(height**2) < 25:
#     print("您的体重正常，请继续保持！")
# elif weight/(height**2)>=25 and weight/(height**2) < 28:
#     print("您的体重过重，请增强体育锻炼，控制饮食！")
# elif weight/(height**2)>=28 and weight/(height**2) < 32:
#     print("您的体重属于肥胖，请增强体育锻炼，控制饮食！")
# else:
#     print("您属于严重肥胖！")
