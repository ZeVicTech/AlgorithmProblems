n,k = map(int,input().split())
coins = []
dp = [0] * k+1
for _ in range(n):
    coins.append(int(input()))

print(n,k)