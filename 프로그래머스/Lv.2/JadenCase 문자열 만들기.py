def solution(s):
    answer = ''
    prev = ' '
    s = s.lower()
    for c in s:
        if str.isalpha(c) and prev==' ':
            answer += c.upper()
        else:
            answer += c
        prev = c
    return answer