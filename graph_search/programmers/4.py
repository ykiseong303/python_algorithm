def dfs (start, target,length,visit,answer,temp) : 
    # global length
    # global visit
    # global answer
    for i in range(length) : 
        if tickets[i][0] == start and tickets[i][1] == target :
            if visit[i][1] == 0:
                visit[i][1] = 1
                print(visit)
                answer.append(target) 
                break   
    for j in range(length) :
        # print(target)
        if tickets[j][0] == target and tickets[j][1] in temp: 
            print("yes",tickets[j][0],tickets[j][1])
            if visit[j][1] == 0 :
                print("not visit") 
                print(tickets[j][0],tickets[j][1])
                dfs(tickets[j][0],tickets[j][1],length,visit,answer,temp)


def solution(tickets):
    answer = ["ICN"]
    # 우선 티켓을 정렬하기 
    tickets.sort(key=lambda x: (x[0],x[1]))
    print(tickets)
    # ICN을 찾기 
    length = 0
    for t in tickets : 
        length += 1 
    # 출발지 리스트를 만들기 
    temp = [] 
    for j in range(length) :
        temp.append(tickets[j][0])
    for i in range(length) : 
            if tickets[i][0] == "ICN" and (tickets[i][1] in temp):
                target = tickets[i][1]
                start = tickets[i][0]
                # print(target, start)
                break
    # 방문처리를 위한 리스트 생성
    visit = [[0]*2 for _ in range(length)]
    dfs(start, target,length,visit,answer,temp)
    print(answer)
    return answer

# tickets = [["ICN","A"],["ICN","B"],["B","ICN"]]

tickets = [["ICN","A"],["ICN","A"],["A","ICN"],["A","C"]]

# tickets = [["ICN", "A"], ["A", "ICN"], ["ICN", "A"],["A","ICN"],["ICN","C"]]
# tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
# tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
solution(tickets)
