def solution(intStrs, k, s, l):
    answer = []
    for i in intStrs:
        tmp = i[s:s+l]
        tmp = int(tmp)
        if tmp > k:
            answer.append(tmp)
    return answer