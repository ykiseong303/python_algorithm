'''
분류 : 깊이/너비우선 탐색 
문제 : 단어변환 (프로그래머스)
작성일자 : 21.03.29
'''

# 목적 : begin을 target으로 변환하는데 가장 짧은 연산횟수를 출력
# 접근 : 기준 단어와 한글자만 차이나는 단어를 큐에 넣어서 bfs 탐색을 돌린다 
#       다른 사람 풀이에 제너레이터와 zip을 사용한 것이 있던데, 해당 부분은 공부 필요

from collections import deque

def solution(begin, target, words) : 
    visit = [0] * len(words)
    q = deque([(begin, 0)])
    count = 0
    flag = False 
    while q : 
        x, cnt = q.popleft()
        print(x,cnt)
        if x == target : 
            flag = True 
            break
        # print(visit, len(visit))
        for w in words : 
            count = 0
            for i in range(len(w)) : 
                if x[i] != w[i] : 
                    count += 1
                    if count == 2 : 
                        break
                # 한글자만 다른 단어를 찾은 경우 큐에 삽입
                if i == len(w)-1 and count == 1 :
                    if visit[words.index(w)] == 0 : 
                        visit[words.index(w)] = 1
                        q.append((w,cnt+1))
    if flag == True : 
        return cnt
    else : 
        return 0

begin = "hot"
target = "lot"
words = ["hot", "dot", "dog", "lot", "log"]
# words = ["hot", "dot", "dog", "lot", "log", "cog"]
#words = ["hot", "dot", "dog", "lot", "log"]

print(solution(begin,target,words))