def solution(n, l, r):
    answer = 0
    first_str = '1'
    while n > 0:
        if len(first_str) < r:

            first_str = first_str.replace('0', '00000')
            first_str = first_str.replace('1', '11011')
            
        if len(first_str) >= r:
            first_str = first_str[l-1:r]
        n -= 1

    
    answer = first_str.count('1')

    return answer