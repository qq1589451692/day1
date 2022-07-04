# 将以下列表升序排序
lista = [66, 46, 50,35, 6,20]
# 思路：先将第一个数和第二个数做比较，大的放后面
if lista[0] > lista[1]:
    lista[0],lista[1] = lista[1],lista[0]
print(lista)

# 将第二个和第三个数做比较，大的放后面
if lista[1] > lista[2]:
    lista[1],lista[2] = lista[2],lista[1]
print(lista)

# 将第三个和第四个数做比较，大的放后面
if lista[2] > lista[3]:
    lista[2],lista[3] = lista[3],lista[2]
print(lista)

# 将第四个和第五个数做比较，大的放后面
if lista[3] > lista[4]:
    lista[3],lista[4] = lista[4],lista[3]
print(lista)

# 将第五个和第六个数做比较，大的放后面
if lista[4] > lista[5]:
    lista[4],lista[5] = lista[5],lista[4]
print(lista)

print('****************第一次for循环*******************')
# 重复比较了len(lista)-1次，将最大的数移到了最后面，找寻到规律，可以写出如下循环语句
lista = [66, 46, 50,35, 6,20]
for i in range(len(lista)-1):
    if lista[i] > lista[i+1]:
        lista[i], lista[i+1] = lista[i+1], lista[i]
    print(lista)

print('****************第二次for循环*******************')
# 再重新将排序后的第一个数和后面的数依次比较，将第二大的数移到倒数第二位，也可以写出如下for循环
for i in range(len(lista)-2):   # 下标-2是因为前面已经把最大的移到最后面了，这里只是找第二大的数移到倒数第二，再去和最后一个数比较没有意义
    if lista[i] > lista[i+1]:
        lista[i], lista[i+1] = lista[i+1], lista[i]
    print(lista)

print('****************第三次for循环*******************')
for i in range(len(lista)-3):  #下标-3的意思同上，再去跟最大的数和第二大的数比较没有意义
    if lista[i] > lista[i+1]:
        lista[i], lista[i+1] = lista[i+1], lista[i]
    print(lista)

print('****************第四次for循环*******************')
for i in range(len(lista)-4):  #下标-4的意思同上
    if lista[i] > lista[i+1]:
        lista[i], lista[i+1] = lista[i+1], lista[i]
    print(lista)

print('****************第五次for循环*******************')
for i in range(len(lista)-5):  #下标-5的意思同上
    if lista[i] > lista[i+1]:
        lista[i], lista[i+1] = lista[i+1], lista[i]
    print(lista)

print('***********************************************')
# 经历了五个for循环，将该列表升序排好，可以写出如下for循环嵌套
lista = [66, 46, 50,35, 6,20]
for j in range(len(lista)-1):  #控制下面的for循环执行次数为五次
    for i in range(len(lista) - 1):  #控制下面的if语句执行五次   if语句执行5*5次，排序完成
        if lista[i] > lista[i + 1]:
            lista[i], lista[i + 1] = lista[i + 1], lista[i]
print(lista)

# 最终优化
lista = [66, 46, 50,35, 6,20]
for j in range(1,len(lista)):  #从1开始，不包含6，还是执行4次
    for i in range(len(lista) -j):  #第一次下标减1，不和已经排到最后的最大的数做比较，第二次下标减2，不和已经排到后面的第一第二大的数做比较。。。。。
                                    #最终只需要执行15次if语句就能排好
        if lista[i] > lista[i + 1]:
            lista[i], lista[i + 1] = lista[i + 1], lista[i]
print(lista)