'''
분류 : DFS & BFS
문제 : 숨바꼭질 (백준 1697)
작성일자 : 2021.06.01
'''

# 목적 : N > K가 되는 최소 연산횟수 출력
# 접근 : 현재위치에서 증가하는 연산은 입력의 최대한계까지, 감소하는 연산은 0이상까지 
#       bfs를 수행 
#       불필요한 메모리, 시간효율성을 위해 연산한 값이 목표값에 도달하는지를 먼저 계산하고
#       도달하지 못하는 경우만 큐에 삽입

from collections import deque 

def bfs(N) : 
    visit[N] = 1
    q = deque([(N,0)])
    while q : 
        x, depth = q.popleft()
        # print(x)
        if x == K : 
            return depth 
        if x+1 == K : return depth + 1
        elif x+1<=100000 and visit[x+1] == 0 : 
            visit[x+1] = 1
            q.append((x+1,depth+1))
        if x-1 == K : return depth + 1
        elif x-1>=0 and visit[x-1] == 0 : 
            visit[x-1] = 1
            q.append((x-1,depth+1))
        if x*2 == K : return depth + 1
        elif x*2<=100000 and visit[x*2] == 0 : 
            visit[x*2] = 1
            q.append((x*2,depth+1))



N, K = map(int, input().split())
visit = [0] * 100001
print(bfs(N))