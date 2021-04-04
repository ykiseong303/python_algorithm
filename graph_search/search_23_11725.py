'''
분류 : DFS & BFS
문제 : 트리의 부모 찾기 (백준 11725)
작성일자 : 2021.04.04
'''   

# 목적 : 2번노드부터 부모노드를 출력한다
# 접근 : 링크드 리스트 방식으로 해당 인덱스(정점)에 연결되는 정점을 저장한다
#       딕셔너리를 사용한 방법 참고해보기 https://velog.io/@bye9/%EB%B0%B1%EC%A4%80%ED%8C%8C%EC%9D%B4%EC%8D%AC-11725-%ED%8A%B8%EB%A6%AC%EC%9D%98-%EB%B6%80%EB%AA%A8-%EC%B0%BE%EA%B8%B0
#       graph={i:[] for i in range(1,n+1)}

import sys 
sys.setrecursionlimit(10000000)
def dfs(r) : 
    visit[r] = 1 
    for i in lst[r] : 
        if visit[i] == 0 : 
            visit[i] = 1
            result[i] = r
            dfs(i)

N = int(input())
visit = [0] * (N+1)
result = [0] * (N+1)
lst = {i:[] for i in range(1,N+1)}
for _ in range(N-1) : 
    x, y = map(int, sys.stdin.readline().rstrip().split())
    lst[x].append(y)
    lst[y].append(x)
dfs(1)
for r in range(2,N+1) : 
    print(result[r])
'''
from collections import deque 
import sys 
sys.setrecursionlimit(10000)
def dfs(r) : 
    visit[r] = 1 # 현재 위치를 방문처리
    for i in lst[r] : 
        if i == 0 : continue
        if visit[i] == 0 : 
            result[i] = r 
            dfs(i)

# N은 정점의 개수  
N = int(input())
visit = [0] * (N+1)
lst = [[0] for _ in range(N+1)]
# 부모노드를 체크하기 위한 리스트 생성
result = [0] * (N+1)
for _ in range(N-1) : 
    x, y = map(int, sys.stdin.readline().rstrip().split())
    lst[x].append(y)
    lst[y].append(x)
# print(lst)
dfs(1)
for i in range(2,N+1) : 
    print(result[i])
# q = deque(lst[1])
# print(q)
'''