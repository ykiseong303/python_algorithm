'''
분류 : DFS & BFS
문제 : 음식물 피하기 (백준 1743)
작성일자 : 2021.04.28
'''

# 목적 : 가장 큰 음식물 크기 출력
# 접근 : 각 연결요소를 탐색하며 연결요소의 구성원을 count한다

import sys 
from collections import deque 
input = sys.stdin.readline

def bfs(x,y) : 
    global res
    if shape[x][y] == 1 : 
        shape[x][y] = 0 
        q = deque([(x,y)])
        res += 1
        while q : 
            x, y = q.popleft()
            for i in range(4) : 
                nx, ny = x+dx[i],y+dy[i]
                if (0<=nx<N and 0<=ny<M) and shape[nx][ny] == 1 :
                    shape[nx][ny] = 0
                    q.append((nx,ny))
                    res += 1 
        return True 
    else :
        return False 
N, M, K = map(int, input().split())
shape = [[0]*M for _ in range(N)]
dx, dy = [-1,1,0,0], [0,0,-1,1]
for _ in range(K) : 
    x, y = map(int, input().split())
    x, y = x-1, y-1
    shape[x][y] = 1
res = 0
max_val = 0
for i in range(N) : 
    for j in range(M) : 
        if bfs(i,j) == True : 
            max_val = max(max_val,res)
            res = 0 
print(max_val)