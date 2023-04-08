# https://www.acmicpc.net/problem/11403

"""
플로이드 워셜 알고리즘을 응용해서 해결 할 수 있었던 문제
새로 알아간것은 자기자신에 출발해서 자기자신으로 돌아가는 부분은 거리가 주어질때 음수만 아니면 다른 부분에 영향을 안미친다.
"".join()의 경우 매개변수로 iterable한 객체가 들어가야 되고 ""안에는 구분자를 넣어준다 _를 넣으면 중간에 원소 중간중간에 _를 넣어 반환
"""

import sys
from pprint import pprint

n = int(input())
graph = [sys.stdin.readline().split() for _ in range(n)]

for k in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][k] == '1' and graph[k][j] == '1':
                graph[i][j] = '1'

for i in range(n):
    print(" ".join(graph[i]))
