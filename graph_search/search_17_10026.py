'''
분류 : DFS & BFS
문제 : 적록색약 (백준 10026)
작성일자 : 2021.03.27
'''

# 목적 : 정상인과 적록색약인 경우의 연결요소 수를 각각 출력한다 
# 접근 : 정상인의 map을 만들고, 이를 적록색약인 경우로 하나 더 만들어서 탐색을 돌린다
#       적록색약인 경우는 R > G 혹은 G > R로 바꾼다 
import sys 
import copy
from collections import deque

def bfs(i,j,target) : 
    if shape[i][j] == target : 
        shape[i][j] = 0 
        queue = deque([(i,j)])
        while queue : 
            x, y = queue.popleft()
            for i in range(4) : 
                nx, ny = x + dx[i], y + dy[i]
                if (0<=nx<N and 0<=ny<N) and shape[nx][ny] == target : 
                    shape[nx][ny] = 0 
                    queue.append((nx, ny))
        return True 
    else : 
        return False 

def bfs_1 (i,j, target) : 
    if shape_1[i][j] == target : 
        shape_1[i][j] = 0 
        q = deque([(i,j)])
        while q : 
            x, y = q.popleft()
            for i in range(4) : 
                nx, ny = x + dx[i], y + dy[i]
                if (0<=nx<N and 0<=ny<N) and shape_1[nx][ny] == target : 
                    shape_1[nx][ny] = 0
                    q.append((nx,ny))
        return True 
    else : 
        return False        

N = int(input())
shape = [list(sys.stdin.readline().rstrip())for _ in range(N)]
# 적록색약의 map을 생성
shape_1 = copy.deepcopy(shape)
for i in range(N) : 
    for j in range(N) : 
        if shape[i][j] == 'G' : 
            shape_1[i][j] = 'R' 
lst1 = ['R','G','B']
# lst2 = ['R','B']
dx = [-1,1,0,0]
dy = [0,0,-1,1]
ans = []
count,count_1 = 0,0
# 정상인의 경우 연결요소의 수를 출력
for l in lst1 : 
    for i in range(N) : 
        for j in range(N) : 
            if bfs(i,j,l) == True : 
                count += 1
            if bfs_1(i,j,l) == True : 
                count_1 += 1
ans.append(count)
ans.append(count_1)
print(*ans)

