def solution(n,a,b):
    answer = 0

    while(True):
        a -= 1
        b -= 1
        a = a//2 + 1
        b = b//2 + 1
        answer += 1
        if a == b:
            break

    return answer