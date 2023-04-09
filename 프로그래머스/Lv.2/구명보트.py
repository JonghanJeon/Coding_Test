def solution(people, limit):
    answer = 0
    p = sorted(people)
    # 앞쪽 인덱스
    l = 0
    # 뒤쪽 인덱스
    h = len(people)-1
    while(l <= h):
        # 앞사람과 뒷사람 묶었을때 limit 초과시
        if p[l] + p[h] > limit:
            answer += 1
            h -= 1
        # 앞사람과 뒷사람 묶었을때 limit 비 초과시
        else:
            answer += 1
            l += 1
            h -= 1
    return answer