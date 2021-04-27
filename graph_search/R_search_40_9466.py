'''
분류 : DFS & BFS
문제 : 텀 프로젝트 (백준 9446)
작성일자 : 2021.04.27
'''

# 목적 : 사이클에 포함되지 않는 정점의 수를 출력 (시간초과에 유의, 단 한번의 DFS로)
# 접근 : dfs를 수행하며, 사이클의 마지막 원소가 가리키는 원소가 사이클의 시작
#       첫번째 방법은, 임의의 정점에서부터 시작하여 사이클의 마지막 원소까지 그룹번호를 부여하고, 
#       마지막 번호가 가리키는 원소에서부터 사이클을 이루는 원소만 -1을 대입
#       두번째 방법은, 임의의 정점을 리스트에 추가하며 dfs를 수행 > 
#       방문한적이 있는데, 리스트에 들어있는 값이라면(그 값이 시작원소)
#       거기서부터 사이클의 시작이므로 별도로 저장
##      순열사이클의 수 문제(28)와 다르게 사이클이 되는 정점으로만 구성된 것이 아닌 문제
##      또한 여기서는 한 정점이 딱 한곳만 가리키므로 인접리스트로 표현할 필요x
##      정점이 한곳만 가리키는 단방향 그래프이면 하나의 연결요소에서 하나의 사이클만 존재할 수 있다

# 다른 풀이
import sys 
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

T = int(input())
for _ in range(T) : 
    N = int(input())
    lst = [0] + list(map(int, input().split()))
    visit = [0] * (N+1)
    group = 1
    for i in range(1,N+1) :
        if visit[i] == 0 : # 방문한적이 없다면
            while visit[i] == 0 : # 임의의 정점에서 사이클을 모두 돌때까지
                visit[i] = group # 그룹번호를 지정
                i = lst[i] # 다음 정점으로 변환
            # 첫번째 while문의 종료시 i는 사이클의 시작위치를 가리킴
            while visit[i] == group : # 사이클을 이루는 정점의 값을 모두 바꿀때까지
                visit[i] = -1 # 사이클의 시작위치부터 -1을 대입 (양수,음수구분)
                i = lst[i] # 다음 정점변환
        group += 1 # 그룹번호를 증가
    cnt = 0
    for v in visit : 
        if v > 0 : 
            cnt += 1 
    print(cnt)

'''
import sys 
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

def dfs(start) : 
    global lst, ans
    visit[start] = 1
    lst.append(start)
    # print("start",start)
    for i in adj_lst[start] : 
        if visit[i] == 0 : 
            # lst.append(i)
            dfs(i)
        elif visit[i] == 1 and i in lst : 
            ans += lst[lst.index(i):]

            # print(lst)
            # result += len(lst)
            return 


T = int(input())
for _ in range(T) : 
    N = int(input())
    adj_lst = [[] for _ in range(N+1)]
    lst = list(map(int, input().split()))
    for i in range(1,N+1) : 
        adj_lst[i].append(lst[i-1])
    visit = [0] * (N+1)
    lst = []
    result = 0
    ans = []
    for i in range(1,N+1) : 
        if visit[i] == 0 : 
            dfs(i)
            lst = []
            # visit = [0] * (N+1)
    # print(result)
    print(N - len(ans))'''