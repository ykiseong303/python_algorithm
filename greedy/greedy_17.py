'''
분류 : 그리디 알고리즘
문제 : 로프 (백준 2217번)
작성일자 : 2021.03.02
'''

# K개의 로프가 주어질 때, K개의 로프에는 w/K만큼의 중량이 걸린다
## 목적 : K개의 로프를 사용하여 들 수 있는 최대 용량 (모두 사용할 필요 x)
## 접근 : 최대 중량이 가장 큰 로프부터 1개씩 추가해서 들 수 있는 최대 중량 출력
##       큰 것 부터 해보기, 넘사벽으로 큰 값이 딱 하나면 그 값이 답이지만, 
##       비슷한 값이 여러개가 있는 경우를 고려해야함

N = int(input())
rope = []
for _ in range(N) : 
    x = int(input())
    rope.append(x)
rope.sort(reverse=True)
#rope.reverse()
max_weight = []

weight = 0
for i in range(len(rope)) : 
    temp = rope[i] * (i+1)
    if temp > weight : 
        weight = temp
print(weight)

'''
# 효과적이지 않은 풀이
# 이유는 N<=10000일 경우 for 문에서 시간초과 발생
# 불필요한 반복문을 진행하기 때문

N = int(input())
rope = []
for _ in range(N) : 
    x = int(input())
    rope.append(x)
rope.sort()
rope.reverse()
#print(rope)
max_weight = []
num = 0 
while 1 : 
    #print(num)
    weight = 0
    cur_weight = []
    for i in range(0,num+1) : 
        weight = (num+1) * rope[i]
        #print("weight :",weight)
        cur_weight.append(weight)
        #print(cur_weight)
    max_weight.append(min(cur_weight))
    #print(max_weight)
    num += 1
    if num > len(rope) - 1 :
        break
print(max(max_weight))
'''