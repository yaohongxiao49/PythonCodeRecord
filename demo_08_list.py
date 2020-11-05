# -*- coding: utf-8 -*-
import os # 导入os模块，模块的概念后面讲到
####################### 列表生成器 ######################
print("基础列表生成器 == %s" % list(range(2, 10)))

L = []
for x in range(2, 10):
    L.append(x * x)
print("正常循环计算 == %s" % L)
print("参数列表生成器 == %s" % [x * x for x in range(2, 10)])
print("加条件的列表生成器 == %s" % [x * x for x in range(2, 10) if x % 2 == 0])

# 两层循环嵌套
print("两层循环嵌套 == %s" % [x + y for x in range(1, 4) for y in range(2, 6)])
print([d for d in os.listdir('.')]) # os.listdir可以列出文件和目录