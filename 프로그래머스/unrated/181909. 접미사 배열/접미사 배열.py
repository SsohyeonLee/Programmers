def solution(my_string):
    answer = []
    l = len(my_string)
    for i in range(l):
        answer.append(my_string[-i:])
    return sorted(answer)