'''
분류 : 그리디 알고리즘
문제 : A->B (백준 16953)
작성일자 : 2021.03.13
'''

# A를 2를 곱하거나 뒤에 1을 붙여서 B를 만든다
## 목적 : B를 만들 수 있는 최소 연산의 횟수 출력
## 접근 : B에서 부터 A를 만들어간다 
##       BFS 자료구조 필요 (현재 풀이와 다르게)

# 다른 풀이 2
## 덱(큐를 써도 무방)자료구조를 사용한 풀이
## 2가 *2 혹은 끝에 1붙이기를 통해 얻을 수 있는 모든 경우를 그래프로 나타내고
## 이를 BFS로 탐색
from collections import deque

A, B = map(int, input().split())

# 세트 자료형으로 대입
queue = deque([(A,1)])
result = -1 
while queue : 
    # 두개의 인자를 받을 때, set형태로 입력된 자료만 popleft() 사용가능
    temp, cnt = queue.popleft()
    # print(temp, cnt)
    if temp == B : 
        result = cnt
        break
    if temp*2 <= B : 
        # cnt += 1을 하지 않는 이유는, 아래의 if문에서 또 cnt가 1 증가할 수 있으므로
        # cnt += 1
        ## 대입되는 ()자료형은 iterable argument가 아니므로 extend불가 
        queue.append((temp*2,cnt+1))
    if int(str(temp)+'1') <= B : 
        # cnt += 1 
        queue.append((int(str(temp)+'1'),cnt+1))
    # print(queue)
print(result)

'''
# DFS를 이용한 구현 방법 (결과는 같음)
stack = [(A,1)]
result = -1
while stack : 
    # print(stack)
    # temp, cnt = stack.pop()
    # print("temp",temp)
    if temp==B : 
        result = cnt
        break
    if temp*2 <= B : 
        stack.append((temp*2,cnt+1))
    if int(str(temp)+'1') <= B : 
        stack.append((int(str(temp)+'1'),cnt+1))
print(result)
'''



# 다른 풀이 1 
'''
A, B = map(int, input().split())
count = 0
while 1 : 
    # A와 B가 같으면 중단
    if A==B : 
        break
    # B가 2로 나눠지지 않고, 뒤에 1이 없거나 A보다 작다면 불가능
    elif (B%2 and (B%10 != 1)) or B<A : 
        count = -2
        break
    # 위의 경우가 아니라면 ~ 
    else : 
        # 뒤에 1이 있으면
        if B%10 == 1 : 
            B = B//10 
            count += 1
        # 그렇지 않으면 
        else : 
        # elif not B%2 : (위의 elif 조건에서 B가 2로 나눠지지 않는 경우도 체크하므로)
            B = B//2 
            count += 1
print(count+1)
'''


'''
A, B = map(int, input().split())
count = 0
flag = True
while 1 : 
    # 먼저 B의 맨 끝에 1이 있는지 체크한다
    lst = []
    B = str(B)
    if B[-1] == '1' : 
        for b in B : 
            lst.append(b)
        lst.pop(-1)
        # 11과 같은 경우 예외처리
        if len(lst) == 0 : 
            flag = False 
            break
        count += 1
        B = "".join(lst)
    B = int(B)
    # A와 B가 같은지 비교한다
    if A == B : 
        #print(B)
        break
    else : 
        # 다른데, 나눌 수 있으면 나눠준다
        if not B%2 : 
            B = B//2
            #print(B)
            count += 1
            if A==B : 
                break
    B = str(B)
    if (int(B)%2 and B[-1] != '1') or A>int(B) : 
        flag = False 
        break
    B = int(B)
    #print(B)
if flag == True : 
    print(count+1)
else : 
    print(-1)
'''