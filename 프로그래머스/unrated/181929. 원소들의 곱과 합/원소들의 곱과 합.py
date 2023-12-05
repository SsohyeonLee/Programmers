def solution(num_list):
    sum = 0
    mul = 1
    
    for i in range(len(num_list)):
        sum = num_list[i] + sum
        mul = num_list[i] * mul
    
    if mul < sum**2:
        return 1
    else:
        return 0