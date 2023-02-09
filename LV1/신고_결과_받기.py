from collections import defaultdict
import collections
def solution(유저_아이디 = list, 설명 = list, 정지_기준 = int) -> list:
    answer = []

    answer = 유저_아이디
    누가_누구에게 = defaultdict(list)
    유저별_신고당한_횟수 = defaultdict(int)
    신고_유저_회신_횟수 = defaultdict(int)
    
    신고당한_아이디 = []
    정지된_아이디 = []

    for 요소 in 유저_아이디:
        누가_누구에게[요소] = []
    
    설명 = list(set(설명))
    for 인덱스 in range(len(설명)):
        설명[인덱스] = 설명[인덱스].split(' ')
        누가_누구에게[설명[인덱스][0]].append(설명[인덱스][1])
        신고당한_아이디.append(설명[인덱스][1])

    유저별_신고당한_횟수 = collections.Counter(신고당한_아이디)
    for 아이디 in 유저_아이디:
        if 아이디 not in 신고당한_아이디:
            유저별_신고당한_횟수[아이디] += 0
    
    신고당한_아이디 = list(set(신고당한_아이디))
    
    for 요소_ in 신고당한_아이디:
        if 유저별_신고당한_횟수[요소_] >= 정지_기준:
            정지된_아이디.append(요소_)
    
    for 아이디 in 유저_아이디:
        for 요소__ in range(len(누가_누구에게[아이디])):
            if 누가_누구에게[아이디][요소__] in 정지된_아이디:
                신고_유저_회신_횟수[아이디] += 1
            else:
                신고_유저_회신_횟수[아이디] += 0

    for 인덱스__ in range(len(answer)):
        answer[인덱스__] = 신고_유저_회신_횟수[answer[인덱스__]]

    return answer

print(solution(['muzi', 'frodo', 'apeach', 'neo'], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))