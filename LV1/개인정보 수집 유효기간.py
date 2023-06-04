def solution(today, terms, privacies):
    answer = []
    dic = {}
    ver = []
    for i in range(len(terms)):
        terms[i] = terms[i].split(' ')
        dic[terms[i][0]] = terms[i][1]
    for j in range(len(privacies)):
        privacies[j] = privacies[j].split(' ')
        if privacies[j][1] in dic.keys():
            ver.append([privacies[j][1],((int(today[:4]) - int(privacies[j][0][:4])) * 12 + \
                    (int(today[5:7]) - int(privacies[j][0][5:7])))*28 + (int(today[8:10]) - int(privacies[j][0][8:10]))])
    
    for i in range(0, len(ver)):
        if (ver[i][1]) >= int(dic[ver[i][0]])*28:
            answer.append(i+1)


    return answer



print(solution("2022.05.19", ["A 6", "B 12", "C 3"]	, ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))