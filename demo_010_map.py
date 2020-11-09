# -*- coding: utf-8 -*-
from functools import reduce
####################### 高阶函数 ######################
# map与list组合使用
def f(x):
   return x * x
r = map(f, [1, 2, 3, 4, 5])
print("map == %s" % list(r))

# reduce(累计)
def add(x, y):
    return x + y
count = reduce(add, [1, 2, 3, 4])
print("reduce == %s" % count)