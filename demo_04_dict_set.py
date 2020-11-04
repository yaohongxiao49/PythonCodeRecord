# -*- coding: utf-8 -*-
###################### 可变字典 ######################
mutableDic = {"a":1, "b":2}
# print("a == %s, %s" % (mutableDic["a"], mutableDic.get("a")))

# 判断可变字典中是否存在key为"a"
if "a" in mutableDic:
    print("key a 存在")

# 移除可变数字典指定key
mutableDic.pop("a")
# print("移除可变字典 == %s" % mutableDic)

###################### set ######################
s = set([1, 2, 3])
s.add(4)
s.remove(4)
# print("s == %s" % s)