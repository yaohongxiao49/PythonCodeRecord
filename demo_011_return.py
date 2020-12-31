# -*- coding: utf-8 -*-
####################### 函数式返回 ######################
def cals_num(*arg):
    x = 0
    for v in arg:
        x = x + v    
    return x
print("正常求和 == %s" % cals_num(1, 2, 3))

def lazy_sum(*arg):
    def sum():
        x = 0
        for v in arg:
            x = x + v        
        return x
    return sum
l = lazy_sum(1, 2, 3)
print("函数式求和 == %s" % l())