# https://www.acmicpc.net/problem/1107

# 다른 사람의 아이디어를 참고해서 해결한 문제
# 브루트포스 문제인 것은 알아차렸고 탐색해야할 범위 또한 알았다.
# 하지만 100에서 + - 만으로 도달하는 수와 숫자를 조합해서 + - 도달하는 수를
# 어떻게 비교해야할지를 떠올리지 못했음
# 왜 떠올리지 못했을까?
# 100에서 출발한 케이스가 답이 되는 경우를 명확하게 인지하지 못해서 그런것 같다. 

from itertools import product

n = int(input())
m = int(input())
broken = []
if m != 0:
    broken += list(map(int,input().split()))

min_count = abs(100-n)

for i in range(1000001):
    nums = str(i)
    flag = 0
    for num in nums:
        if int(num) in broken:
            flag = 1
            break
    if flag == 0:
        min_count = min(len(nums) + abs(n-i),min_count)

print(min_count)