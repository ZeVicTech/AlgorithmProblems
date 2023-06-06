# https://www.acmicpc.net/problem/10816

import sys
input = sys.stdin.readline

n = int(input())

cards = list(map(int,input().split()))

hash_table = {}

for card in cards:
    if card not in hash_table.keys():
        hash_table[card] = 1
    else:
        hash_table[card] += 1

m = int(input())

number = list(map(int,input().split()))

for num in number:
    if num in hash_table.keys():
        print(hash_table[num], end = ' ')
    else:
        print(0, end = ' ')
