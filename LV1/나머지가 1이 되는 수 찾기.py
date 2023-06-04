def solution(n):
    answer = 0
    ele = []
    for i in range(1, n):
        if n % i == 1:
            ele.append(i)
    answer = ele.pop(0)
    return answer

print(solution(10))