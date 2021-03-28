'''
분류 : DFS & BFS
문제 : 나이트의 이동 (백준 7562)
작성일자 : 2021.03.28
'''

# 목적 : 나이트가 목표위치로 도달할 수 있는 최소 이동횟수
# 접근 : 8방향에 대해 방문기록을 남기며, 목표위치에 도달하면 탐색을 중단한다
#       처음에는 백트래킹으로 생각을 했는데 가능은 하겠지만, 방문기록을 남기는 것이 더 효ㅕ율적
#       왜냐하면 직전 나이트가 이동한 곳은 이후의 나이트도 도착할 수 있기 때문에
#       직전나이트가 1번이라도 더 빨리 가서 도달하면 되기 때문이다

import sys 
from collections import deque

def bfs(i,j) : 
    global ans
    q = deque([(i,j,0)])
    while q : 
        x,y,cnt = q.popleft()
        if x == t_x and y == t_y : 
            ans = cnt
            # ans.append(cnt)
            break
        for a in range(8) : 
            nx, ny = x +dx[a], y+dy[a]
            # print(nx,ny)
            if (0<=nx<N and 0<=ny<N) and shape[nx][ny] == 0 : 
                shape[nx][ny] = 1
                q.append((nx,ny,cnt+1))

T = int(input())
dx = [-1,-2,-2,-1,1,2,2,1]
dy = [-2,-1,1,2,-2,-1,1,2]
index = 0
for _ in range(T) : 
    N = int(input())
    shape = [[0]*(N) for _ in range(N)]
    x, y = map(int, input().split())
    t_x, t_y = map(int, input().split())
    shape[x][y] = 1
    ans = []
    bfs(x,y)
    print(ans, end=' ')
# print(*ans)