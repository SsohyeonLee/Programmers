def solution(my_string, queries):
    answer = ''
    my_string = list(my_string)
    
    for s,e in queries:
        tmp = my_string[s:e+1]
        my_string = (my_string[:s] + tmp[::-1] + my_string[e+1:])
            
        answer = ''.join(my_string)
    return answer