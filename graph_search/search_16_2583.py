'''
분류 : DFS & BFS
문제 : 영역 구하기 (백준 2583)
작성일자 : 2021.03.27
'''

# 목적 : 연결요소의 개수와, 각 연결요소의 원소 수를 오름차순으로 출력
# 접근 : 처음 0인 곳을 만났을 때를 count하고, 그 연결요소를 bfs탐색하고
#       연결요소의 원소수를 count한다 
#       입력되는 좌표계를 리스트의 index와 맞게 수정하는 작업이 필요하다 
#       90도로 뒤집어 주면 b~d, a~c로 index처리가 가능하다
import sys
from collections import deque

def bfs(i,j) : 
    global cnt 
    # print(i,j)
    if shape[i][j] == 0 :
        cnt += 1
        shape[i][j] = 1
        queue = deque([(i,j)])
        while queue : 
            x, y = queue.popleft()
            for k in range(4) : 
                nx, ny = x + dx[k], y + dy[k]
                if (0<=nx<M and 0<=ny<N) and shape[nx][ny] == 0 : 
                    cnt += 1
                    shape[nx][ny] = 1
                    queue.append((nx,ny))
        return True 
    else :
        return False 

# 맵을 입력받기 
M, N, K = map(int, input().split())
shape = [[0]*(N) for _ in range(M)]
for _ in range(K) : 
    a, b, c, d = map(int, sys.stdin.readline().rstrip().split())
    for i in range(b,d) : 
        for j in range(a,c) : 
            shape[i][j] = 1
'''
    temp_1,temp_2 = a,c
    b, d = abs(M-b), abs(M-d)
    a, c = b,d
    b, d = temp_1, temp_2
    # print(a,b,c,d)
    for i in range(c,a) :
        for j in range(b,d) : 
            # print(i,j)
            shape[i][j] = 1
'''
for s in shape : 
    print(*s)
dx = [-1,1,0,0]
dy = [0,0,-1,1]
count = 0
cnt = 0 
ans = []
# 맵을 순회하며 연결요소의 수를 세기 
for i in range(M) : 
    for j in range(N) : 
        cnt = 0
        if bfs(i,j) == True : 
            count += 1
            ans.append(cnt)
            # cnt = 0
            # print(cnt)
ans.sort()
print(count)
print(*ans)