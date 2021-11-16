# 海伦公式计算三角形面积

# 定义变量
a = b = c = 0.0
flag = 1

# 判断是否为三角形
while flag:
    a = float(input("输入第一条边长："))
    b = float(input("输入第二条边长："))
    c = float(input("输入第二条边长："))
    if a + b > c and a + c > b and b + c > a:
        flag = 0
        break
    else:
        print("输入边长不构成三角形，请重新输入！")

# 计算面积
l = (a + b +c) / 2
s = (l * (l - a) * (l - b) * (l - c)) ** 0.5
print('三角形的面积是：%0.2f'%s)