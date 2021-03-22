'''
분류 : DFS & BFS
문제 : 토마토 (백준 7576)
작성일자 : 2021.03.22
'''

# 목적 : 토마토가 다 익는데 걸리는 최소 일수
# 접근 : 기준 노드로부터 인접한 노드가 모두 1이 될때까지 진행해야 하므로 BFS를 이용한다
#       최단 거리를 구하는 것과 동일하다 (기준노드에서 끝까지 갈 수 있는 최소시간)
#       지금까지는 matrix 자체를 하나씩 대조해가며 체크했는데, 이 문제에서는 
#       기준이 되는 노드가 동시에 발생하므로 (이런점에서 bfs를 사용해야한다) 1인 부분만
#       큐에 넣고 그 큐를 bfs를 조건에 맞게 돌리면 된다 
from collections import deque
import sys

def bfs(lst) : 
    while lst :
        x, y = lst.popleft() 
        for i in range(4) : 
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or ny<0 or nx>=N or ny>=M : 
                continue
            if shape[nx][ny] == 0 : 
                shape[nx][ny] = shape[x][y] + 1 
                lst.append((nx,ny))


M, N = map(int, input().split())
shape = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
lst = deque()
dx = [-1,1,0,0]
dy = [0,0,-1,1]

for i in range(N) : 
    for j in range(M) :
        if shape[i][j] == 1 : 
            lst.append((i,j))
bfs(lst)
max_ans = max(map(max, shape))
for s in shape : 
    if 0 in s : 
        print(-1)
        sys.exit()
if max_ans == 1 : 
    print(0)
else : 
    print(max_ans-1)
    

'''

def bfs(i,j) : 
    global index 
    if shape[i][j] == -1 or shape[i][j] == 0 :
        return 
    elif shape[i][j] == index : 
        # print("yes")
        # queue = deque([(i,j)])
        # x,y = queue.popleft()
        for k in range(4) : 
            nx = i + dx[k]
            ny = j + dy[k]
            if nx<0 or ny<0 or nx>=M or ny>=N : 
                # print("continue",nx,ny,index)
                continue
            if shape[nx][ny] == 0 : 
                # print(nx,ny)
                shape[nx][ny] = shape[i][j] + 1
        return     




N, M = map(int, input().split())
shape = []
dx = [-1,1,0,0]
dy = [0,0,-1,1]
for _ in range(M) : 
    shape.append(list(map(int, input().split())))
index = 1
while index < N*M : 
    for i in range(M) : 
        for j in range(N) : 
            # print(i,j)
            bfs(i,j)
    index += 1 
mix_shape = min(map(min, shape))
max_shape = max(map(max, shape))
for s in shape : 
    if 0 in s : 
        print(0)
        sys.exit()
    else : 
        if max_shape == 1 : 
            print(0)
            sys.exit()
        else : 
            print(max_shape-1)
            sys.exit()
# print("\n")
# for s in shape : 
#     print(*s)

'''