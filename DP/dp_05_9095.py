'''
분류 : 다이나믹 프로그래밍
문제 : 1,2,3 더하기 (이코테 백준 9095)
작성일자 : 2021.05.30
'''

# 목적 : 입력받은 N을 1,2,3의 합으로 나타낼 수 있는 모든 경우의 수를 출력
# 접근 : bfs or DP
#   bfs : 1부터 시작해서 3가지 연산을 수행하며 모든 노드를 확인, 목표에 도달할 때마다 cnt증가
#         모든 경우를 확인해야 하므로 방문처리 x
#   DP : N이 3이상이면 d[i-1] + d[i-2] + d[i-3]의 규칙을 가짐

T = int(input())
for _ in range(T) : 
    N = int(input())
    d = [0] * 12
    d[1] = 1
    d[2] = 2
    d[3] = 4
    if N < 4 : 
        print(d[N])
    else : 
        for i in range(4,N+1) : 
            d[i] = d[i-1]+d[i-2]+d[i-3]
        print(d[N])
'''import sys 
from collections import deque 

def bfs(i) : 
    global cnt
    q = deque([(i)])
    while q : 
        x = q.popleft()
         # print(x)
        if x == N : 
            cnt += 1
            # print("cnt",cnt)
            continue
            
        if x+1 <=N : 
            q.append((x+1))
        if x+2<=N : 
            q.append((x+2))
        if x+3 <=N : 
            q.append((x+3))
    
T = int(input())
cnt = 0
for _ in range(T) : 
    N = int(input())
    for i in range(1,4) : 
        bfs(i)
    print(cnt)
    cnt = 0'''