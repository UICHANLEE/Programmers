def solution(k, score):
    answer = []
    lst = []
    for i in range(len(score)):
        if len(lst) < k:
            lst.append(score[i])
            lst.sort()
            answer.append(lst[0])
        else:
            if lst[0] < score[i]:
                lst[0] = score[i]
                lst.sort()
                answer.append(lst[0])
            else:
                lst = lst
                answer.append(lst[0])

        
    return answer
