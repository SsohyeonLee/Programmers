def solution(a, b):
    a1 = int(f"{a}{b}")
    a2 = 2*a*b
    if a1>=a2:
        return a1
    else:
        return a2