# -*- coding: utf-8 -*-
###################### 可变数组list ######################
mutableArr = ["1", 2, "3"]
# print("mutableArr == %s, len == %d" % (mutableArr, len(mutableArr)))

########### 取值（下标0，1，2正序，下标-1，-2，-3倒序） ##############
# print("1 == %s, 2 == %s, 3 == %s \n 3 == %s, 2 == %s, 1 == %s" % (mutableArr[0], mutableArr[1], mutableArr[2], mutableArr[-1], mutableArr[-2], mutableArr[-3]))

########### 插入值 ##############
mutableArr.append("4") #在末尾插入
mutableArr.insert(4, "5") #指定下标插入
# print("添加arr == %s" % mutableArr)

########### 移除值 ##############
mutableArr.pop() #移除末尾数
mutableArr.pop(3) #指定下标移除
# print("移除arr == %s" % mutableArr)

###################### 不可变数组tuple(元祖) ######################
arr = ("A", "B", "C")
# print(arr)

###################### 循环 ######################
# for value in mutableArr:
#     print(value)

sum = 0
n = 10
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)

# 作业：
# 创建一个包含1，2，3，6的可变数组，在3后插入4，移除6并添加5，得出结果为1，2，3，4，5的数组；
# 将可变数组中的3修改为3.5，循环打印出可变数组中含有的值；
# 计算数组中的数值之和，并打印出来；