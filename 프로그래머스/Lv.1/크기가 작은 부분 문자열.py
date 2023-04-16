# len(t) - len(p) 까지 for
def solution(t, p):
    answer = 0
    for idx in range(0, len(t)-len(p)+1):
        if int(t[idx:idx+len(p)]) <= int(p):
            answer += 1
    return answer