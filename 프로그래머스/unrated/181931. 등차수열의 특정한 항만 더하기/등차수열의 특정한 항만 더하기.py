def solution(a, d, included):
    answer = 0
    n = len(included)
    blank = []
    
    for i in range(n):
        tmp = a + d * i
        blank.append(tmp)
        
    for j in range(n):
        if included[j]:
            answer = answer + blank[j]
            
    return answer