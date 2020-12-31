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

# filter(过滤)
def is_add(x):
    return x %2 == 1
print("filter == %s" % list(filter(is_add, [1, 2, 3, 4, 5])))

# 排空过滤
def not_empty(s):
    return s and s.strip()
print("notEmpty == %s" % list(filter(not_empty, ["1", "", "3", "", "5"])))

# 排序
print("排序 == %s" % sorted([1, 5, 6, 3, 2, -4]))
print("绝对值排序 == %s" % sorted([1, 5, 6, 3, 2, -4], key=abs))
print("区分大小写排序 == %s" % sorted(["A", "a", "B", "b", "c", "C"]))
print("不区分大小写排序 == %s" % sorted(["A", "a", "B", "b", "c", "C"], key=str.lower))
print("不区分大小写排序，倒序 == %s" % sorted(["A", "a", "B", "b", "c", "C"], key=str.lower, reverse=True))