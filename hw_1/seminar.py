num = int(input(': '))
first = 0
second = 1
counter = 2
while second <= num:
    if second == num:
        print(counter)
        break
    first, second = second, first + second
    counter+=1
else:
    print(-1)

#-------------------------------------------------------------------------------------

# n = int(input('Введите число: '))
# first = 0
# second = 1
# my_list = [first, second]
# for i in range (n-1):
#     sum = first-second
#     first = second
#     second = sum
#     my_list.append(sum)
# my_list = my_list[::-1]
# first = 0
# second = 1
# my_list.append(second)
# for i in range (n-1):
#     sum = first+second
#     first = second
#     second = sum
#     my_list.append(sum)
# print(my_list)    


# Уставшие от необычно теплой зимы, жители решили узнать, 
# действительно ли это самая длинная оттепель за всю историю 
# наблюдений за погодой. Они обратились к синоптикам, 
# а те, в свою очередь, занялись исследованиями статистики за прошлые годы. 
# Их интересует, сколько дней длилась самая длинная оттепель. 
# Оттепелью они называют период, в который среднесуточная температура ежедневно 
# превышала 0 градусов Цельсия. Напишите программу, помогающую синоптикам в работе.
# Пользователь вводит число N – общее количество рассматриваемых дней 
# (1 ≤ N ≤ 100). В следующих строках располагается N целых чисел. 
# Каждое число – среднесуточная температура в соответствующий день. 
# Температуры – целые числа и лежат в диапазоне от –50 до 50

# Input:    6 -> -20 30 -40 50 10 -10
# Output: 2
from random import randint

n = int(input("Enter number of days: "))
#temp = [int(input("Enter temperature for day {}: ".format(i + 1))) for i in range(n)]
temp = [randint(-50, 50) for i in range(n)]

max_warm_period = 0
current_warm_period = 0
for i in range(n):
    if temp[i] > 0:
        current_warm_period += 1
    else:
        if current_warm_period > max_warm_period:
            max_warm_period = current_warm_period
        current_warm_period = 0

if current_warm_period > max_warm_period:
    max_warm_period = current_warm_period

print(temp)
print("Longest warm period: {} days".format(max_warm_period))
