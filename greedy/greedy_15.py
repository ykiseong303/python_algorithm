'''
분류 : 그리디 알고리즘
문제 : 설탕배달 (백준 2839번)
작성일자 : 2021.03.01
'''

## 목적 : 입력받은 수를 -5와 -3의 연산을 선택해서 최소 연산 수 출력
## 접근 : 연산 수가 최소이려면, 5를 빼는 것을 제일 우선시. 그렇게 해서 안되면 3을 빼는 방법으로 
##       특정 조건에 대한 구현도 필요
'''
# 다른 풀이 (1)
# 3을 최소한으로 쓰기 
N = int(input())
count = 0
while 1 : 
    if not N%5 : 
        print(N//5 + count)
        break
    N -= 3
    count += 1 
    if N < 0 : 
        print(-1)
        break
'''
'''
# 다른풀이 (2)
# 5를 다쓰고, 1개씩 빼기
N = int(input())
five = N//5
three = 0
N = N%5

while five >= 0 :
    if N % 3 == 0 : 
        three = N//3
        N = N%3 
        break
    five -= 1
    N += 5
print(N==0 and (three + five) or -1)
'''

'''
N = int(input())
current = N
count = 0
lst = []
a=5001
while 1 : 
    if not N%5  : 
        print(N//5)
        break
    else :
        #print("else", count)
        current -= 5
        count += 1
        if not current%3 and current > 0: 
            a = current%3
            temp = count + current//3
            lst.append(temp)
            #print(lst)

        elif current < 0 : 
            if(N-a)== N : 
                #print("min",min(lst))
                print(min(lst))
                break
            elif not N%3 : 
                #print("%3", N//3)
                print(N//3)
                break
            else : 
                print(-1)
                break
'''


