def solution(record):
    answer = []
    dic = {}
    for i in range(len(record)):
        record[i] = record[i].split(' ')
        if record[i][0] != 'Leave':
            dic[record[i][1]] = record[i][2]
        elif record[i][0] == 'Leave':
            record[i].append(dic[record[i][1]])
    
    for i in range(len(record)):
        if record[i][0] == 'Enter':
            answer.append("{0}님이 들어왔습니다.".format(dic[record[i][1]]))
        elif record[i][0] == 'Leave':
            answer.append("{0}님이 나갔습니다.".format(dic[record[i][1]]))
        
    return answer

