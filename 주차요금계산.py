# 차량 별로 구분
# IN, OUT 구분
# 기본요금과 아닐 때
from collections import defaultdict
from datetime import datetime as dt
import copy
import math
def solution(fees : list, records: list) -> int:
    answer = []
    
    for i in range(len(records)):
        records[i] = records[i].split(' ')

    time = defaultdict(list)
    
    for t, n, b in records:
        time[n].append(t)
    time = dict(sorted(time.items(), key = lambda x : x[0]))
    
    for n in time.keys():
        if len(time[n]) % 2 == 1:
            time[n].append('23:59')
    
    cal = list(time.values())
    
    for i in range(len(cal)):
        for j in range(len(cal[i])):
            cal[i][j] = cal[i][j].replace(':', '')
            cal[i][j] = int(cal[i][j][:2])*60 + int(cal[i][j][2:])
    
    result = copy.deepcopy(cal)

    for i in range(len(result)):
        result[i].clear()

    for i in range(len(cal)):
        for j in range(len(cal[i])):
            if j % 2 == 1:
                temp = cal[i][j] - cal[i][j - 1]
                result[i].append(temp)

    answer = copy.deepcopy(result)

    for i in range(len(result)):
        result[i] = sum(result[i])
        if result[i] > fees[0]:
            answer[i] = fees[1] + math.ceil(((int(result[i]-fees[0])))/fees[2])*fees[3]
        else:
            answer[i] = fees[1]

    return answer
