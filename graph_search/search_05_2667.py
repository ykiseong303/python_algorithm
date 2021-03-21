'''
분류 : DFS & BFS
문제 : 단지번호붙이기 (백준 2667)
작성일자 : 2021.03.21
'''

# 목적 : 연결되어 있는 집을 방문하고, 연결요소의 수와 각 연결요소의 집 갯수를 출력
# 접근 : DFS 혹은 BFS를 이용한다 
#       집의 개수를 세기 위해서 전역변수를 설정한다 
from collections import deque

# BFS를 이용한 방법
def bfs (a,b) : 
    global house 
    if shape[a][b] == 1 : 
        shape[a][b] = 0
        house += 1
        queue = deque([(a,b)])
        while queue : 
            x, y = queue.popleft()
            for i in range(4) : 
                nx = x + dx[i]
                ny = y + dy[i]
                if nx<0 or ny<0 or nx>=N or ny>=N : 
                    continue
                if shape[nx][ny] == 1 : 
                    shape[nx][ny] = 0 
                    house += 1 
                    queue.append((nx,ny))

        return True 
    else : 
        return False 


def dfs (x,y) : 
    global house # 집의 개수를 세기 위한 전역변수 선언
    if x<0 or x>=N or y<0 or y >= N: 
        # 범위를 초과하면 무시하기
        return 
    if shape[x][y] == 1 : 
        # 현재 값을 -1로 변경(방문함을 표현) 
        shape[x][y] = 0 
        house += 1 
        # print(house)
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        #answer.append(house)
        return True
    else : 
        # 이미 방문하거나 길이 아니라면 False
        return False 

# 커맨드를 이용한 방법
def dfs_c (x,y) : 
    global house
    if shape[x][y] == 1 : 
        house += 1
        shape[x][y] = 0 
        for i in range(4) : 
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or nx>=N or ny<0 or ny>=N :
                continue
            if shape[nx][ny] == 1 : 
                dfs_c(nx,ny)
        return True
    else : 
        return False 

N = int(input())
shape = []
count = 0 
house = 0
answer = []
dx = [-1,1,0,0]
dy = [0,0,-1,1]
for _ in range(N) :
    shape.append(list(map(int, input())))
for i in range(N) : 
    for j in range(N) : 
        if bfs(i,j) == True : 
            count += 1
            answer.append(house)
            house = 0
            # print(house)
print(count)
for h in sorted(answer) : 
    print(h)