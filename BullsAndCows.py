# 猜数字

from operator import truediv
import random

# 产生1~100随机数
anwser = random.randint(1,100)
counter = 0
while True:
    number = int(input('请输入：'))
    counter += 1
    if anwser > number:
        print('大一点')
    elif anwser < number:
        print('小一点')
    else:
        print('恭喜你，猜对了！')
        break
print('你共猜了%d次!'%counter)
