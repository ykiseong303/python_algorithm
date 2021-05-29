'''
분류 : DFS & BFS
문제 : DFS와 BFS (백준 1260)
작성일자 : 2021.05.30
'''

# 목적 : 입력받은 그래프를 DFS와 BFS로 탐색한 결과를 출력한다
# 접근 : 각 정점에 연결된 간선이 정보로 주어지는 경우, 인접행렬로 정점간의 연결관계를 표시한다
#       시작할 노드(행기준)부터 순차적으로 연결된 정점(열기준)을 탐색한다

import sys
from collections import deque
sys.setrecursionlimit(100000)

def dfs(x) : 
    print(x,end=' ')
    visit[x] = 1
    for i in range(1,N+1) : 
        if shape[x][i] == 1 and visit[i] == 0 : 
                dfs(i)
def bfs(x) : 
    q = deque([(x)])
    visit[x] = 1 
    print(x, end=' ')
    while q : 
        x = q.popleft()
        for i in range(1,N+1) : 
            if shape[x][i] == 1 and visit[i] == 0 : 
                print(i,end=' ')
                visit[i] = 1 
                q.append((i))
N, M, V = map(int, input().split())
shape = [[0]*(N+1) for _ in range(N+1)]
for _ in range(M) : 
    x, y = map(int, input().split())
    shape[x][y] = 1
    shape[y][x] = 1 
visit = [0] * (N+1)
dfs(V)
visit = [0] * (N+1)
print("")
bfs(V)