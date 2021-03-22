'''
분류 : DFS & BFS
문제 : 유기농 배추 (백준 1012)
작성일자 : 2021.03.22
'''

# 목적 : 연결 요소의 개수 출력
# 접근 : bfs와 dfs를 이용하여 연결요소를 구한다 
#       dfs로 구하면 recursive error가 뜨는데 이유를 모르겠음 


from collections import deque

def dfs(i,j) : 
    if shape[i][j] == 1 : 
        shape[i][j] = 2
        for k in range(4) : 
            nx = i + dx[k]
            ny = j + dy[k]
            if nx<0 or ny<0 or nx>=N or ny>=M : 
                continue
            if shape[nx][ny] == 0 : 
                continue
            if shape[nx][ny] == 1 : 
                dfs(nx,ny)
    
        return True
    else : 
        return False 
def bfs(i,j) : 
    if shape[i][j] == 1 : 
        shape[i][j] = 0 
        queue = deque([(i,j)])
        while queue : 
            x, y = queue.popleft()
            for i in range(4) : 
                nx = x + dx[i]
                ny = y + dy[i]
                if nx<0 or ny<0 or nx>=N or ny>=M : 
                    continue
                if shape[nx][ny] == 0 : 
                    continue
                if shape[nx][ny] == 1 :
                    queue.append((nx,ny)) 
                    shape[nx][ny] = 0
        return True 
    else : False 

T = int(input())
for _ in range(T) : 
    M, N, K = map(int ,input().split())
    shape = [[0 for _ in range(M)] for _ in range(N)]

    for i in range(K) : 
        x, y = map(int, input().split())
        shape[y][x] = 1


    count = 0
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    for i in range(N) : 
        for j in range(M) : 
            if bfs(i,j) == True : 
                count += 1
    print("\n")
    for s in shape : 
        print(*s)
    print(count)