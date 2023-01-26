# https://www.acmicpc.net/problem/1655

# 다른 사람들의 아이디어를 참고해서 해결한 문제
# 아이디어를 어떻게 생각해내야 할까?
# 우선 시간제한이 짧고 n이 100,000이하이므로 시간복잡도 O(nlogn)이내의 해결법을 찾아야한다.
# 항상 중간값을 찾아야하므로 정렬 알고리즘이 필요할 것이고 삽입할때마 정렬 되어야 하므로
# 힙정렬을 이용해야함을 알 수 있음 하지만 나는 힙을 사용해야 할것이라고 생각은 들었지만
# 최대힙 최소힙으로 나눠서 풀어야한다는 것까지는 접근하지 못함
# 나는 중간값을 찾을때 정렬을 한 후 리스트 길이/2를 통해 접근하려고만 생각했기 때문이다.

# 알게된 점
# 힙 푸시와 팝은 O(logn)의 시간복잡도를 가진다.
# 힙을 생성할때(heapify)는 O(nlogn)의 시간복잡도를 가진다.

import sys
import heapq

leftheap = [] #최대 힙
rightheap = [] #최소 힙

n = int(input())

for i in range(n):
    num = int(sys.stdin.readline())

    if i == 0:
        heapq.heappush(leftheap,-num)
    else:
        if i%2 == 0:
            heapq.heappush(leftheap,-num)
        else:
            heapq.heappush(rightheap,num)

        if -leftheap[0] > rightheap[0]:
            a = heapq.heappop(leftheap)
            b = heapq.heappop(rightheap)

            heapq.heappush(leftheap,-b)
            heapq.heappush(rightheap,-a)

    print(-leftheap[0])

    