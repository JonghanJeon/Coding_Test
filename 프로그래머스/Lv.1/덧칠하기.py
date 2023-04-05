def solution(n, m, section):
    answer = 0
    paint = section[0]-1
    for item in section:
        if paint < item:
            paint = item+m-1
            answer += 1
        
    return answer