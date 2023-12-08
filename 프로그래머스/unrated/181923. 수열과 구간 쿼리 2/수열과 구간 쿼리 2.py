def solution(arr, queries):
    answer = []
    for s,e,k in queries:
        min_val = float('inf')
        for i in range(s,e+1):
            if k < arr[i] and arr[i] < min_val:
                min_val = arr[i]
        answer.append(min_val if min_val != float('inf') else -1)
    return answer