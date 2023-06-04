def solution(t, p):
    answer = 0
    cut = len(p)
    Operations = []
    for i in range(len(t)-cut+1):
        Operations.append(t[i:i+cut])
    
    for i in range(len(Operations)):
        if int(p) >= int(Operations[i]):
            answer += 1
    return answer