# https://www.acmicpc.net/problem/1181

import sys
n = int(sys.stdin.readline())
words = [sys.stdin.readline() for _ in range(n)]

words = list(set(words)) # 중복제거
words.sort() # 사전순으로 정렬
words.sort(key=len) # 길이 순으로 정렬

for word in words:
    print(word, end='')