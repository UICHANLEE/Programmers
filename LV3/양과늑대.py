from collections import defaultdict
def solution(info, edges):
    answer = 0
    dic = {}
    Node = defaultdict(list)
    pred = edges[0][0]
    sheep = 1
    wolf = 0
    for i in range(len(info)):
        dic[i] = info[i]
    
    for i in range(len(edges)):
        Node[edges[i][0]].append(edges[i][1])
            

    print(Node)
    print(dic)

    return answer

print(solution([0,0,1,1,1,0,1,0,1,0,1,1], [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]))