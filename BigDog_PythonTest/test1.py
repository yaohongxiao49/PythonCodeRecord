# 变量a = 6，变量b = 9，变量c = 3，请两两相比，并输入相对较大的数值
# a = 6
# b = 9
# c = 3
# if a<b:
#     if b<c:
#         print(c)
#     else:
#         print("b=%s"%b)
# elif a>b:
#     if a<c:
#         print(c)
#     else:
#         print(a)
# else:
#     if a>c:
#         print(c)
#     else:
#         print(a,b)
a = 6
b = 9
c = 3
if a > b and a > c:
    print("最大a == %s" % a)
elif a > b and a < c:
    print("最大c == %s" % c)
elif a < b and b < c:
    print ("最大c == %s" % c)
else:
    print ("最大b == %s" % b)