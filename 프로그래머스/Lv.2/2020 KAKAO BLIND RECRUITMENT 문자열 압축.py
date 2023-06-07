# 문제의 핵심: 가능한 조합을 모두 검사해 보는 것!

def compress(s, length):
    # 모든 규칙생성. 
    words = [s[i: i+length] for i in range(0, len(s), length)]
    # 빈 배열
    res = []
    # 첫 규칙
    cur_word = words[0]
    # 중복되는 횟수
    cur_cnt = 1
    # zip 반복
    for pattern, comp in zip(words, words[1:] + ['']):
        # 현재규칙과 비교규칙이같을 경우 중복횟수 증가 
        if pattern == comp: cur_cnt += 1
        # 현재규칙과 비교규칙이 다를경우
        else:
            # res 에 append
            res.append([cur_word, cur_cnt])
            # 현재 규칙을 비교규칙으로 바꿈.
            cur_word = comp
            # 중복횟수는 다시 1
            cur_cnt = 1
    # res 에 포함된 규칙과 중복 횟수를 모두 더함
    # 단 cur_cnt 이하 cnt 가 1이상일 경우 추가해주고 아닌경우 추가하지 않음.
    return sum(len(word) + (len(str(cnt)) if cnt > 1 else 0) for word, cnt in res)

def solution(s):
    # answer = len(s)
    # for x in range(1, len(s)//2 + 1):
    #     comp_len = 0
    #     comp = ''
    #     cnt = 1
    #     for i in range(0, len(s), x):
    #         tmp = s[i:i+x]
    #         if comp == tmp: cnt += 1
    #         elif comp != tmp:
    #             comp_len += len(tmp)
    #             if cnt > 1:
    #                 comp_len += len(str(cnt))
    #             cnt = 1
    #             comp = tmp
    #     answer = min(answer, comp_len)
    # return answer
    
    # 모든 규칙 찾아서 비교
    # 단 단어 길이가 1일 경우는 예외 처리로 1로 반환.
    if len(s) == 1: return 1
    # 만든 함수를 전부 적용 시킴. 
    # 1개짜리 규칙, 2개짜리 규칙,
    # ... 
    # 전체 길이의 1/2개에 해당하는 규칙
    # 해서 길이가 가장 짧은 놈 반환.
    else: return min(compress(s, length) for length in list(range(1, len(s)//2 + 1))) 