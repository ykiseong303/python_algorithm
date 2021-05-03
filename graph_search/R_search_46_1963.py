'''
분류 : DFS & BFS
문제 : 소수경로 (백준 1963)
작성일자 : 2021.05.03
'''

# 목적 : A>B로 가기 위한 최소 연산횟수(모두 소수여야함)
# 접근 : 최소연산횟수이므로 현재 값에서 bfs를 수행하며 목적지 찾기
# 구현 : 1. 소수찾기
#          > 에라토스테네스의 체를 활용하여 주어진 범위까지의 모든 소수를 check
#          > 최대 범위의 루트값이(**0.5)이 최대 약수이므로 여기까지 검사 
#          > 소수인 값에서 배수들을 모두 소수가 아님으로 체크한다
#       2. 각 자리수 이동하기
#          > 리스트로 접근하지 않고, 점화식으로 구현
#          > 각 자리수의 값을 단위값씩 증가시키면 되므로 그 자리의 값을 0으로 변환
#          > n = num(원래 수) - num%(i*10) // i * i
#          > num을 i*10으로 나머지연산하면 구해야할 자리수 값이 나오고
#          > 그 수에서 구하려는 자리값외의 숫자는 필요없으므로 다시 i로 나누어서 몫을 구하고
#          > 단위만큼 곱해줌
#          1033 - 1033%(10*10) // 10 * 10 
#          1033 % (100) = 33
#          33 // 10 = 3, 3 * 10 = 30
#          1033 - 30 = 1003 (10의 자리가 0으로 변환됌)

import sys 
from collections import deque 
sys.setrecursionlimit(10000)
input = sys.stdin.readline

prime = [0]*10001
for i in range(2,101) : # 최대범위의 루트까지만 체크
    if prime[i] == 0 : 
        # prime[i] = 1
        j = i * 2 
        while j < 10001 : 
            prime[j] = 1
            j += i # 배수를 모두 소수아님으로 체크함

def bfs(s) : 
    visit = [0] * 10001
    visit[s] = 1
    q = deque([(s,0)])
    while q :
        num, cnt = q.popleft()
        # print(num,cnt)
        if num == b : return cnt
        if num < 1000 : continue # continue는 while에서도 사용 가능
        for i in [1,10,100,1000] : 
            n = num - num%(i*10)//i*i # 단위별 변환을 위한 점화식
            for j in range(10) : 
                # 0~9까지 반복하며 
                # 방문한적이 없고, 소수라면
                if visit[n] == 0 and prime[n] == 0 : 
                    visit[n] = 1
                    q.append((n,cnt+1))
                n += i # 현재 값에 단위값만큼 더해줌
                # 1003 > 1013 > 1023 > 1033 ... (단위값이 10인경우)
    print("Impossible")

T = int(input())
for _ in range(T) : 
    a, b = map(int, input().split())
    print(bfs(a))
