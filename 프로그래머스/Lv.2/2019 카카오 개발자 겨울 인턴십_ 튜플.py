def solution(s):
    # list 사용시 not in 연산시 시간이 오래걸림
    # 따라서 dictionary 사용
    answer = {}
    # 문자열에서 필요한 숫자들만 나눔.
    s = s[2:-2].split('},{')
    # 길이가 가장 짧은 것 부터 정렬
    s = sorted(s, key = lambda x : len(x))
    # 각 숫자들의 모임에 대해
    for item in s:
        # 원소를 나누고
        li = list(item.split(','))
        # 각 원소에 대해
        for item in li:
            # answer 에 포함되어 있지 않은 숫자만 dictionary에 추가
            if int(item) not in answer:
                # key 에 해당하는 value 는 아무거나 상관 없음
                answer[int(item)] = 1
    return list(answer.keys())