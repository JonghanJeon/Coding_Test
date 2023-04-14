def cal(a, b):
    for x in range(max(a,b), a*b+1):
        if x%a == 0 and x%b == 0:
            return x

def solution(arr):
    num = 1
    for item in arr:
        num = cal(num, item)
    return num