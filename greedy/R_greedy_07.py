'''
분류 : 그리디 알고리즘
문제 : ZOAC (백준 18238번)
작성일자 : 2021.02.27
'''

# 원판에 문자들이 순서대로 적혀있고, 화살표가 이 중하나를 가르킨다 (처음에는 A)
# 한번 움직일때마다 1의 시간이 소요되고, 앞 뒤로만 움질일 수 있다.
## 목적 : 입력되는 문자열을 최소한의 시간으로 출력하기
## 접근 : 다음 문자로 갈 수 있는 최소한의 시간이 걸리는 방향으로 움직이기

var = list(input())
result = []
for v in var : 
    a = ord(v) - 64
    result.append(a)

target = 1
count = 0
for i in range(len(result)) :
    #print(i) 
    # 정방향으로 가는 경우
    pre = abs(result[i] - target)
    # 후방향으로 가는 경우
    if target == 1 : 
        pos = abs(27 - result[i])
    else : 
        if target - result[i] < 0 : 
            pos = abs(27 - result[i] + target -1)   
        else : 
            pos = abs(27 - target + result[i] - 1)
    #print(i, pre, pos)
    if pre > pos :
        count += pos 
        #print("pos",count)
    else : 
        count += pre
        #print("pre",count)
    pre, pos = 0,0
    target = result[i]
    #print("tar", target)

print(count)
'''
string = list(input())
start = 'A'
count = 0
for i in string : 
    l = ord(start) - ord(i)
    r = ord(i) - ord(start)
    
    if l < 0 :
        l += 26
    if r < 0 : 
        r += 26
    count+=min(l,r)
    start = i
print(count)
'''
