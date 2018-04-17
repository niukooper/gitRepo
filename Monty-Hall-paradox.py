'''
条件：三扇门；两扇门里面有羊，另外一个是大奖
第一步 ：先假定出car大奖的位置
第二步 ：玩家自己从三个门里面选择一个门
第三步 ：主持人打开除了玩家选择的另外两扇门中的其中一扇,打开其中一扇有羊的门
第四步 ：主持人打开有羊的一扇门，然后玩家选择是否更改自己的选择；
        1.玩家不更改自己的选择。
        2.玩家更改自己的选择。
第五步 ：判定结果：
                1.玩家赢的汽车。
                2.玩家没有赢得汽车
第六步 ：统计数据；
                1.总共进行的模拟次数
                2.玩家不调换位置赢得汽车的次数
                3.玩家不调换位置的胜率
                4.玩家调换位置赢得汽车的次数
                5.玩家调换位置赢得汽车的胜率'''


import random


n = int(input())
total = n
switch = 0
switch_win = 0
stay = 0
stay_win = 0


for i in range(n):
    car = random.randint(0, 2)
    your_answer = random.randint(0, 2)
    change = random.choice([True, False])
    if change:
        switch += 1
        if car != your_answer:
            switch_win += 1

    else:
        stay += 1
        if car == your_answer:
            stay_win += 1


print('total = ', total)
print('switch = ', switch)
print('switch_win = %d, %.2f' % (switch_win, switch_win/switch * 100))
print('stay = ', stay)
print('stay_win = %d, %.2f' % (stay, stay_win/stay*100))