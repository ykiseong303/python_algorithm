'''
분류 : 그리디 알고리즘
문제 : 멀티탭 스케줄링 (백준 1700번)
작성일자 : 2021.03.09
'''

# 각각의 제품이 사용 순서대로 입력된다 
## 목적 : 플러그를 빼는 최소 횟수 출력
## 접근 : 넣을 수 있는 제품은 다 넣고, 꽉찼을 때는 사용 순서가 가장 마지막인 걸 빼기
##       플러그에 하나도 없는 경우, 같은 걸 넣어야 하는 경우 등을 고려

N, K = map(int, input().split())
seq = list(input().split())
concent = []
temp = []
count = 0

for i in range(K) : 
    # print("i",i)
    flag = False
    if len(concent) <= N-1 : 
        if len(concent) == 0 : 
            concent.append([0,seq[i]])
        else : 
            for con in concent : 
                if seq[i] in con[1] : 
                    flag = True
                    break
            if flag == False : 
                concent.append([0,seq[i]])
        # print("if",concent)
    # 콘센트가 꽉차있는 경우 
    else : 
        for con in concent : 
            if seq[i] in con[1] : 
                flag = True
                break
        if flag == False : 
            temp = seq[i:]
            for j in range(len(concent)) : 
                if concent[j][1] in temp : 
                    concent[j][0] = temp.index(concent[j][1])
                else : 
                    concent[j][0] = 1000
                # print("temp",temp)
            concent.pop(concent.index(max(concent)))
            concent.append([0,seq[i]])
            # print(concent)
            count += 1 
print(count)