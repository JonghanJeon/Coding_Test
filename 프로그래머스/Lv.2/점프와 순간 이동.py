def solution(n):
    # 가장 먼저 반드시 점프(한칸 이동)해야 하므로 answer 은 1로 시작
    answer = 1
    while(n > 1):
        # 순간이동(2배 이동)이 가능 한 경우
        if n % 2 == 0:
            n = n // 2
        # 순간이동이 불가능한 경우
        else:
            n -= 1
            answer += 1
    return answer 