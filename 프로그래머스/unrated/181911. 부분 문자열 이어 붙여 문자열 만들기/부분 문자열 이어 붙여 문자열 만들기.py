def solution(my_strings, parts):
    answer = ''
    l = len(my_strings)

    for i in range(l):
        tmp = my_strings[i]
        s, e = parts[i]
        answer += tmp[s:e+1]        
        
    return answer