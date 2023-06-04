def solution(food):
    answer = ''
    for i in range(1, len(food)):
        if food[i] >= 2:
          while food[i] >= 2:
            ch = food.index(food[i])
            ch = str(ch)
            answer += ch
            food[i] -= 2
    answer += '0'
    a = answer[:-1]
    a = list(a)
    a.reverse()
    a = "".join(a)
    answer += a

    return answer
   
solution([1, 3, 4, 6])