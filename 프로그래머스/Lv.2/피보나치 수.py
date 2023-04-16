def solution(n):
    li = [0, 1]
    for _ in range(2, n):
        sum_li = sum(li)
        li = [li[1], sum_li]
    
    return sum(li)%1234567