def solution(s):
    li = list(map(int, s.split()))
    print(li)
    MIN = min(li)
    MAX = max(li)
    answer = f'{MIN} {MAX}'
    return answer