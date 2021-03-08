'''
분류 : 그리디 알고리즘
문제 : 게임을 만든 동준이 (백준 2847번)
작성일자 : 2021.03.08
'''

# 레벨일 올라갈수록 얻는 점수가 증가해야하는데, 낮은 레벨이 더 높은 경우가 있다
## 목적 : 점수를 낮추는데 드는 최소한의 횟수 출력
## 접근 : 가장 높은 레벨을 기준으로해서 낮은 레벨의 점수를 최소한으로 조정한다

N= int(input())
score = []
for _ in range(N) : 
    score.append(int(input()))
score.reverse()
#print(score)
start = score[0]
count = 0
for i in range(1,len(score)) : 
    if start <= score[i] : 
        while 1 : 
            if score[i] < start : 
                break
            score[i] -= 1
            count += 1
        start = score[i]
    else : 
        start = score[i]
        #print("start", start)
    #print("i",i,"score",score[i])
print(count)