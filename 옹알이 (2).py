'''
머쓱이는 태어난 지 11개월 된 조카를 돌보고 있습니다. 
조카는 아직 "aya", "ye", "woo", "ma" 네 가지 발음과 네 가지 발음을 조합해서 만들 수 있는 발음밖에 하지 못하고 연속해서 같은 발음을 하는 것을 어려워합니다. 
문자열 배열 babbling이 매개변수로 주어질 때, 머쓱이의 조카가 발음할 수 있는 단어의 개수를 return하도록 solution 함수를 완성해주세요.
'''

'''
1 ≤ babbling의 길이 ≤ 100
1 ≤ babbling[i]의 길이 ≤ 30
문자열은 알파벳 소문자로만 이루어져 있습니다.
'''




def solution(babbling):
    answer = 0

    babbling_Element = ['aya', 'ye', 'woo', 'ma']
    babbling_Element2 = []
    babbling_Element3 = []
    babbling_Element4 = []
    
    

    if len(babbling) <= 100:
        babbling = babbling

    for i in range(len(babbling)):
        if len(babbling[i]) <= 30:
            babbling[i] = babbling[i]

    for i in range(len(babbling_Element)):
        for j in range(len(babbling_Element)):
            if babbling_Element[i] != babbling_Element[j]:
                ch = babbling_Element[i] + babbling_Element[j]
                babbling_Element2.append(ch)

    
    for i in range(len(babbling_Element)):
        for j in range(len(babbling_Element)):
            for k in range(len(babbling_Element)):
                if babbling_Element[i] != babbling_Element[j] and babbling_Element[j] != babbling_Element[k]:
                    ch = babbling_Element[i] + babbling_Element[j] + babbling_Element[k]
                    babbling_Element3.append(ch)


    for i in range(len(babbling_Element)):
        for j in range(len(babbling_Element)):
            for k in range(len(babbling_Element)):
                if babbling_Element[i] != babbling_Element[j] and babbling_Element[j] != babbling_Element[k] and babbling_Element[i] != babbling_Element[k]:
                    ch = babbling_Element[i] + babbling_Element[j] + babbling_Element[k]
                    babbling_Element3.append(ch)

    for i in range(len(babbling_Element)):
        for j in range(len(babbling_Element)):
            for k in range(len(babbling_Element)):
                for l in range(len(babbling_Element)):
                    if babbling_Element[i] != babbling_Element[j] and babbling_Element[i] != babbling_Element[k] and babbling_Element[i] != babbling_Element[l] and \
                        babbling_Element[j] != babbling_Element[k] and babbling_Element[j] != babbling_Element[l] and \
                        babbling_Element[k] != babbling_Element[l]:
                        ch = babbling_Element[i] + babbling_Element[j] + babbling_Element[k] + babbling_Element[l]
                        babbling_Element4.append(ch)

    
    for i in range(len(babbling_Element)):
        for j in range(len(babbling_Element)):
            for k in range(len(babbling_Element)):
                for l in range(len(babbling_Element)):
                    if babbling_Element[i] != babbling_Element[j] and \
                        babbling_Element[j] != babbling_Element[k] and \
                        babbling_Element[k] != babbling_Element[l]:
                        ch = babbling_Element[i] + babbling_Element[j] + babbling_Element[k] + babbling_Element[l]
                        babbling_Element4.append(ch)

    for i in range(len(babbling)):
        if babbling[i] in babbling_Element:
            answer += 1
        elif babbling[i] in babbling_Element2:
            answer += 1
        elif babbling[i] in babbling_Element3:
            answer += 1
        elif babbling[i] in babbling_Element4:
            answer += 1


    print(babbling_Element)
    print(babbling_Element2)
    print(babbling_Element3)
    print(babbling_Element4)
    
    return answer

print(solution(["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]))