'''
분류 : DFS & BFS
문제 : 맥주 마시면서 걸어가기 (백준 9205)
작성일자 : 2021.04.06
'''   

# 목적 : 목적지까지 갈 수 있는지를 체크
# 접근 :  
#       1. bfs를 이용한 풀이 : 현재 위치에서 갈 수 있는 - 즉, child - 노드를 모두 큐에 넣고 )
#          bfs를 돌리면서 목적지에 도달 할 수 있는지 검사
#       2. 플로이드-워셜을 이용한 풀이 : 모든 정점에서 모든 정점으로 이동할 수 있는 최단거리를 구하기
#          이 문제에서는 목적지까지의 최단거리가 max값인 1000보다 작으면 성공으로처리
#          O(N^3)의 시간복잡도를 가지지만, 입력데이터가 크지 않다는 점에서 문제 없음


'''
# bfs를 이용한 풀이

from collections import deque 
import sys 

def calDist(a,b) : 
    # print(a,b)
    x1,y1 = a
    x2,y2 = b
    return abs(x1-x2) + abs(y1-y2)

def bfs(lst) : 
    q = deque([(s_x,s_y)])
    # 현재 위치를 방문처리
    visit[0] = True 
    while q : 
        now = q.popleft()
        # print("now",now)
        # 현재 위치에서 목적지까지 갈 수 있다면
        if calDist(now, des) <= 1000 : 
            print("happy")
            return 
        for i in range(len(home)) : 
            if visit[i] or calDist(now,home[i]) > 1000 : 
                continue 
            visit[i] = True 
            q.append((home[i]))
    print("sad")

t = int(input())
for _ in range(t) : 
    N = int(input())
    cvs = []
    s_x, s_y = map(int, sys.stdin.readline().rstrip().split())
    home = [[s_x,s_y]]
    for _ in range(N) : 
        x, y = map(int, sys.stdin.readline().rstrip().split())
        cvs.append([x,y])
    home.extend(cvs)
    t_x, t_y = map(int, sys.stdin.readline().rstrip().split())
    des = [t_x,t_y]
    home.append([t_x,t_y])
    visit = [False] * (N+2)
    bfs(home)
'''