'''
분류 : 깊이/너비우선 탐색 
문제 : 네트워크 (프로그래머스)
작성일자 : 21.03.28
'''

# 목적 : 연결요소의 개수 출력
# 접근 : 간선이 주어진 경우이므로, 정점간의 연결관계를 나타내는 matrix를 생성하고
#       1번 정점부터 N번까지 bfs를 돌리며 방문하지 않은 곳을 count한다

from collections import deque

def s(n,lst) : 
    count = 0
    cnt = 0
    result = 0
    for l in lst : 
        count += 1
        for a in l : 
            cnt += 1
    visit = [0] *count
    for i in range(count) : 
        for j in range(count) :
            if i == j : 
                lst[i][j] = 0
    for i in range(count) : 
        # print(i)
        if visit[i] == 0 : 
            # bfs(i)
            q = deque([i])
            while q : 
                x = q.popleft()
                for i in range(count) : 
                    if lst[x][i] == 1 and visit[i] == 0 : 
                        visit[i] = 1
                        q.append(i)
            result += 1
    print(result)



    return 
# l = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
# s(3, l)

# l = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
l = [[1,0,0]]
s(3,l)