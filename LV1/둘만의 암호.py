def solution(s, skip, index):
    answer = ''
    
    ran = []
    for j in range(97, 123):
        if chr(j) not in skip:
            ran.append(j)

    for i in range(len(s)):
        if (ran.index(ord(s[i])) + index) < len(ran):
            asci = ran[((ran.index(ord(s[i])) + index))]
        else:
            asci = ran[((ran.index(ord(s[i]))) + index) - len(ran)]
        
        answer += chr(asci)
    
    return answer

# def solution(s, skip, index):
#     answer = ''
    
#     ran = [i for i in range(97, 123)]
#     for j in range(len(skip)):
#         vs = ord(skip[j])
#         if vs in ran:
#             ran.remove(vs)

#     for i in range(len(s)):
#         if (ran.index(ord(s[i])) + index) < len(ran):
#             asci = ran[((ran.index(ord(s[i])) + index))]
#         else:
#             asci = ran[((ran.index(ord(s[i]))) + index) - len(ran)]
        
#         answer += chr(asci)
    
#     return answer
