# -*- coding: utf-8 -*-
####################### 循环取值 ######################
dic = {'a': 1, 'b': 2, 'c': 3}
for key in dic:
    print("key == %s" % key)

for value in dic.values():
    print("value == %s" % value)

for key, value in dic.items():
    print("key == %s, value == %s" % (key, value))

for str in "ABC":
    print("str == %s" % str)

for i, value in enumerate(["A", "B", "C"]):
    print("index == %s, value == %s" % (i, value))

for i, value in [("A", 2), ("B", 4), ("C", 6)]:
    print("index == %s, value == %s" % (i, value))