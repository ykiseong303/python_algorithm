'''
분류 : DFS & BFS
문제 : 토마토 (백준 7569)
작성일자 : 2021.03.27
'''

# 목적 : 토마토가 모두 익는데 걸리는 최소시간
# 접근 : 사방으로 퍼지는 경우 모든 영역을 도달하는데 걸리는 최소 시간이므로 bfs를 이용
#       3차원 리스트를 생각
#       최댓값과 최솟값을 찾는 경우를 그냥 정석적인 방법으로

import sys 
from collections import deque

def bfs(q) : 
    while q : 
        z, x, y = q.popleft()
        for i in range(6) : 
            nz, nx, ny = z + dz[i], x+dx[i], y+dy[i]
            if (0<=nx<N and 0<=ny<M and 0<=nz<H) and shape[nz][nx][ny] == 0 :
                shape[nz][nx][ny] = shape[z][x][y] + 1
                q.append((nz,nx,ny))

M, N, H = map(int, input().split())
shape = [] 
queue = deque()
dx = [-1,1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dz = [0,0,0,0,-1,1]
# shape의 입력을 3차원으로 입력받음
# z, x, y 순으로
for _ in range(H) : 
    temp = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
    shape.append(temp)
    temp = []
# 익은 토마토가 있는 좌표만 큐에 넣기
for h in range(H) : 
    for i in range(N) : 
        for j in range(M) : 
            if shape[h][i][j] == 1 : 
                queue.append((h,i,j))
bfs(queue)
'''
print("\n")
for s in shape : 
    for a in s : 
        print(*a)
'''
# bfs 수행 후 max 값을 찾기 
z = 1 
result = -1 
for i in shape : 
    for j in i : 
        for k in j :
            if k == 0 :
                z = 0
            result = max(result,k)
if z == 0 :
    print(-1)
elif result == 1 :
    print(0)
else :
    print(result-1)

'''
max_result = max((max(map(max, shape))))-1
if 0 in shape : 
    print("yes")
for s in shape : 
    print(s)
    for a in s : 
        if 0 in a : 
            print(a)
            max_result = -1
print(max_result)
'''
# print(max_result)
# print(shape[0][2][4])