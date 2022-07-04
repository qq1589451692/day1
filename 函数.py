# 可变参数
def sum(*args):
    '''
    累加和
    :param args:
    :return:
    '''
    result=0
    for i in args:
        result+=i
        pass
    print("result的累加和是%d"%result)
    pass

sum(1,2,3,4,5)