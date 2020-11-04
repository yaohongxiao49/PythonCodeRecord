# -*- coding: utf-8 -*-
####################### 切片 ######################
arr = ["1", "2", "3", "4", "5", "6"]
appendArr = []
count = 3
for i in range(count):
    appendArr.append(arr[i])
print("正常取前三个元素 == %s" % ([arr[0], arr[1], arr[2]]))
print("循环取三个元素 == %s" % appendArr)
print("正序切片取三个元素 == %s, %s" % (arr[0:3], arr[:3]))
print("倒序切片取三个元素 == %s" % arr[-3:])
print("每两个取数 == %s" % arr[0:4:2])