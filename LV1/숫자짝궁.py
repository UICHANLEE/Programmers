def solution(X, Y):
    answer = ''
    temp = []
    X_i = []
    for i in range(len(X)):
        X_i.append(X[i])
    for j in range(len(X_i)):
        if X_i[j] in Y:
            temp.append(X_i[j])
            Y = Y.replace(X_i[j], '', 1)
    temp.sort(reverse = True)
    answer = ''.join(temp)
    if answer == '':
        answer = '-1'
    if answer.strip('0') == '':
        answer = '0'
    return answer

print(solution("100", "203045"))