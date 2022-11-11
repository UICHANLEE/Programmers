def solution(ingredient):
    answer = 0
    COUNT = set(['1', '2', '3'])
    

    stack = []

    if len(ingredient)<1000000:
        ingredient = "".join(map(str,ingredient))
    
    for _ in ingredient:
        if '1231' in ingredient:
            ingredient = ingredient.replace('1231', '')
            answer += 1
        elif 
    print(answer)

    


print(solution([2, 1, 1, 2, 3, 1, 2, 3, 1]))