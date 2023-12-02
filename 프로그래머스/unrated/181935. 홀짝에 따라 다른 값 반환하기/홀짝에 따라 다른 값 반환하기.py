def solution(n):
    answer = 0
    if n%2 == 1:
        for i in range(n+1):
            if i % 2 == 1:
                answer = i + answer
        return answer
    
    else:
        for i in range(n+1):
            if i % 2 == 0:
                tmp = i ** 2
                answer = tmp + answer
        return  answer