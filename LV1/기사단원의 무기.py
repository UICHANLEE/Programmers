def solution(number, limit, power):
    answer = 0
    yaksu = [i for i in range(1, number+1)]
    count = []
    
    for i in range(number):
        if yaksu[i] >= 2:
            for j in range(1, yaksu[i]+1):
                if yaksu[i] % j ==0:
                    count.append(j)
                    
        else:
            count.append(yaksu[i])
        yaksu[i] = len(count)
        count.clear()
    
    for i in range(len(yaksu)):
        if yaksu[i] > limit:
            yaksu[i] = power

        answer += yaksu[i]
    return answer

print(solution(5, 3, 2))