# https://www.acmicpc.net/problem/2108

import sys
input = sys.stdin.readline

n = int(input())
dic = {}
data = []

for i in range(n):
    num = int(input())

    if num in dic.keys(): 
        dic[num] += 1
    else:
        dic[num] = 1

    data.append(num)

data.sort()

temp = sorted(dic.items(), key = lambda x: x[1],reverse=True)

mode_list = []
max_num = temp[0][1]
for i in range(len(temp)):
    if temp[i][1] == max_num:
        mode_list.append(temp[i][0])
    else:
        break

if len(mode_list) == 1:
    mode_value = mode_list[0]
else:
    mode_value = mode_list[1]

mean_value = round(sum(data)/len(data))
median_value = data[len(data)//2]
range_value = data[-1]-data[0]

print(mean_value)
print(median_value)
print(mode_value)
print(range_value)