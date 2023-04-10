# 진법 변환 함수 (dictionaty를 하용하여 A, B, C, D, E, F 추가)
def calculator(n, q, dic):
    rev_base = ''
    if n == 0:
        return '0'
    while n > 0:
        n, mod = divmod(n, q)
        if mod >= 10:
            mod = dic[mod]
        rev_base += str(mod)

    return rev_base[::-1] 

def solution(n, t, m, p):
    answer = ''
    dic  = {
        10 : 'A', 11 : 'B', 12 : 'C', 13 : 'D', 14 : 'E', 15 : 'F'
    }
    leng = 0
    number = 0
    while leng < (p + (t-1)*m):
        s = calculator(number, n, dic)
        answer += s
        leng += len(s)
        number += 1
    idx = p-1
    string = ''
    for _ in range(t):
        string += answer[idx]
        idx += m
    return string