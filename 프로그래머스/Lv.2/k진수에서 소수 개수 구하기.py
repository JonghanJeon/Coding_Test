def calculator(n, q):
    rev_base = ''

    while n > 0:
        n, mod = divmod(n, q)
        rev_base += str(mod)

    return rev_base[::-1] 

def is_prime_number(n):
    if n == 1:
        return False
    for x in range(2, int(n**(1/2)) + 1):
        if n % x == 0:
            return False
    return True

def solution(n, k):
    dic = {}
    s = calculator(n, k)
    li = list(s.split('0'))
    for item in li:
        if item == '':
            continue
        elif is_prime_number(int(item)):
            if item in dic.keys():
                dic[item] += 1
            else:
                dic[item] = 1
    return sum(dic.values())
    