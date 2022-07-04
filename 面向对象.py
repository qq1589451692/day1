#类：是对现实生活中一类具有共同特征的事物的抽象。类是具有一组相同或者相似特征和行为的一系列对象的集合   类相当于造汽车的图纸，造出的车相当于对象
# 对象：类的实例化可以得到一个对象，对象就具备了类的属性和方法
#类由三部分组成：名称、属性和方法   例如：类（人类） 名称（小明）、属性（身高、年龄）、方法（学习、吃饭）
class Person:
    '''
    对应人的特征
    '''
    name="小公"
    age=20
    '''
    对应人的行为
    '''
    def eat(self):
        print('大口吃饭')
    def run(self):
        print('飞快的跑')
# 创建一个对象(类的实例化)
xm=Person()
xm.eat()  #调用函数
print("{}的年龄是{}".format(xm.name,xm.age))

# 实例方法：在类的内部，使用def关键字来定义，第一个参数默认是self（名字标识可以是其他的名字，但是这个位置必须被占用）
# 实例方法是归于类的实例所有
# 类属性：在类的内部定义的变量
# 实例属性：在方法内部定义的变量，且用self.变量名引用
