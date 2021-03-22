'''
분류 : DFS & BFS
문제 : 숨바꼭질 (백준 1697)
작성일자 : 2021.03.22
'''

# 목적 : 원하는 수에 도달하기 까지 걸리는 최소 연산의 수
# 접근 : 세가지 연산을 통해 최단거리를 구하는 것과 같다
#       다만 범위를 어느정도 좁혀줘야 한다 (파생되는 범위가 너무 넓어지므로)
#       방문한 노드또한 체크한다 
#       현재 풀이에서 M+5까지 하면 풀리는데 (시간도 짧음) 어느정도 이해는 가는데
#       (현재 값을 두배해서 M보다 어느정도 초과한 경우에 한해서만 )
#       정확한 이유를 찾는 과정이 필요햘것 같다

from collections import deque

N, M = map(int, input().split())
visited = set()
if N == M : 
    print(0)
else : 
    queue = deque([(N,0)])
    while queue : 
        print(queue)
        x, cnt = queue.popleft()
        visited.add(x)
        #print(visited)
        if x == M : 
            print(cnt)
            break
        if x < M : 
            
            if x*2 not in visited and x*2 < M + 5:
                queue.append((x*2,cnt+1))
                visited.add(x*2)
            if x+1 not in visited : 
                queue.append((x+1,cnt+1))
                visited.add(x+1)
            if x-1 not in visited :
                queue.append((x-1,cnt+1))
                visited.add(x-1)
        else : 
            queue.append((x-1,cnt+1))

        '''
        queue.append((x-1,cnt+1))

        if x*2 <= M : 
            queue.append((x*2,cnt+1))
        if x+1 <= M : 
            queue.append((x+1,cnt+1))
        '''