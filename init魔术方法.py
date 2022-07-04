# init传递参数  改进
class People:
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex
    def eat(self,food):
        print(self.name+'喜欢吃'+food)

xm=People('小明','18','男')
xm.eat('香蕉')
print(xm.name,xm.age,xm.sex)

lh=People('李辉','20','男')
lh.eat('苹果')
print(lh.name,lh.age,lh.sex)

xh=People('小花','18','女')
xh.eat('橘子')
print(xh.name,xh.age,xh.sex)

# 总结  __init__
# 1、python自带的内置函数，具有特殊的含义，使用双下划线包起来的魔术方法
# 2、是一个初始化方法，用来定义实例属性和初始话数据的，在创建对象的时候自动调用，不用手动取调用
# 3、利用传参的机制可以让我们定义功能更加强大并且方便的类 