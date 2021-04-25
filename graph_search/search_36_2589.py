'''
분류 : DFS & BFS
문제 : 보물섬 (백준 2589)
작성일자 : 2021.04.25
'''

# 목적 : 보물이 묻힌 두 곳사이의 최단 거리 시간 출력
# 접근 : bfs탐색, 브루트포스
#       각각의 위치에서의 최단경로 시간이 다르므로 완전탐색을 수행한다


import sys
from collections import deque
input = sys.stdin.readline

def bfs(x1,y1) :
    global ans
    if shape[x1][y1] == 'L' : 
        # shape[x1][y1] = 'W'
        visit[x1][y1] = 1
        q = deque([(x1,y1)])
        while q :
            x, y = q.popleft()
            for i in range(4) : 
                nx, ny = x+dx[i], y+dy[i]
                if (0<=nx<N and 0<=ny<M) and visit[nx][ny] == 0 : 
                    if shape[nx][ny] == 'L' : 
                        visit[nx][ny] = visit[x][y] + 1
                        q.append((nx, ny))
                        ans = max(ans, visit[nx][ny])
            # print("\n")
            # for v in visit : 
            #     print(*v)
        return True
    else : 
        return False

N, M = map(int, input().split())
shape = [list(input().strip())for _ in range(N)]
dx, dy = [-1,1,0,0], [0,0,-1,1]
visit = [[0]*M for _ in range(N)]
ans = 0
max_val = 0
for i in range(N) : 
    for j in range(M) : 
        if bfs(i,j) == True : 
            max_val = max(max_val, ans)
            visit = [[0]*M for _ in range(N)]
            ans = 0
print(max_val-1)