from collections import defaultdict
def solution(survey, choices):
    answer = ''
    dic = defaultdict(int)
    type = ['RT', 'CF', 'JM', 'AN']
    
    for i in range(len(choices)):
        if choices[i] == 4:
            dic[survey[i][0]] += 0
            dic[survey[i][1]] += 0
        elif choices[i] <= 3:
            dic[survey[i][0]] += (4-choices[i])
            dic[survey[i][1]] += 0
        elif choices[i] <= 7:
            dic[survey[i][1]] += (choices[i]-4)
            dic[survey[i][0]] += 0
    
    for i in range(len(type)):
        type[i] = ''.join(sorted(type[i]))
        print(type[i])
        if dic[type[i][0]] >= dic[type[i][1]]:
            answer += type[i][0]
        else:
            answer += type[i][1]

        
    return answer
print(solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]))