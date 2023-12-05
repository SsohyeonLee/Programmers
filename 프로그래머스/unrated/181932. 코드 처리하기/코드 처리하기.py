def solution(code):
    mode = 0
    answer = ''
    
    for i in range(len(code)):
        if mode == 0:
            if code[i:i+1] == '1':
                mode = 1
            else:
                if i % 2 == 0:
                    answer = answer + code[i:i+1]                    
        else:
            if code[i:i+1] == '1':
                mode = 0
            else:
                if i % 2 == 1:
                    answer = answer + code[i:i+1]
    
    if answer == '':
        return "EMPTY"
    else:       
        return answer