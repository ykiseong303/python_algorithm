'''
분류 : DFS & BFS
문제 : 숨바꼭질4 (백준 13913)
작성일자 : 2021.05.17
'''

# 목적 : 시작위치에서 목적지까지 도달하는 최단시간 및 경로 표현
# 접근 : 현재위치에서 방문할 수 있는 경우를 모두 탐색
#       다음위치로 탐색하는 데 걸리는 시간은 (현재문제는 이동순서의 가중치가 모두 같음)
#       현재 위치에서 도달할 수 있는 최단시간이고, 
#       방문하지 않은 경우만 탐색하기 때문에 
#       자식의 parent를 기록하는 것 또한 바로 직전의 parent를 기록할 수 있다.

from collections import deque 

def path(x) : 
    q = deque([(x)])
    lst = [x]
    while q : 
        x = q.popleft()
        if x == N : 
            break
        lst.append(move[x])
        q.append((move[x]))
    lst.reverse()
    print(lst)
def bfs() : 
    q = deque([(N)])
    # dist[N] = 1
    while q : 
        x = q.popleft()
        if x == K : 
            print(dist[x])
            # print(x)
            path(x)
            return 
        for i in (x+1, x-1, x*2) : 
            if 0<=i<=100000 and dist[i] == 0 : 
                q.append((i))
                dist[i] = dist[x] + 1
                move[i] = x

N, K = map(int, input().split())
dist = [0] * 100001
move = [0] * 100001
bfs()

'''import sys 
from collections import deque 
input = sys.stdin.readline

def bfs() : 
    global val
    visit[N] = 1
    lst = [N]
    q = deque([(N,0,val)])
    while q : 
        x,cnt,lst = q.popleft()
        # print(x,cnt,lst)
        # print(type(lst),lst)
        if x*2 == K : 
            print(cnt+1)
            print(str(N)+lst,K)
            return 
        elif x*2 < K*10 and visit[x*2] == 0 : 
            visit[x*2] = 1
            q.append((x*2,cnt+1,lst+' '+str(x*2)))
        if x+1 == K : 
            print(cnt+1)
            print(str(N)+lst,K)
            return 
        elif visit[x+1] == 0: 
            visit[x+1] = 1
            q.append((x+1,cnt+1,lst+' '+str(x+1)))
        if x-1 == K : 
            print(cnt+1)
            print(str(N)+lst,K)
            return 
        elif x-1 >= 0 and visit[x-1] == 0: 
            visit[x-1] = 1 
            q.append((x-1,cnt+1,lst+' '+str(x-1)))

N, K = map(int, input().split())
visit = [0] * 200001
val = ''
if N == K : 
    print(0)
    print(N)
else : bfs()'''