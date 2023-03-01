# https://www.acmicpc.net/problem/1074

# 다른 사람의 아이디어를 참고해서 해결한 문제
# 처음에는 재귀를 이용해서 전부 탐색하려고 했다.
# 이렇게 되면 시간초과가 일어나고 구현하는 것도 힘들었다.
# 구글링을 통해 재귀가 아닌 분할정복 이용이라는 힌트를 얻었고
# 시간 초과가 일어나지 않고 해결 할 수 있었다.


n,r,c = map(int,input().split())

def funz(r,c,n):
    global cnt
    while n != 0:
        n -= 1
        size = 2**n
        if c < size and r < size: # 2사분면
            cnt += 0
        elif size <= c and r < size: # 1사분면
            cnt += size**2
            c-=size
        elif c < size and size <= r: # 4사분면
            cnt += (size**2)*2
            r-=size
        elif size <= c and size <= r: #2 3사분면
            cnt += (size**2)*3
            r-=size
            c-=size
cnt = 0
funz(r,c,n)
print(cnt)
        


