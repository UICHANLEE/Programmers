def solution(a, b, n):
    answer = 0
    while n >= a:
        recycle = n // a
        answer += recycle * b
        n = n - a * recycle + recycle * b


    return answer

print(solution(2, 1, 20))
print(solution(3, 1, 20))