'''
분류 : DFS & BFS
문제 : 연결요소의 개수 (백준 11724)
작성일자 : 2021.06.01
'''

# 목적 : 연결요소의 개수를 출력
# 접근 : 간선에 연결된 정점의 정보가 주어진 경우, 이를 인접행렬로 표현
#       실제 정점은 1차원 리스트이므로, 방문처리할 리스트도 1차원이고,
#       탐색을 이어갈때도 1차원으로 진행될 수 있게 해야함

import sys 
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

def dfs(x) : 
    visit[x] = 1
    for i in range(1,N+1) : 
        if shape[x][i] == 1 and visit[i] == 0 : 
            dfs(i)

N, M = map(int, input().split())
shape =[[0] * (N+1) for _ in range(N+1)]
visit = [0] * (N+1)
for _ in range(M) : 
    x, y = map(int, input().split())
    shape[x][y] = 1 
    shape[y][x] = 1 
cnt = 0

for i in range(1,N+1) : 
    if visit[i] == 0 : 
        dfs(i)
        cnt += 1
print(cnt)