def solution(s):
    answer = 0
    
    S = []
    US = []
    result = []
    for i in range(len(s)):
        if len(S) == 0:
            S.append(s[i])
        elif s[i] == S[0]:
            S.append(s[i])
        elif s[i] != S[0]:
            US.append(s[i])
        if len(S) == len(US):
            result.append(S.extend(US))
            S.clear()
            US.clear()
    if len(S) != 0:
        result.append(S)
    answer += len(result)
    return answer
