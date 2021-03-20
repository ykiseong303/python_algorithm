'''
분류 : DFS & BFS
문제 : 음료수 얼려먹기 (이코테 1번)
작성일자 : 2021.03.20
'''

# 얼음틀이 있는데, 0으로 이루어진 부분은 음료수를 채울 수 있고, 1은 칸막이로 채울 수 없다
## 목적 : 얼음틀이 입력되었을 때 만들 수 있는 얼음의 수 를 구하기
## 접근 : 방문하지않은 지점이 있을 때마다 count를 증가시킨다 
##       방문한 지점이 0이라면 해당 지점의 상하좌우를 다시 탐색하며 나머지를 1로 채워나간다
##       dfs,bfs를 이용하여 구현 

from collections import deque
# bfs를 이용한 구현
def bfs (i,j) : 
    # 우선 해당 지점이 0인지 1인지 구분
    if shape[i][j] == 0 : 
        myQue = deque([(i,j)]) # 해당 지점을 큐에 삽입

        while myQue : # 큐에 값이 없을떄까지
            x, y = myQue.popleft() # 하나씩 빼서 
            if x<= -1 or x>=M or y<=-1 or y>=N : # 범위를 넘는지 조회
                pass # 범위를 넘긴다면 그냥 넘긴다 
            elif shape[x][y] == 0 : # 범위를 넘지 않고 그 값이 0이라면
                shape[x][y] = 1 
                # 해당 지점의 상하좌우 좌표를 큐에 삽입한다 
                myQue.append((x-1,y))
                myQue.append((x+1,y))
                myQue.append((x,y-1))
                myQue.append((x,y+1))
        return True # 지점이 0이면 방문되지 않은 곳이므로 True  
    else : 
        return False 
# dfs를 이용한 구현
def dfs (i,j) : 
    # 범위를 벗어난 지점은 통과시킨다
    if i<=-1 or i>=M or j<=-1 or j>=N : 
        return 
    if shape[i][j] == 0 : # 방문하지 않았다면 
        shape[i][j] = 1 # 1로 변환
        # 해당 지점의 상하좌우를 탐색
        dfs(i-1,j) 
        dfs(i+1,j)
        dfs(i,j-1)
        dfs(i,j+1)
        # 맨 처음 방문한 곳이 어쩄든 0이므로 True를 리턴
        return True
    # 0이 아니라면 이미 방문했거나 칸막이인 부분이므로 False처리 
    else : 
        return False 

M, N = map(int, input().split())
shape = []
for _ in range(M) : 
    # 문자열이 공백없이 입력될 경우 정수형으로 mapping하면 한글자씩 떨어져 나옴 
    # mapping은 iterable한 데이터의 한 원소를 변환시켜주기 때문에 
    shape.append(list(map(int, input())))

count = 0
# shape를 하나씩 탐색
for i in range(M) :
    for j in range(N) : 
        # 첫 위치에서 True인 경우만 (종료지점이 True인 것과 같음)
        if bfs(i,j) == True : 
            for s in shape : 
                print(*s)
            print("\n")
            count += 1
print(count)