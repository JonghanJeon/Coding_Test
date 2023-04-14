def solution(s):
    cnt, cnt0 = 0, 0
    while s != '1':
        cnt += 1
        cnt1 = s.count('1')
        cnt0 += s.count('0')
        s = bin(cnt1)[2:]
    return [cnt, cnt0]