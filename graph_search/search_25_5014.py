'''
분류 : DFS & BFS
문제 : 스타트링크 (백준 5014)
작성일자 : 2021.04.08
'''   

# 목적 : 목적지까지 도달하기 위한 최소 연산횟수 출력
# 접근 : 현재위치에서 갈 수 있는 두가지 방법을 순서대로 탐색(bfs)
#       목적지까지 도달할 수 있는 최소 연산횟수이므로 최단거리 탐색과 동일
#       A->B만들기 문제와 동일 

from collections import deque 

def bfs(s) : 
    q = deque([(s,0)])
    visit[s] = 1
    lst = 'use the stairs'
    while q : 
        x, cnt = q.popleft()
        # print(x, cnt)
        if x == g : 
            return cnt
        for i in range(2) :
            if i == 1 : 
                nx = x - el[i] 
            else : 
                nx = x + el[i] 
            if 1<=nx<=f and visit[nx] == 0 : 
                visit[nx] = 1 
                q.append((nx,cnt+1))
                
    return lst
f, s, g, u, d = map(int ,input().split())
el = [u,d]
visit = [0] * (f+1)
print(bfs(s))