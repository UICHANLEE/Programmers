from collections import defaultdict
from copy import deepcopy

def solution(s):
    answer = []
    split = []
    exist = []
    for i in range(len(s)):
        split.append(s[i])
    
    spell = defaultdict(int)
    answer = deepcopy(split)

    for i in range(len(split)):
        if split[i] not in exist:
            exist.append(split[i])
            answer[i] = -1
            spell[split[i]] = split.index(split[i])
        elif split[i] in exist:
            temp = answer.index(split[i])
            spell[split[i]] = answer.index(split[i]) - spell[split[i]]
            answer[i] = spell[split[i]]
            spell[split[i]] = temp
            
    return answer