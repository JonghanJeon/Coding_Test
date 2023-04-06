def solution(n):
    num = n
    while(True):
        num += 1
        if bin(num).count('1') == bin(n).count('1'):
            return num