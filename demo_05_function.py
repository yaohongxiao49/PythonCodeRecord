# -*- coding: utf-8 -*-
####################### 函数 ######################
# 绝对值函数 abs()，只能传入一个整形
i = -1
# print("常数 == %s, 绝对值 = %s" % (i, abs(i)))

# 最大函数 max()
arr = (1, 2, 3)
# print("最大值 == %d" % max(arr))

####################### 自定义函数 ######################
def test1(x):
    if x >= 0:
        return x
    else:
        return -x
# print(test1(-99))

# ininstance用于判定、约束参数的类型
def test2(x):
    if not isinstance(x, (float, int)):
        raise TypeError("bad oprand type")
    if x >= 0:
        return x
    else:
        return -x
# print(test2("d"))

# 多参数
def test3(x, y):
    xy = x + y
    yx = x * y
    return xy, yx
# print(test3(10, 10))

# 默认参数（只有多参数可使用，并且设置的默认参数必须在后）
def test4(x, y = 10):
    xy = x + y
    yx = x * y
    return xy, yx
# print(test4(10))

def test5(L=None):
    if L is None:
        L = []
    L.append("end")
    return L
# print(test5())

# 可变参数(参数前带 * 标识可变参数，list、tuple都可用)
mutableArr = [1, 2, 3]
def mutableValue(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
# print("mutableValue == %s" % mutableValue(1, 2, 3))
# print("mutableArr == %s" % mutableValue(*mutableArr))

# **表示关键字参数，接收的是dict
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)
# person("1", 2)
# person("1", 2, city = "sf")

# 限制关键字参数名称 * 后的视为命名关键字参数
def personLimit(name, age, *, city, job):
    print(name, age, city, job)
personLimit("1", 2, city="成都", job="无")

####################### 函数中写pass，可代表占位方法 ######################
def nop():
    pass