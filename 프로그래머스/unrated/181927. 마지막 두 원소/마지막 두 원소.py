def solution(num_list):
    answer = []
    answer.extend(num_list)
    n = len(num_list)
    a = num_list[n-1]
    b = num_list[n-2]
    if a > b:
        answer.append(a-b)
    else:
        answer.append(a*2)
    return answer